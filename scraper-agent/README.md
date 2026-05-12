# AI-Powered Web Scraping Agent

This project is a local Python agent that reads URLs from `urls.txt`, scrapes each page, sends cleaned page text to Claude, saves structured results to SQLite, and exports `results.json` after each successful scrape.

## What It Does

- Loads target URLs from `urls.txt`
- Fetches pages with Playwright
- Falls back to `httpx` and BeautifulSoup if Playwright fails
- Cleans page HTML into readable body text
- Uses Claude Sonnet 4 to extract structured research data
- Saves results to `scraper_results.db`
- Exports all saved results to `results.json`
- Can run once or on a schedule with APScheduler

## Setup

Run these commands from this folder:

```powershell
cd d:\AIS-OS\scraper-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Configure

Copy the example environment file:

```powershell
Copy-Item .env.example .env
```

Open `.env` and add your Anthropic API key:

```env
ANTHROPIC_API_KEY=your_real_key_here
SCHEDULE_ENABLED=false
SCHEDULE_HOURS=6
MAX_CONCURRENT=1
REQUEST_DELAY_SECONDS=2
LOG_LEVEL=INFO
```

## Add URLs

Edit `urls.txt` with one URL per line:

```text
https://example.com
https://example.org
https://example.net
```

Blank lines and lines starting with `#` are ignored.

## Run Once

```powershell
python main.py
```

## Run On A Schedule

Set this in `.env`:

```env
SCHEDULE_ENABLED=true
SCHEDULE_HOURS=6
```

Then run:

```powershell
python main.py
```

The agent runs immediately, then repeats every configured number of hours until you stop it with `Ctrl+C`.

## Output Files

After a successful run, the agent creates:

- `scraper_results.db`: local SQLite database
- `results.json`: exported master JSON results

Example `results.json`:

```json
[
  {
    "title": "Example Domain",
    "summary": "This page explains that Example Domain is reserved for illustrative examples in documentation. It tells readers they may use the domain without asking for permission. The page is short and mainly acts as a neutral placeholder.",
    "key_points": [
      "Example Domain is available for documentation examples.",
      "The domain can be used without prior permission.",
      "The page points readers to more information."
    ],
    "topics": [
      "documentation",
      "example domains",
      "internet resources"
    ],
    "entities": [
      "Example Domain",
      "IANA"
    ],
    "sentiment": "neutral",
    "data_found": [
      "No major numbers, statistics, or dates found."
    ],
    "source_url": "https://example.com",
    "scraped_at": "2026-05-12T14:30:00+00:00"
  }
]
```

## Error Handling

The agent handles:

- 404 pages by logging and skipping
- CAPTCHA or blocking pages by logging and skipping
- Claude timeout or rate limits with 3 retries and exponential backoff
- Malformed Claude JSON by logging the raw response and skipping
- Network failures with 2 retries before skipping

## Notes

This scraper is for sites you are allowed to access and scrape. Always respect website terms, robots rules, and rate limits.
