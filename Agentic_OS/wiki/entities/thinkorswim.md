---
title: "thinkorswim (TOS)"
type: entity
tags: [platform, trading, backtesting, broker, td-ameritrade]
created: 2026-05-11
updated: 2026-05-11
---

## What It Is

thinkorswim (TOS) is TD Ameritrade's professional-grade trading platform — desktop and web. Blaine's primary execution and analysis platform. Scripted via **Thinkscript** (proprietary language for scans, strategies, indicators).

---

## Current Role in Blaine's OS

- **Primary execution platform** — all trades entered here
- **Trade data source** — journal data originates from TOS executions, then logged at https://goheat207.pythonanywhere.com
- **Backtesting environment** — Q2 goal is a full working TOS strategy backtester (in Thinkscript)
- **Scanner** — Thinkscript scan filters are part of the Q2 build

---

## Q2 Build Goals

1. **TOS Strategy Backtester** — Thinkscript-based, with Dilution Tracker, Learning System, and working scan filters
2. **Profitable scan filters** — Thinkscript conditions identifying small-cap momentum setups
3. Integration with [[trading_context]] data to validate scanner output against live P&L

See [[q2_goals]] for full priority list and deadlines.

---

## Connections

- Trade journal API: `https://goheat207.pythonanywhere.com` (fetches TOS trade history)
- [[fincept_tools]] backtesting module — Python alternative for strategy validation before coding in Thinkscript
- [[trading_prompts]] — Strategy Backtester prompt maps to this build

---

## Thinkscript Notes

- Proprietary — not Python. Syntax is unique to TOS.
- Backtesting is built into TOS Strategy Tester (separate from On-Demand)
- Scan filters run on TOS scanner — can filter by custom Thinkscript conditions
- No direct API — outputs must be exported manually or captured from journal

---

## Links

[[trading_context]] · [[q2_goals]] · [[blaine]] · [[trading_prompts]] · [[fincept_tools]]
