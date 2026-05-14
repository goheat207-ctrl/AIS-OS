---
title: Exit Strategies
type: topic
domain: trading
tags: [exits, ATR, RSI, price-action, trailing-stop, expectancy]
relevance: high
source_count: 1
created: 2026-05-13
updated: 2026-05-13
---

# Exit Strategies

How Blaine exits trades. Exits determine profitability more than entries.

> Profitability is determined more by how you exit winners than how you enter trades.

---

## The Core Problem

Most beginner mistakes happen at the exit, not the entry:
- Selling the first green candle (fear-based)
- Holding a winner until it reverses completely (greed-based)
- Exiting on emotion ("I made enough", "I feel nervous")

Professional exits are predefined, objective, and rule-based.

---

## Exit Method 1 — ATR Trailing Stop

**Formula:** `Trailing Stop = HighestHigh(10 candles) − current ATR`

Ask before using: "Is this pullback normal for this stock right now?"
- Yes → stay in trade
- No → exit

**Use when:**
- High RVOL continuation day
- Clean squeeze with strong catalyst
- No obvious dilution ceiling or offering risk

**Avoid when:**
- Choppy micro-floats
- Dilution-heavy names
- No news / newsless squeeze

**Risk:** ATR widens in parabolic moves — stop trails wide, can give back large gains on late reversals.

---

## Exit Method 2 — RSI Exit (Trend Continuation)

**Rule:** Enter when RSI > 60. Exit when RSI < 40.

High RSI does NOT mean overbought. It means aggressive buying pressure is entering.

This is a trend-following system:
- Win rate ~44% (many small losses)
- Profits come from the few large asymmetric winners
- The few winners pay for all the failed attempts

**Small-cap warning:** High RSI can also signal exhaustion, trapped longs, or dilution setup. Validate with catalyst quality and float.

---

## Exit Method 3 — Prior Candle Low (Price Action)

**Rule:** `Exit when current candle closes below prior candle's low`

The cleanest, lowest cognitive load exit:
```
Did candle close below prior low?
  YES → exit
  NO  → hold
```

Strong uptrends should continue making higher lows. When that fails, momentum may be weakening.

**Adapt to market regime:**
- Weak market → 1-minute chart, tighter prior-low rule
- Strong market → 5-minute chart, give more room

---

## Resistance Exit Rule (SMB Capital)

**Data:** First test of resistance holds 68% of the time.

**Rule:** When stock approaches clear resistance (prior high, whole number, VWAP):
- Offer out 50% of position 10 cents before the level
- If it breaks: still hold 50%, can re-add after pullback confirms
- If it rejects: profits locked, no damage done

---

## Momentum Window Exit (SMB Capital)

**Data:** 73% of first-hour >5% runners made HOD before 10:30 AM.

**Rule for first-hour momentum trades:**
- Set a 10:25 AM alarm at entry
- Begin scaling out or exit entirely at 10:25
- No exceptions for the first 30 days of applying this rule

---

## Exit Decision Framework

| Market condition | Exit method |
|------------------|-------------|
| Strong trend, no dilution risk | ATR trailing or prior candle low |
| Approaching resistance | Partial exit 10 cents before the level |
| First-hour momentum trade | Scale by 10:25 AM hard rule |
| RSI continuation system | Exit when RSI < 40 |
| Weak/choppy market | 1-minute prior candle low, tighter |

---

## What Exits Are NOT

- "I feel scared" — emotional, not objective
- "I made enough" — arbitrary, not rule-based
- Waiting for the top — predicting extremes is low probability

> Your job is not to buy the bottom and sell the top. It's to take the middle 70% and get out before the fade starts.

---

## Related Pages

[[how_to_time_exact_entries_and_exits]] · [[breakdown_of_high_probability_entries_and_exits]] · [[trading_context]] · [[execution_discipline]] · [[reading_the_tape_quick]] · [[small_cap_catalyst]]

## Sources

- [[src_20260513_exit_conditions_trading]]
