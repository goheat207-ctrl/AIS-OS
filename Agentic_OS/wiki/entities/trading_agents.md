---
title: "TradingAgents — Multi-Agent LLM Trading Framework"
type: entity
tags: [framework, agents, analysis, langgraph, anthropic]
created: 2026-05-11
updated: 2026-05-11
---

## What It Is

TradingAgents (TauricResearch) is an open-source multi-agent trading research framework backed by a research paper (arXiv 2412.20138). It mirrors a real trading firm — analysts, researchers, trader, risk team, portfolio manager — all powered by LLMs via LangGraph.

**Installed at:** `d:\AIS-OS\TradingAgents\`
**Configured for:** Anthropic Claude (`ANTHROPIC_API_KEY` from environment)

---

## The Team

### Analyst Layer
| Agent | What it does |
|---|---|
| Fundamentals Analyst | Balance sheet, income statement, cash flow, company profile |
| News Analyst | Macro headlines + ticker-specific news, catalyst identification |
| Sentiment Analyst | StockTwits (retail), Reddit (r/wsb, r/stocks, r/investing), Yahoo Finance |
| Market Analyst (Technical) | MACD, RSI, moving averages, support/resistance, trend |

### Research Layer
- **Bull Researcher** — strongest case for the trade, with evidence
- **Bear Researcher** — strongest case against the trade, with evidence
- Both debate from the analyst reports. More rounds = sharper conclusion.

### Decision Layer
- **Trader** — converts research plan to BUY/HOLD/SELL proposal
- **Risk Team (3)** — conservative / neutral / aggressive risk perspectives
- **Portfolio Manager** — final approval or rejection

---

## How to Run

**One-shot script (from d:\AIS-OS):**
```bash
python scripts/run_trading_agents.py TICKER YYYY-MM-DD
```

**Interactive CLI (from TradingAgents dir):**
```bash
cd d:\AIS-OS\TradingAgents
python -m cli.main
```

**In Python:**
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "anthropic"
config["deep_think_llm"] = "claude-sonnet-4-6"
config["quick_think_llm"] = "claude-haiku-4-5-20251001"

ta = TradingAgentsGraph(debug=True, config=config)
_, decision = ta.propagate("AAPL", "2026-05-11")
```

**Install (one-time):**
```bash
cd d:\AIS-OS\TradingAgents
pip install .
```

---

## Decision Memory

Every completed run is saved to `~/.tradingagents/memory/trading_memory.md`.
On the next run for the same ticker, it injects:
- Prior decisions and their outcome (realized return)
- Alpha vs SPY for each prior run
- A generated reflection paragraph

This creates a compounding learning loop over time.

---

## Data Sources (default — no API key required)

- **yfinance** — stock data, fundamentals, news
- **StockTwits** — retail sentiment by cashtag (public)
- **Reddit** — r/wallstreetbets, r/stocks, r/investing (public)

Optional: Alpha Vantage API key (`ALPHA_VANTAGE_API_KEY`) for more fundamental data.

---

## Relevance to Blaine

- **Pre-trade research** — run full analysis the night before on any A-tier setup
- **Sentiment check** — StockTwits/Reddit retail sentiment catches what catalyst screeners miss
- **Bull/Bear debate** — forces consideration of the other side before entry
- **Q2 connection** — backtesting strategy with quantified analysis + decision memory = learning system
- **Small-cap filter** — Fundamentals Analyst flags float/share structure; News Analyst catches dilution filings

---

## Links

[[trading_context]] · [[q2_goals]] · [[thinkorswim]] · [[trading_prompts]] · [[fincept_tools]]
