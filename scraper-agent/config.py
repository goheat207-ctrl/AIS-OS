import logging
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os


BASE_DIR = Path(__file__).resolve().parent


def _to_bool(value: str, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def _to_int(value: str, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _to_float(value: str, default: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


@dataclass(frozen=True)
class Settings:
    anthropic_api_key: str
    schedule_enabled: bool
    schedule_hours: int
    max_concurrent: int
    request_delay_seconds: float
    log_level: str
    database_path: Path
    results_json_path: Path
    urls_path: Path
    claude_model: str = "claude-sonnet-4-20250514"
    claude_timeout_seconds: float = 60.0
    max_content_chars: int = 50000


def load_settings() -> Settings:
    load_dotenv(BASE_DIR / ".env")

    settings = Settings(
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY", "").strip(),
        schedule_enabled=_to_bool(os.getenv("SCHEDULE_ENABLED"), False),
        schedule_hours=max(1, _to_int(os.getenv("SCHEDULE_HOURS"), 6)),
        max_concurrent=max(1, _to_int(os.getenv("MAX_CONCURRENT"), 1)),
        request_delay_seconds=max(0.0, _to_float(os.getenv("REQUEST_DELAY_SECONDS"), 2.0)),
        log_level=os.getenv("LOG_LEVEL", "INFO").strip().upper(),
        database_path=BASE_DIR / "scraper_results.db",
        results_json_path=BASE_DIR / "results.json",
        urls_path=BASE_DIR / "urls.txt",
    )

    logging.basicConfig(
        level=getattr(logging, settings.log_level, logging.INFO),
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    return settings
