# Trading Neuron — Current State of Knowledge

> Load this file when working on any trading task. Ignore all other neurons.

## Who I am as a trader
- Small cap day trader, solo operator
- Focus: momentum, breakouts, tape reading
- Platform: thinkorswim (TD Ameritrade / Schwab)
- Core pain: per-trade losses too high — target 0.25–0.33% per trade

## What I know well
- **Price action (Al Brooks):** bar-by-bar analysis, breakouts, reversals, bull channels, late trend entries, pullback timing
- **Momentum / tape reading:** Level 2, time & sales, reading order flow
- **Candlestick patterns:** Candlestick Trading Bible (Kohan FX) internalized
- **Small cap setups:** gapper identification, pre-market catalyst screening, float/short interest
- **Quadrant system:** 4-quadrant classification (Momentum Trap, Value Trap, Dead Zone, breakout edge); SPS and DRS scoring
- **Exit strategies:** execution discipline, exit conditions, bar-by-bar trade review framework
- **Fundamentals:** liquidity, dilution risk, catalyst types (8-K, FDA, PR)

## Frameworks in use
- Quadrant Trading System — classifies setups by momentum + dilution risk
- SPS (Squeeze Probability Score) — pre-entry scoring
- DRS (Dilution Risk Score) — risk filter
- 3-step entry rules by quadrant

## Active tools
- thinkorswim scanners (ThinkScript watchlist filters — in development)
- TradingAgents multi-agent pipeline (`scripts/run_trading_agents.py`)
- Pre-market scan agent (`.claude/agents/pre-market-scan.md`)
- Small cap catalyst agent (`.claude/agents/small-cap-catalyst.md`)
- Trade pattern analyst agent (`.claude/agents/trade-pattern-analyst.md`)
- Trade journal API (public REST at goheat207.pythonanywhere.com)
- Fincept tools: yfinance, SEC EDGAR, technicals, backtester

## Known gaps
- AI stock picks are unreliable — use AI for research/analysis, NOT for trade calls
- TOS backtester not yet built (Q2 priority)
- Dilution tracker not yet built (Q2 priority)
- ThinkScript scan filters still in development

## Sources ingested
- Al Brooks: multiple transcripts (trends, channels, breakouts, pullbacks, webinars)
- SMB Capital: 5 trading mistakes, exit conditions
- YTC Price Action Trader — Lance Beggs
- Day Trading Momentum Level 2 (2023)
- Warrior Trading: technical analysis
- HTCO catalyst synthesis (2026-05-13)

---
*Last updated: 2026-05-14 | Update this file after each new source ingested into this neuron.*
