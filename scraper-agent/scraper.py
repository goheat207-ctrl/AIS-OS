import logging
import re
import time
from dataclasses import dataclass
from typing import Optional

import httpx
from bs4 import BeautifulSoup
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


BLOCKED_PATTERNS = (
    "captcha",
    "cf-challenge",
    "access denied",
    "verify you are human",
    "unusual traffic",
    "blocked",
    "robot check",
)


class ScraperError(Exception):
    pass


class PageNotFoundError(ScraperError):
    pass


class BlockedBySiteError(ScraperError):
    pass


class NetworkFetchError(ScraperError):
    pass


@dataclass
class ScrapedPage:
    url: str
    title: str
    html: str
    text: str
    status_code: Optional[int]
    fetch_method: str


def _looks_blocked(content: str) -> bool:
    lowered = content.lower()
    return any(pattern in lowered for pattern in BLOCKED_PATTERNS)


def clean_html_to_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(
        [
            "script",
            "style",
            "noscript",
            "nav",
            "footer",
            "header",
            "aside",
            "form",
            "iframe",
            "svg",
            "canvas",
        ]
    ):
        tag.decompose()

    for selector in [
        "[class*=ad]",
        "[id*=ad]",
        "[class*=cookie]",
        "[id*=cookie]",
        "[class*=banner]",
        "[id*=banner]",
        "[class*=subscribe]",
        "[id*=subscribe]",
        "[class*=newsletter]",
        "[id*=newsletter]",
    ]:
        for tag in soup.select(selector):
            tag.decompose()

    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    main = soup.find("main") or soup.find("article") or soup.body or soup
    text = main.get_text("\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)

    if title and title not in text[:300]:
        text = f"{title}\n\n{text}"

    return text.strip()


def _title_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    if soup.title:
        return soup.title.get_text(" ", strip=True)
    heading = soup.find(["h1", "h2"])
    return heading.get_text(" ", strip=True) if heading else ""


def _fetch_with_playwright(url: str, timeout_ms: int = 30000) -> ScrapedPage:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            )
        )
        response = None
        try:
            response = page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
            page.wait_for_load_state("networkidle", timeout=10000)
            html = page.content()
        except PlaywrightTimeoutError as exc:
            raise NetworkFetchError(f"Playwright timeout for {url}: {exc}") from exc
        finally:
            browser.close()

    status_code = response.status if response else None
    if status_code == 404:
        raise PageNotFoundError(f"404 page not found: {url}")
    if status_code and status_code >= 400:
        raise NetworkFetchError(f"HTTP {status_code} from Playwright: {url}")
    if _looks_blocked(html):
        raise BlockedBySiteError(f"Site appears to block scraping: {url}")

    return ScrapedPage(
        url=url,
        title=_title_from_html(html),
        html=html,
        text=clean_html_to_text(html),
        status_code=status_code,
        fetch_method="playwright",
    )


def _fetch_with_httpx(url: str, timeout_seconds: float = 30.0) -> ScrapedPage:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    with httpx.Client(timeout=timeout_seconds, follow_redirects=True, headers=headers) as client:
        response = client.get(url)

    if response.status_code == 404:
        raise PageNotFoundError(f"404 page not found: {url}")
    if response.status_code >= 400:
        raise NetworkFetchError(f"HTTP {response.status_code} from httpx: {url}")
    if _looks_blocked(response.text):
        raise BlockedBySiteError(f"Site appears to block scraping: {url}")

    return ScrapedPage(
        url=url,
        title=_title_from_html(response.text),
        html=response.text,
        text=clean_html_to_text(response.text),
        status_code=response.status_code,
        fetch_method="httpx",
    )


def fetch_page(url: str, network_retries: int = 2) -> ScrapedPage:
    last_error: Optional[Exception] = None

    for attempt in range(1, network_retries + 2):
        try:
            return _fetch_with_playwright(url)
        except PageNotFoundError:
            raise
        except BlockedBySiteError:
            raise
        except Exception as exc:
            last_error = exc
            logging.warning("Playwright fetch failed for %s on attempt %s: %s", url, attempt, exc)

        try:
            return _fetch_with_httpx(url)
        except PageNotFoundError:
            raise
        except BlockedBySiteError:
            raise
        except Exception as exc:
            last_error = exc
            logging.warning("httpx fallback failed for %s on attempt %s: %s", url, attempt, exc)

        if attempt <= network_retries:
            time.sleep(2 ** attempt)

    raise NetworkFetchError(f"Network fetch failed after retries for {url}: {last_error}")
