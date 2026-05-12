import logging
import time
from pathlib import Path
from queue import Queue
from typing import List

from agent import ClaudeExtractionError, MalformedClaudeJSONError, ResearchExtractionAgent
from config import load_settings
from scheduler import run_with_optional_schedule
from scraper import BlockedBySiteError, NetworkFetchError, PageNotFoundError, fetch_page
from storage import ResultStorage


def load_urls(urls_path: Path) -> List[str]:
    if not urls_path.exists():
        raise FileNotFoundError(f"Missing urls.txt file at {urls_path}")

    urls = []
    for line in urls_path.read_text(encoding="utf-8").splitlines():
        cleaned = line.strip()
        if cleaned and not cleaned.startswith("#"):
            urls.append(cleaned)
    return urls


def run_agent_once() -> None:
    settings = load_settings()
    storage = ResultStorage(settings.database_path, settings.results_json_path)
    extraction_agent = ResearchExtractionAgent(
        api_key=settings.anthropic_api_key,
        model=settings.claude_model,
        timeout_seconds=settings.claude_timeout_seconds,
        max_content_chars=settings.max_content_chars,
    )

    urls = load_urls(settings.urls_path)
    url_queue: Queue[str] = Queue()
    for url in urls:
        url_queue.put(url)

    total = len(urls)
    success_count = 0
    fail_count = 0

    print(f"\nAI Scraper Agent started. URLs queued: {total}\n")

    while not url_queue.empty():
        url = url_queue.get()
        print(f"[START] {url}")

        try:
            page = fetch_page(url)
            if not page.text:
                raise NetworkFetchError("Fetched page had no readable text.")

            result = extraction_agent.extract(url, page.text)
            storage.save_result(result)

            success_count += 1
            print(f"[OK] {url}")
            print(f"     Title: {result.get('title', 'No title')}")
            print(f"     Method: {page.fetch_method}")
        except PageNotFoundError as exc:
            fail_count += 1
            logging.warning("%s", exc)
            print(f"[SKIP] Page not found: {url}")
        except BlockedBySiteError as exc:
            fail_count += 1
            logging.warning("%s", exc)
            print(f"[SKIP] Blocked or CAPTCHA detected: {url}")
        except MalformedClaudeJSONError as exc:
            fail_count += 1
            logging.error("Skipping malformed Claude response for %s: %s", url, exc.raw_response)
            print(f"[SKIP] Claude returned malformed JSON: {url}")
        except ClaudeExtractionError as exc:
            fail_count += 1
            logging.error("Claude extraction failed for %s: %s", url, exc)
            print(f"[SKIP] Claude extraction failed: {url}")
        except NetworkFetchError as exc:
            fail_count += 1
            logging.error("Network failed for %s: %s", url, exc)
            print(f"[SKIP] Network failed after retries: {url}")
        except Exception as exc:
            fail_count += 1
            logging.exception("Unexpected error for %s", url)
            print(f"[SKIP] Unexpected error: {url} ({exc})")

        if not url_queue.empty() and settings.request_delay_seconds > 0:
            time.sleep(settings.request_delay_seconds)

    print("\nRun complete.")
    print(f"Total scraped: {total}")
    print(f"Success count: {success_count}")
    print(f"Fail count: {fail_count}\n")


def main() -> None:
    settings = load_settings()
    run_with_optional_schedule(
        run_once=run_agent_once,
        schedule_enabled=settings.schedule_enabled,
        schedule_hours=settings.schedule_hours,
    )


if __name__ == "__main__":
    main()
