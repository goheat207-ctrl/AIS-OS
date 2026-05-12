---
title: Trading Context
type: topic
tags: [trading, small-cap, thinkorswim, backtesting]
source_count: 2
created: 2026-05-11
updated: 2026-05-11
---

# Trading Context

[[blaine]] trades small cap stocks using thinkorswim (TD Ameritrade). This is the primary activity right now. All the tools being built exist to solve problems he ran into as a beginner.

## The core problem

Beginner traders get destroyed by three things:
- Losses that are too large per trade (no hard system)
- No way to review what worked and why
- No reliable scanner filters to find actual setups

The tools being built fix all three.

## Current setup

- Platform: thinkorswim / TD Ameritrade
- Style: small cap momentum and catalyst plays
- Primary pain: per-trade losses too large — target is 0.25–0.33% (see [[q2_goals]])

## What's being built

1. **Trade Journal / backtest prototype** — log trades, tag setups, review performance
2. **TOS strategy backtester** — test Thinkscript strategies against historical data
3. **Dilution Tracker** — flag stocks with dilution risk (critical for small caps)
4. **Learning System** — embedded in the backtester so reviews teach, not just record
5. **Watchlist scan filters** — Thinkscript scans that produce actually tradeable tickers

## Why small caps

Small caps move faster and farther on catalysts. More accessible for a solo trader with a smaller account. The knowledge gap between beginner and profitable is also narrower — good tools close it faster.

## Future product angle

Eventually selling tools and dashboards to other beginner traders — people who are where [[blaine]] was when he started. See [[q2_goals]] for current timeline.
