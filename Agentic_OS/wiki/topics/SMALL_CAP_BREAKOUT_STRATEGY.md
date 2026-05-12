---
title: Small Cap Breakout Strategy
type: topic
tags: [trading, strategy, breakout, small_cap]
source_count: 1
created: 2026-05-12
updated: 2026-05-12
---

# ðŸ”¥ SMALL CAP BREAKOUT STRATEGY
**Version:** 1.0 | **Author:** Grant | **Type:** Long-Only Momentum  
**Tags:** #strategy #breakout #small-cap #long-only  
**Vault:** `D:\Project Syndicate Strategy\06_System\Playbooks\SMALL_CAP_BREAKOUT_STRATEGY.md`

---

## ðŸ“Œ STRATEGY OVERVIEW

> [!info] Core Premise
> Exploit short-term supply/demand imbalances created by catalysts + volume expansion in low/mid float small-caps. Trade only the **highest-probability structural breakouts** â€” ranked by a 3-tier priority system. Assume most breakouts fail. Enter only when volume, structure, and catalyst all confirm simultaneously.

### System Pillars

| Pillar | Rule |
|--------|------|
| **Market Cap** | < $2B only |
| **Direction** | Long-only |
| **Primary Edge** | Supply exhaustion + catalyst demand surge |
| **Volume Filter** | RVOL â‰¥ 3x minimum at entry |
| **Dilution Filter** | SAFE or RISK tier only â€” no HIGH RISK longs |
| **Regime Gate** | Regime must be HOT (DC 7-10) or NEUTRAL (DC 4-6) |
| **Max Loss Per Trade** | 1R hard stop â€” no widening, ever |
| **Position Build** | Probe â†’ Confirm â†’ Full (40/35/25%) |

---

## ðŸ† SETUP PRIORITY RANKING

Three setups. One priority order. Execute in this rank â€” A before B, B before C.

```
PRIORITY 1 â†’ Day 3 Liquidity Trap (D3LT)
PRIORITY 2 â†’ Opening Range Breakout + VWAP Reclaim (ORB/VWAP)
PRIORITY 3 â†’ Multi-Day Catalyst Continuation (MDCC)
```

> [!warning] Capital Allocation Rule
> Never hold all three simultaneously at full size. In NEUTRAL regime, trade P1 only unless P2 confirms independently.

---

## ðŸ¥‡ PRIORITY 1 â€” Day 3 Liquidity Trap (D3LT)

### Setup Definition

A 3-day sequence where Day 1 creates the catalyst move, Day 2 traps remaining shorts on low volume, and Day 3 triggers the squeeze/breakout above the accumulation range.

### Why It Works (Mechanism)

Day 2 is a **supply exhaustion trap**: volume dries up, shorts feel safe, longs are shaken out. All remaining shares consolidate in strong hands. Day 3 entry creates a **liquidity vacuum** â€” there are almost no sellers between Day 2 high and Day 1 high. Short covering + new buyers = explosive move.

---

### D3LT â€” Day-by-Day Structure

| Day | Required | What It Means |
|-----|----------|---------------|
| **Day 1** | Catalyst + gap/surge + RVOL â‰¥ 5x + closes in top 40% of range | Demand event confirmed |
| **Day 2** | Inside day OR low-volume consolidation â‰¤ Day 1 range + RVOL < 1.5x + NO new lows below Day 1 low | Supply exhaustion confirmed â€” shorts feel safe |
| **Day 3** | Break above Day 2 high on RVOL â‰¥ 3x within first 30 min | Liquidity trap triggered |

> [!warning] Disqualifiers (ANY one = NO TRADE)
> - Day 2 closes below Day 1 low (structure broken)
> - Day 2 RVOL > 2x (no dry-up = no trap)
> - Dilution = HIGH RISK
> - Active ATM / S-3 filed within 90 days
> - Day 3 break happens on RVOL < 3x (fake)

---

### D3LT â€” Entry Execution

**Stage 1 â€” Probe (40% of planned size)**
- Trigger: Price breaks above Day 2 high on intraday candle
- Condition: RVOL beginning to expand, not yet 3x
- Stop: 2â€“3 cents below Day 2 high OR low of the 5-min breakout candle

**Stage 2 â€” Confirmation (35% additional)**
- Trigger: Price holds above Day 2 high for 1+ full candle AND RVOL â‰¥ 3x
- Condition: Stage 1 is at breakeven or better
- If Stage 1 shows loss: EXIT Stage 1 â€” do NOT add

**Stage 3 â€” Full (remaining 25%)**
- Trigger: Price takes out Day 1 high on volume
- Condition: Stage 1 + 2 combined is in profit
- This is the squeeze leg â€” captures the liquidity vacuum above Day 1 high

---

### D3LT â€” Exit Rules

| Condition | Action |
|-----------|--------|
| +1.5R | Remove 25â€“30% of position, move stop to breakeven |
| +2R | Remove additional 25%, trail stop to +0.5R |
| +3R+ | Hold remaining 50% with structure-based trail |
| Price fails to hold Day 2 high after entry | Exit immediately â€” trap failed |
| Price reclaims Day 1 high then reverses on high vol | Exit 50%, trail tight |
| Volume surges on down candle with no news | Exit â€” distribution signal |

**Trail Method:** Prior 5-min bar low after momentum established. Switch to prior 2-min bar low during squeeze acceleration.

---

### D3LT â€” Stop Placement

```
Hard Stop = 2-3 cents below Day 2 high
            OR
            Low of the 5-min candle that broke Day 2 high
            (whichever is TIGHTER)
```

> [!danger] Anti-Widening Rule
> Stop is NEVER widened after entry. If hit = thesis dead. Exit. No hope trades.

---

### D3LT â€” Failure Scenarios

| Failure Mode | Signal | Response |
|--------------|--------|----------|
| Fake Day 3 break | Price tags Day 2 high, volume < 3x, immediately reverses | Don't enter (RVOL filter catches this) |
| Dilution during hold | S-3 or ATM activity detected post-entry | EXIT immediately â€” size is irrelevant |
| Market regime collapses intraday | IWM drops >2%, VIX spikes | Tighten to prior 1-min bar low |
| Group breakdown | Same-sector peers reversing hard | Exit â€” leadership rotating |

---

### D3LT â€” Quick Reference Card

```
DAY 1: Catalyst + RVOL â‰¥5x + closes top 40%
DAY 2: Inside/low-vol day + RVOL <1.5x + holds Day 1 low
DAY 3: Break of Day 2 high + RVOL â‰¥3x within 30 min

ENTRY:  Probe at Day 2 high break â†’ Add on confirmation â†’ Full above Day 1 high
STOP:   Below Day 2 high / 5-min breakout candle low
TRAIL:  Prior 5-min bar low â†’ tighten on acceleration
EXIT:   Structure break / distribution signal / group failure
```

---

## ðŸ¥ˆ PRIORITY 2 â€” Opening Range Breakout + VWAP Reclaim (ORB/VWAP)

### Setup Definition

Two sub-setups that share the same confirmation logic: price breaks above the **Opening Range** (first 5 or 15 minutes) OR reclaims **VWAP** after a controlled pullback â€” both confirmed with volume expansion. The VWAP Reclaim is the more reliable of the two in small caps.

### Why It Works (Mechanism)

The Opening Range concentrates the day's initial supply/demand discovery. A break above it on volume means demand has absorbed all early sellers. VWAP reclaim signals that institutional/smart money is defending price â€” the intraday structure has shifted bullish. Both create a clean, definable risk level with a visible fuel source (trapped shorts below, new buyers above).

---

### ORB/VWAP â€” Sub-Setup Definitions

#### Sub-Setup A: Opening Range Breakout (ORB)

| Condition | Requirement |
|-----------|-------------|
| Catalyst present | YES â€” A or B grade minimum |
| ORB timeframe | 5-min ORB (preferred) or 15-min ORB |
| Entry trigger | Price breaks above ORB high on volume |
| RVOL at break | â‰¥ 3x |
| Candle close | Must close ABOVE ORB high (not wick) |
| VWAP relationship | Price at or above VWAP at break |
| General market | SPY/QQQ not in acute sell-off |

**Avoid ORB when:**
- Price gaps up >15% pre-market and is already extended (parabolic risk)
- No individual catalyst â€” pure sympathy/sector
- VWAP is far below price (wide stop = bad R:R)

#### Sub-Setup B: VWAP Reclaim

| Condition | Requirement |
|-----------|-------------|
| Prior context | Stock had initial move, pulled back to VWAP or below |
| Reclaim trigger | Price crosses VWAP from below with expanding volume |
| RVOL at reclaim | â‰¥ 2.5x |
| Hold requirement | Price must hold ABOVE VWAP for 2+ consecutive candles |
| Rejection test | Watch for 1 failed VWAP reclaim first â€” second reclaim is higher conviction |
| General market | SPY/QQQ holding above their VWAP |

**Best VWAP Reclaim Context:**
- Stock opened strong, flushed to shake weak hands, reclaims VWAP â†’ continuation
- Stock had PM catalyst, dipped off open, holds PM low, then reclaims VWAP â†’ second leg

---

### ORB/VWAP â€” Entry Execution

**Stage 1 â€” Probe (40%)**
- Trigger: First close above ORB high (ORB) OR first 2-candle hold above VWAP (VWAP)
- Stop: Below breakout candle low or below VWAP (2â€“3 cents)

**Stage 2 â€” Confirmation (35%)**
- Trigger: Volume surge (highest bar of morning) confirms the move, price holds level
- Condition: Stage 1 at breakeven or better

**Stage 3 â€” Full (25%)**
- Trigger: Price takes out HOD or pre-market high on continuation
- Condition: Clear momentum â€” not a slow grind

---

### ORB/VWAP â€” Exit Rules

| Condition | Action |
|-----------|--------|
| +1R | Take 25% off, move stop to breakeven |
| +2R | Take additional 25%, trail to prior bar low |
| Price closes below VWAP after reclaim | Exit â€” reclaim failed |
| Price breaks back into ORB range | Exit â€” false breakout confirmed |
| Volume dries up at prior HOD | Take partial, trail tight |
| Market TICK goes deeply negative (-800+) | Tighten stops, prepare exit |

**Trail Method:** 2-min bar trailing stop while in momentum. Switch to 5-min bar trail after full position confirmed.

---

### ORB/VWAP â€” Stop Placement

```
ORB Stop:        2-3 cents below the ORB high (which is now support)
                 OR low of the breakout candle (tighter)

VWAP Stop:       2-3 cents below VWAP at entry
                 Absolute max: prior day low or opening range low
```

---

### ORB/VWAP â€” Failure Scenarios

| Failure Mode | Signal | Response |
|--------------|--------|----------|
| False ORB break | Breaks ORB, immediately reverses, closes back inside range | Hard stop triggered â€” no rebid unless it re-establishes cleanly |
| VWAP chop | Multiple VWAP crosses with no conviction | No entry â€” reduce to watch-only |
| Volume doesn't confirm | Price reaches ORB high but RVOL stays flat | No entry â€” volume law violated |
| Opening drive reversal | Market turns, stock follows hard | Exit before stop â€” don't wait when market reverses your sector |

---

### ORB/VWAP â€” Quick Reference Card

```
ORB:      Catalyst + close above 5-min ORB high + RVOL â‰¥3x + VWAP â‰¥ price
VWAP:     Pull back â†’ hold support â†’ cross VWAP â†’ hold 2 candles + RVOL â‰¥2.5x

ENTRY:    Probe at trigger â†’ Add on vol confirmation â†’ Full on HOD break
STOP:     Below ORB high / Below VWAP (2-3 cents)
TRAIL:    2-min bar low â†’ 5-min bar low after momentum
EXIT:     Close below VWAP / Return inside ORB / Vol dries at HOD
```

---

## ðŸ¥‰ PRIORITY 3 â€” Multi-Day Catalyst Continuation (MDCC)

### Setup Definition

A stock with a legitimate catalyst that is building a multi-day trend â€” each day adding structure, holding gains, and expanding participation. The entry is at the second or third pivot point, not the first-day gap. This is the "big swing" setup â€” requires the most patience and has the highest R potential.

### Why It Works (Mechanism)

Catalysts that genuinely change the narrative for a small-cap (FDA, contract, sector re-rating) take multiple days to fully attract new buyers and force short covering. Day 1 is chaos. Day 2-3 is when institutional accumulation and informed buying consolidate above the catalyst level. A controlled pullback on Day 2-3 that holds structure = supply being absorbed = the next leg is fuel-loaded.

---

### MDCC â€” Multi-Day Structure Requirements

| Day | Structure |
|-----|-----------|
| **Day 1** | Catalyst + large move + close in top 25% of day's range + RVOL â‰¥ 5x |
| **Day 2** | Holds above Day 1 close (or 50% of Day 1 range) + volume declines (consolidation) |
| **Day 3+** | Higher low forms + sector peers participating + breakout above prior day high |

> [!info] The "Sitting Tight" Test
> If you must check every 5 minutes to feel comfortable, the position is too big or the structure is wrong. In a valid MDCC, the daily chart tells you the trade is still on. Use the daily close â€” not the intraday tape â€” as primary management.

---

### MDCC â€” Continuation Entry Types

**Type 1 â€” Second-Day Breakout**
- Trigger: Day 2 opens and breaks above Day 1 high in first 30 minutes
- Condition: Volume expanding, RVOL â‰¥ 2.5x, market not in sell-off
- Stop: Below Day 2 opening range low or below Day 1 high

**Type 2 â€” Pullback-to-Structure Entry**
- Trigger: Stock pulls back Day 2 or Day 3 to key level (VWAP, 9 EMA, prior day close) on declining volume, then bounces
- Condition: Bounce on expanding volume confirms the level = new support
- Stop: Below the pullback low / below the structural level tested

**Type 3 â€” Continuation Breakout (Day 3+)**
- Trigger: Break above prior day high on Day 3+ with RVOL â‰¥ 3x
- Condition: Group peers also participating (confirms leadership, not isolation)
- Stop: Below prior day low

---

### MDCC â€” Position Management (Multi-Day)

| Situation | Action |
|-----------|--------|
| Price pulls back 5â€“10% within trend | HOLD â€” normal reaction |
| Price closes below prior consolidation low | REDUCE or EXIT â€” structure broken |
| Volume surges on red day with no news | WARNING â€” investigate dilution |
| Sector peers begin breaking down | TIGHTEN stop â€” leadership rotating |
| Good news but price won't advance | EXIT â€” distribution confirmed |
| New high on expanding volume | HOLD, consider adding |

**Overnight Hold Gate (6/8 minimum):**
- [ ] Close in top 25% of day's range
- [ ] Closed above VWAP
- [ ] RVOL > 2x vs 20-day avg
- [ ] Dilution = SAFE or RISK (not HIGH RISK)
- [ ] Daily chart above rising 10/20 SMA
- [ ] Sector/theme strength confirmed
- [ ] No earnings/event risk overnight
- [ ] Float < 50M, overhead resistance clean

---

### MDCC â€” Exit Rules

| Trigger | Action |
|---------|--------|
| Distribution signal (high vol, no progress) | Exit full |
| Sector peer breakdown (2+ peers fail) | Exit or reduce to 50% |
| Price closes below prior day low | Exit |
| ATM / S-3 activity confirmed | Exit immediately |
| +5R or more in the trade | Trail aggressively, protect majority |

**Core Hold Rule:** Hold minimum 25% of position as a "runner" as long as the daily structure is intact. Exit runners only when the daily trend breaks â€” not when the stock has a bad intraday session.

---

### MDCC â€” Quick Reference Card

```
STRUCTURE:  Day 1 catalyst â†’ Day 2 consolidation holds â†’ Day 3+ continuation
ENTRIES:    Second-day breakout / Pullback-to-structure / Day 3+ HOD break
STOP:       Below structural level specific to entry type
HOLD GATE:  6/8 overnight checklist before holding past 4 PM
EXIT:       Distribution / peer breakdown / ATM / structure break
RUNNER:     Keep 25% until daily trend breaks
```

---

## ðŸ” PRE-TRADE CHECKLIST (All Setups)

Run this before ANY entry. 8 questions. If â‰¥2 are NO â†’ pass or wait.

```
[ ] 1. Is there a real, specific catalyst (A or B grade)?
[ ] 2. Is RVOL genuinely elevated (â‰¥3x for P1/P2, â‰¥2.5x for P3)?
[ ] 3. Is dilution status SAFE or RISK (not HIGH RISK)?
[ ] 4. Is the daily chart not broken â€” near highs, no massive overhead?
[ ] 5. Is this the leading stock in its category today (not a laggard)?
[ ] 6. Is the general market (SPY/QQQ/IWM) not in acute sell-off?
[ ] 7. Can I define exactly where I am WRONG (stop level)?
[ ] 8. Am I NOT in recovery mode from a recent loss?
```

> [!danger] Hard Disqualifiers â€” ANY ONE = NO TRADE
> - Active ATM agreement (within 90 days)
> - S-3 filed and effective with significant shares remaining
> - Insider selling >5% of position in past 30 days
> - Shares outstanding increased >10% in past 90 days
> - Dilution tier = HIGH RISK
> - VIX > 35 (Regime 4 / Chaotic)

---

## ðŸ“Š CATALYST GRADING SYSTEM

| Grade | Type | Multi-Day Potential |
|-------|------|---------------------|
| **A** | FDA approval, Phase 3 data, major contract win, acquisition | High |
| **B** | Phase 2 data, partnership with major co., gov contract, earnings beat | Medium-High |
| **C** | Vague PR, MOU, LOI, licensing without financials | Low â€” scalp only |
| **D** | Press release rehash, no new info | NO TRADE |
| **F** | No catalyst â€” pure momentum/sympathy | NO TRADE |

> [!info] Catalyst + Float Rule
> A-grade catalyst + float <10M = maximum squeeze potential (D3LT priority)
> B-grade catalyst + float 10â€“50M = ORB/VWAP and MDCC valid
> C-grade catalyst = P2 scalp only, no multi-day hold

---

## ðŸŽ¯ POSITION SIZING MATRIX

### Base Risk = 0.75%â€“1.25% of account equity per trade

**Regime Multiplier:**

| Regime | Condition | Size Multiplier |
|--------|-----------|----------------|
| HOT (DC 7-10) | Risk-On, multiple setups working | 1.0xâ€“1.25x |
| NEUTRAL (DC 4-6) | Mixed, selective | 0.75x |
| COLD (DC 0-3) | Bearish, limited participation | 0.5x |
| CHAOTIC | VIX > 35 | 0x â€” no new positions |

**Setup Quality Multiplier:**

| Stars | Criteria | Multiplier |
|-------|----------|-----------|
| A+ (5 stars) | All 8 pre-trade checks pass + top catalyst + clean float | 1.0x |
| A (4 stars) | 7/8 checks pass | 0.75x |
| B (3 stars) | 6/8 checks pass | 0.5x |
| < 3 stars | Multiple gaps in criteria | NO TRADE |

**Combined Example:**
- HOT regime (1.0x) Ã— A+ setup (1.0x) Ã— 1.0% base = **1.0% risk**
- NEUTRAL regime (0.75x) Ã— A setup (0.75x) Ã— 1.0% base = **0.56% risk**

---

## âš ï¸ RISK MANAGEMENT ARCHITECTURE

### Portfolio Heat Limits

| Portfolio Heat | Action |
|---------------|--------|
| 0â€“3% | Normal operations |
| 3â€“4% | Review all open positions; no new full-size entries |
| 4â€“6% | Maximum â€” no new positions; manage existing only |
| > 6% | Reduce all positions 50%; investigate cause |

### Drawdown Throttle

| Equity Drawdown | Action |
|-----------------|--------|
| -3% | Review trades; identify patterns |
| -6% | Reduce all new position sizes 50%; pause new entries 1 day |
| -8% | Size down to 25%; trade review required |
| -10%+ | Hard stop â€” no new positions; full system review |

### The Universal Stop Rules

1. Stop is placed BEFORE entry â€” no exceptions
2. Stop is NEVER widened after entry
3. Stop placement = thesis death level (where the setup is proven wrong)
4. Time stops: If ORB/VWAP setup doesn't work within 15 minutes â†’ exit regardless of price

---

## ðŸ”„ SETUP SELECTION DECISION TREE

```
MORNING SCAN COMPLETE
       â†“
Is there a catalyst (A or B grade)?
  NO â†’ No trade today (or wait for news)
  YES â†“
Is this Day 3 with Day 1-2 structure intact?
  YES â†’ Evaluate D3LT (Priority 1 first)
  NO  â†“
Is it the open window (9:30â€“10:15)?
  YES â†’ Evaluate ORB setup (Priority 2)
  NO  â†“
Is the stock post-pullback holding structure?
  YES â†’ Evaluate VWAP Reclaim (Priority 2)
  NO  â†“
Is this Day 2+ of a confirmed multi-day trend?
  YES â†’ Evaluate MDCC entry type (Priority 3)
  NO  â†’ NO TRADE â€” wait for next setup to develop
```

---

## ðŸ§  DAILY EXECUTION ROUTINE (Strategy Integration)

### Pre-Market (5:00â€“9:30 AM)

- [ ] Run regime check (VIX, IWM, SPY, QQQ trend)
- [ ] Scan top gainers sorted by RVOL in sector
- [ ] Identify catalyst grade for each candidate
- [ ] Check dilution tier (EDGAR â€” S-3, ATM, Form 4)
- [ ] Classify each name: D3LT candidate / ORB candidate / MDCC candidate / no trade
- [ ] Mark pivot levels for each: Day 2 high, ORB range, prior HOD
- [ ] Write trade plan with exact entry, stop, and T1/T2 before open

### Open (9:30â€“11:00 AM)

- [ ] Priority 1 (D3LT): Watch for Day 2 high break with RVOL â‰¥ 3x
- [ ] Priority 2 (ORB): Confirm ORB high break in first 5-15 min on volume
- [ ] Do NOT chase: if RVOL doesn't confirm at trigger â†’ wait or pass
- [ ] Stage 1 probe only on first entry
- [ ] Add Stage 2 only if Stage 1 is working

### Midday (11:00 AMâ€“12:00 PM)

- [ ] No new entries in chop
- [ ] Manage open positions: check distribution signals
- [ ] VWAP reclaim setups valid if stock held morning levels cleanly

### Afternoon (12:00â€“3:30 PM)

- [ ] MDCC continuation entries (Type 2 pullback-to-structure)
- [ ] VWAP reclaim valid if sector theme still active
- [ ] Tighten trailing stops on all open positions
- [ ] Power Hour (3:30â€“4:00): close or run â€” no new entries unless HOD break with volume

### End of Day

- [ ] Run overnight hold gate (6/8 checklist)
- [ ] Assess MDCC candidates for next-day plan
- [ ] Log all trades with execution grade
- [ ] Update setup_expectancy.md with results

---

## ðŸ“‹ ONE-LINE TRADE TEMPLATE

```
TICKER:
SETUP TYPE:        [D3LT / ORB / VWAP Reclaim / MDCC Type 1/2/3]
CATALYST GRADE:    [A / B / C]
FLOAT:             [#M]
DILUTION TIER:     [SAFE / RISK / HIGH RISK]
RVOL AT ENTRY:     [Xx]
ENTRY TRIGGER:     [$X â€” specific condition]
STOP LEVEL:        [$X â€” thesis death]
T1:                [$X â€” first partial]
T2:                [$X â€” trail begins]
REGIME:            [HOT / NEUTRAL / COLD]
STARS:             [X/5]
VERDICT:           [TAKE IT / WAIT / PASS]
```

---

## ðŸš« SYSTEM REJECTION LIST

These concepts were evaluated and rejected for small-cap breakout application:

| Concept | Source | Rejection Reason |
|---------|--------|-----------------|
| Large-cap VWAP continuation (multi-hour) | SMB transcripts | Requires deep liquidity â€” small caps reverse too fast |
| Selling options against positions | General | Outside domain constraint |
| Averaging down into losing breakout | Any | Violates anti-averaging rule |
| Trading laggards in hot sectors | Livermore (inverse) | Laggard = hidden supply/dilution â€” disqualified per Laggard Rule |
| Breakouts on RVOL < 2x | All sources | Volume law: unconfirmed price = fake signal |
| Trading for recovery after loss | Psychology module | Recovery trading = emotional override of system |
| Holding past distribution signals "hoping" | Livermore | Hope is a liability â€” structure-based exits only |

---

## ðŸ”— LINKED SYSTEM FILES

- `06_System/Playbooks/SMALL_CAP_BREAKOUT_STRATEGY` â† this file
- `06_System/Edge Stats/setup_expectancy`
- `06_System/Regime Backbone/YYYY-MM-DD_regime`
- `06_System/Patterns Library/D3LT_pattern`
- `06_System/Patterns Library/ORB_VWAP_pattern`
- `06_System/Patterns Library/MDCC_pattern`
- `_Templates/trade_plan_template`
- `_Templates/pre_trade_checklist`

---

*Last Updated: 2026-04-26 | Next Review: Weekly /upgrade cycle*


