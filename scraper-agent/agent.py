import json
import logging
import time
from datetime import datetime, timezone
from typing import Any, Dict

from anthropic import Anthropic, APIConnectionError, APIStatusError, APITimeoutError, RateLimitError


EXTRACTION_PROMPT = """You are a research extraction agent. From the content below, extract and return ONLY a JSON object with these fields:
- title: page title
- summary: 3-5 sentence summary of the main content
- key_points: list of up to 10 bullet point takeaways
- topics: list of main topics or categories mentioned
- entities: people, companies, products, or places mentioned
- sentiment: one of [positive, neutral, negative]
- data_found: any numbers, statistics, or dates mentioned
- source_url: the URL that was scraped
- scraped_at: current UTC timestamp"""


class ClaudeExtractionError(Exception):
    pass


class MalformedClaudeJSONError(ClaudeExtractionError):
    def __init__(self, message: str, raw_response: str) -> None:
        super().__init__(message)
        self.raw_response = raw_response


class ResearchExtractionAgent:
    def __init__(
        self,
        api_key: str,
        model: str,
        timeout_seconds: float = 60.0,
        max_content_chars: int = 50000,
    ) -> None:
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY is missing. Add it to scraper-agent/.env.")
        self.client = Anthropic(api_key=api_key, timeout=timeout_seconds)
        self.model = model
        self.max_content_chars = max_content_chars

    def extract(self, source_url: str, cleaned_text: str) -> Dict[str, Any]:
        scraped_at = datetime.now(timezone.utc).isoformat()
        trimmed_text = cleaned_text[: self.max_content_chars]
        user_message = (
            f"{EXTRACTION_PROMPT}\n\n"
            f"source_url: {source_url}\n"
            f"scraped_at: {scraped_at}\n\n"
            f"CONTENT:\n{trimmed_text}"
        )

        raw_response = self._call_claude_with_retries(user_message)
        data = self._parse_json(raw_response)
        return self._normalize_result(data, source_url, scraped_at)

    def _call_claude_with_retries(self, user_message: str) -> str:
        retryable_errors = (RateLimitError, APITimeoutError, APIConnectionError)

        for attempt in range(1, 4):
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=1800,
                    temperature=0,
                    messages=[{"role": "user", "content": user_message}],
                )
                return "".join(
                    block.text for block in response.content if getattr(block, "type", "") == "text"
                ).strip()
            except retryable_errors as exc:
                if attempt == 3:
                    raise ClaudeExtractionError(f"Claude API failed after 3 attempts: {exc}") from exc
                wait_seconds = 2 ** attempt
                logging.warning("Claude retryable error on attempt %s. Waiting %ss: %s", attempt, wait_seconds, exc)
                time.sleep(wait_seconds)
            except APIStatusError as exc:
                if exc.status_code in {429, 500, 502, 503, 504} and attempt < 3:
                    wait_seconds = 2 ** attempt
                    logging.warning("Claude status %s on attempt %s. Waiting %ss", exc.status_code, attempt, wait_seconds)
                    time.sleep(wait_seconds)
                    continue
                raise ClaudeExtractionError(f"Claude API status error: {exc}") from exc

        raise ClaudeExtractionError("Claude API failed unexpectedly.")

    def _parse_json(self, raw_response: str) -> Dict[str, Any]:
        try:
            data = json.loads(raw_response)
        except json.JSONDecodeError as exc:
            logging.error("Malformed Claude JSON response: %s", raw_response)
            raise MalformedClaudeJSONError("Claude returned malformed JSON.", raw_response) from exc

        if not isinstance(data, dict):
            raise MalformedClaudeJSONError("Claude JSON response was not an object.", raw_response)
        return data

    def _normalize_result(self, data: Dict[str, Any], source_url: str, scraped_at: str) -> Dict[str, Any]:
        return {
            "title": str(data.get("title", "")).strip(),
            "summary": str(data.get("summary", "")).strip(),
            "key_points": self._as_list(data.get("key_points"))[:10],
            "topics": self._as_list(data.get("topics")),
            "entities": self._as_list(data.get("entities")),
            "sentiment": self._normalize_sentiment(data.get("sentiment")),
            "data_found": self._as_list(data.get("data_found")),
            "source_url": str(data.get("source_url") or source_url).strip(),
            "scraped_at": str(data.get("scraped_at") or scraped_at).strip(),
        }

    def _as_list(self, value: Any) -> list:
        if value is None:
            return []
        if isinstance(value, list):
            return [str(item).strip() for item in value if str(item).strip()]
        if isinstance(value, str) and value.strip():
            return [value.strip()]
        return []

    def _normalize_sentiment(self, value: Any) -> str:
        sentiment = str(value or "neutral").strip().lower()
        return sentiment if sentiment in {"positive", "neutral", "negative"} else "neutral"
