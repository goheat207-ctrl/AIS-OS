# Connections

Registry of every system your AIOS can reach. Filled by `/onboard` from Q4-Q7 answers; expanded over time as you wire new tools. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
| --- | --- | --- | --- | --- | --- |
| 1 | Revenue / Financials | PayPal + brokerage accounts (thinkorswim/TD) | not yet connected | — | — |
| 2 | Customer interactions | Gmail | not yet connected | — | — |
| 3 | Calendar | Google Calendar (inferred from Gmail) | not yet connected | — | — |
| 4 | Communication | Twitter/X, Facebook, Instagram, Discord | not yet connected | — | — |
| 5 | Project / task tracking | Obsidian Kanban (`TASKS/AIS-OS Board.md`) + markdown task files | local files | — | 2026-05-15 |
| 6 | Meeting intelligence | None yet | not yet connected | — | — |
| 7 | Knowledge / files | Obsidian second brain | local Markdown vault (`Agentic_OS/`) + wiki index (`Agentic_OS/wiki/index.md`) | local files | 2026-05-15 |
| 8 | Trade journal / backtest | TOS Trading Journal API | WebFetch (public REST API at `goheat207.pythonanywhere.com`) | none (public) | 2026-05-11 |
| 9 | Market data | yfinance (Yahoo Finance) | Python script (`fincept_tools/data/yfinance_data.py`) | none (free) | 2026-05-11 |
| 10 | SEC / EDGAR | SEC EDGAR API | Python scripts (`fincept_tools/data/sec_data.py`, `fincept_tools/edgar/`) | none (public) | 2026-05-11 |
| 11 | Technical analysis | compute_technicals (40+ indicators) | Python script (`fincept_tools/technicals/compute_technicals.py`) | none | 2026-05-11 |
| 12 | Backtesting engine | backtestingpy via Fincept bridge | Python scripts (`fincept_tools/backtesting/`) | none | 2026-05-11 |
| 13 | Multi-agent trading analysis | TradingAgents (TauricResearch) | Python package (`TradingAgents/`) via `scripts/run_trading_agents.py` | `ANTHROPIC_API_KEY` (env) | 2026-05-11 |
| 14 | StockTwits sentiment | TradingAgents dataflow | `TradingAgents/tradingagents/dataflows/stocktwits.py` | none (public) | 2026-05-11 |
| 15 | Reddit sentiment | TradingAgents dataflow | `TradingAgents/tradingagents/dataflows/reddit.py` | none (public) | 2026-05-11 |
| 16 | Workflow automation | n8n (local) | n8n instance at `localhost:5678` — starts via `start-n8n.bat` on login | none (local) | 2026-05-15 |
| 17 | Morning brief persistence | brief_writer_server.py | Python HTTP server on `localhost:8765` — receives POST from n8n, writes `logs/morning-brief.json` — starts via `start-brief-writer.bat` on login | none (local) | 2026-05-15 |
| 18 | Nightly task automation | update_tasks.py | Python script at `scripts/update_tasks.py` — registered in Windows Task Scheduler at 10PM daily — updates `TASKS/CURRENT.md`, `TASKS/BACKLOG.md`, `TASKS/COMPLETED.md` | none (local) | 2026-05-15 |

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever.

**n8n workflows currently active:**

| Workflow | Schedule | Input | Output |
|---|---|---|---|
| Morning Journal Pull | 8AM Mon-Fri | `goheat207.pythonanywhere.com/api/metrics` + `/api/per-symbol` | `logs/morning-brief.json` via brief_writer_server |

**Startup services (Windows Startup folder):**

| Service | File | Port/Process | What it does |
|---|---|---|---|
| n8n | `start-n8n.bat` | `localhost:5678` | Workflow automation engine |
| brief_writer_server | `start-brief-writer.bat` | `localhost:8765` | Receives morning brief JSON from n8n, writes to disk |
