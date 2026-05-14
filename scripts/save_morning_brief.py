"""
Called by the n8n Morning Journal Pull workflow.
Saves the formatted brief to logs/morning-brief.json and appends
a one-line entry to logs/morning-brief-history.md.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
LOGS_DIR = ROOT / "logs"
BRIEF_FILE = LOGS_DIR / "morning-brief.json"
HISTORY_FILE = LOGS_DIR / "morning-brief-history.md"

LOGS_DIR.mkdir(exist_ok=True)


def main():
    if len(sys.argv) < 3:
        print("[ERROR] Usage: save_morning_brief.py DATE JSON_DATA")
        sys.exit(1)

    date = sys.argv[1]
    raw = sys.argv[2]

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON: {e}")
        sys.exit(1)

    # Save latest brief (overwrites — always current)
    BRIEF_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

    # Append one line to history log
    metrics = data.get("metrics", {})
    win_rate = metrics.get("win_rate", "?")
    expectancy = metrics.get("expectancy", "?")
    total_pnl = metrics.get("total_pnl", "?")

    if not HISTORY_FILE.exists():
        HISTORY_FILE.write_text(
            "# Morning Brief History\n\n"
            "| Date | Win Rate | Expectancy | Total P&L |\n"
            "|------|----------|------------|----------|\n",
            encoding="utf-8",
        )

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"| {date} | {win_rate} | {expectancy} | {total_pnl} |\n")

    print(f"[OK] Morning brief saved: {BRIEF_FILE}")
    print(f"[OK] History updated: {HISTORY_FILE}")


if __name__ == "__main__":
    main()
