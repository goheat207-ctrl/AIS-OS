# Trade Journal API — Reference

**Base URL:** `https://goheat207.pythonanywhere.com`
**Auth:** None (public)
**Repo:** `https://github.com/goheat207-ctrl/backtest_project`
**Local run:** `python server.py` → `http://localhost:5000`

## Endpoints

| Method | Path | Returns |
|---|---|---|
| GET | `/api/health` | Server status, DB path, total trade count |
| GET | `/api/trades` | All trades + annotations. Filters: `symbol`, `date_from`, `date_to`, `strategy`, `mistake_tag` |
| GET | `/api/metrics` | Aggregate stats: win rate, P&L, drawdown, Sharpe, Sortino, streaks, expectancy |
| GET | `/api/equity-curve` | Equity curve data points |
| GET | `/api/symbols` | Sorted list of all traded symbols |
| GET | `/api/per-symbol` | Per-symbol stats (win rate, avg P&L, count per ticker) |
| GET | `/api/goals` | Current goals (set in the dashboard) |
| GET | `/api/strategies` | All strategy labels |
| GET | `/api/mistake-tags` | All mistake tag labels |

## Common queries for Claude sessions

Ask me to pull any of these on demand:

- "Pull my metrics" → `/api/metrics`
- "What symbols am I trading?" → `/api/symbols`
- "Per-symbol breakdown" → `/api/per-symbol`
- "Show my equity curve data" → `/api/equity-curve`
- "Trades for [SYMBOL]" → `/api/trades?symbol=SYMBOL`
- "Trades between dates" → `/api/trades?date_from=YYYY-MM-DD&date_to=YYYY-MM-DD`
- "Filter by strategy" → `/api/trades?strategy=NAME`

## Data notes

- All trades parsed from TOS Account Statement CSV (FIFO round-trip matching)
- SQLite at `/home/goheat207/backtest_project/data/journal.db` on PythonAnywhere
- Annotations, strategies, mistake tags stored in the same DB
- Goals and playbook stored in localStorage (not accessible via API)
