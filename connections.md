# Connections

Registry of every system your AIOS can reach. Filled by `/onboard` from Q4-Q7 answers; expanded over time as you wire new tools. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
| --- | --- | --- | --- | --- | --- |
| 1 | Revenue / Financials | PayPal + brokerage accounts (thinkorswim/TD) | not yet connected | — | — |
| 2 | Customer interactions | Gmail | not yet connected | — | — |
| 3 | Calendar | Google Calendar (inferred from Gmail) | not yet connected | — | — |
| 4 | Communication | Twitter/X, Facebook, Instagram, Discord | not yet connected | — | — |
| 5 | Project / task tracking | None yet | not yet connected | — | — |
| 6 | Meeting intelligence | None yet | not yet connected | — | — |
| 7 | Knowledge / files | Obsidian | not yet connected | — | — |
| 8 | Trade journal / backtest | TOS Trading Journal | WebFetch (public REST API) | none (public) | 2026-05-11 |
| 9 | Market data | yfinance (Yahoo Finance) | Python script (`fincept_tools/data/yfinance_data.py`) | none (free) | 2026-05-11 |
| 10 | SEC / EDGAR | SEC EDGAR API | Python scripts (`fincept_tools/data/sec_data.py`, `fincept_tools/edgar/`) | none (public) | 2026-05-11 |
| 11 | Technical analysis | compute_technicals (40+ indicators) | Python script (`fincept_tools/technicals/compute_technicals.py`) | none | 2026-05-11 |
| 12 | Backtesting engine | backtestingpy via Fincept bridge | Python scripts (`fincept_tools/backtesting/`) | none | 2026-05-11 |
| 13 | Multi-agent trading analysis | TradingAgents (TauricResearch) | Python package (`TradingAgents/`) via `scripts/run_trading_agents.py` | `ANTHROPIC_API_KEY` (env) | 2026-05-11 |
| 14 | StockTwits sentiment | TradingAgents dataflow | `TradingAgents/tradingagents/dataflows/stocktwits.py` | none (public) | 2026-05-11 |
| 15 | Reddit sentiment | TradingAgents dataflow | `TradingAgents/tradingagents/dataflows/reddit.py` | none (public) | 2026-05-11 |

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever.
