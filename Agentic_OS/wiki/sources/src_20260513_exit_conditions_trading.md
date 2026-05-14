---
title: Exit Conditions in Trading
type: source
domain: trading
tags: [exits, ATR, RSI, price-action, expectancy, trailing-stop]
relevance: high
source_count: 1
created: 2026-05-13
updated: 2026-05-13
---

# Source: Exit Conditions in Trading

**Source:** ChatGPT synthesis of a trading video transcript  
**Clipped:** 2026-05-13  
**Why saved:** Exit strategies for backtesting and P&L improvement

---

## Core Thesis

> Profitability is determined more by how you exit winners than by how you enter trades.

Expectancy = (WinRate × AvgWin) − (LossRate × AvgLoss). This source focuses entirely on maximizing AvgWin.

---

## The 3 Exit Conditions

### 1. ATR Trailing Exit (Volatility-Based)

**Formula:** `ATR Trailing Stop = HighestHigh(10 candles) − current ATR`

- Adapts to actual stock volatility — not arbitrary percentages
- "Is this pullback normal for this stock?" If yes, stay. If no, exit.
- Works best on: high RVOL continuation, clean squeeze, strong catalyst, no dilution ceiling
- Works poorly on: choppy micro-floats, dilution names, low-liquidity traps
- Risk: ATR widens in parabolic moves — can give back large gains on late reversals

### 2. RSI Exit (Trend Continuation)

**Rule:** Enter when RSI > 60. Exit when RSI < 40.

- High RSI = aggressive buying pressure entering (NOT overbought signal)
- Intentionally buys strength, avoids bottom-picking
- Win rate ~44% but produces asymmetric winners — the few big wins pay for many small losses
- Hidden risk in small caps: high RSI can also mean exhaustion, trapped longs, dilution setup

### 3. Price Action Exit (His Favorite — No Indicators)

**Rule:** `Exit when current candle closes below the prior candle's low`

- Very low cognitive load — binary decision
- Naturally lets winners expand through strong trends
- Adapt timeframe and stop width to market regime:
  - Weak market → tighter exits, 1-minute structure
  - Strong market → 5-minute structure, wider trailing

---

## Key Concepts Worth Keeping

| Concept | Application |
|---------|-------------|
| Expectancy > win rate | A 44% win rate system can be profitable |
| Regime-adaptive exits | Widen in strong markets, tighten in weak |
| Objective weakness exits | Predefined rules, not emotional reactions |
| "Room to breathe" | Adapt stop width to current momentum strength |

---

## Small-Cap Warning (Important)

Holding "until weakness" without additional filters is dangerous when:
- Dilution hits mid-run
- Offerings drop
- Halt fails to resume
- Parabolic exhaustion begins
- Volume deteriorates without price follow-through

Exits must ALSO account for catalyst exhaustion, float rotation, offering risk, and failed HOD reclaim — not just indicators.

---

## Related Pages

[[exit_strategies]] · [[how_to_time_exact_entries_and_exits]] · [[trading_context]] · [[breakdown_of_high_probability_entries_and_exits]] · [[small_cap_catalyst]]
