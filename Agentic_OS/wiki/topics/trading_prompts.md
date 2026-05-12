---
title: "Trading Prompts — AI-Assisted Analysis and Automation"
type: topic
tags: [prompts, trading-automation, stock-analysis, backtesting, journal-analysis]
source_count: 2
created: 2026-05-11
updated: 2026-05-11
---

## What This Is

A curated set of LLM prompts for trading workflows — sourced from X (Twitter) posts. Organized by function. The best ones are already implemented in [[blaine-os]] or map directly to [[q2_goals]].

**Warning from the community:** prompts without outcome tracking = confirmation bias. Always tie outputs to real trade data. See [[trading_context]].

---

## Tier 1 — Already in the OS

These are implemented or directly matched to existing agents/tools.

**News-to-Trade Converter** *(maps to `small-cap-catalyst` agent)*
> "Summarize the most recent news related to [company/sector] and convert it into actionable trading insights. Outline the potential short-term and long-term impact, expected price movement range, and suggested positioning."

**Trading Journal Analyzer** *(maps to `trade-pattern-analyst` agent)*
> "Analyze my last 20 trades: [trades with entry, exit, and results]. Identify recurring errors, missed opportunities, and behavioral biases. Then provide 3 personalized rules to improve consistency immediately."

**Fully Automated Daily Trade Plan** *(daily plan skill in [[blaine-os]])*
> "Create a structured daily trading plan for [market/asset]. Include a pre-market scan, opening execution strategy, midday adjustments, and closing approach. Present the plan as a time-stamped checklist I can follow step by step."

---

## Tier 2 — Run Manually Now

These work today as one-off prompts pasted into Claude directly.

**Strategy Backtester** *(Q2 goal — TOS backtester build)*
> "Backtest the [trading strategy, e.g., moving average crossover, RSI divergence] on [stock/index] over the past [time period]. Report the win rate, profit factor, maximum drawdown, and suggest potential improvements to enhance performance."

Can also run via [[fincept_tools]] backtesting module for deeper results.

**Technical Structure Evaluation** *(fallback when fincept technicals unavailable)*
> "Analyze the recent price chart of [stock]. Identify trend direction, support and resistance zones, momentum signals, and possible breakout or breakdown areas. Price data: [paste]."

**Full Stock Breakdown** *(pre-trade research on new tickers)*
> "Act as a senior equity research analyst. Analyze the stock [ticker] and provide a structured breakdown including business model, revenue drivers, competitive position, recent financial performance, and major risk factors."

---

## Tier 3 — Reference / Situational

**Complete Stock Analysis** *(what the pre-market brief produces for A-tier setups)*
> "Combine business analysis, financial health, valuation, industry context, risk assessment, and technical structure into a structured investment summary for [stock]."

**Risk Scenario Mapping**
> "List potential downside scenarios for [stock]. Include macroeconomic risks, industry disruption risks, management risks, and financial risks. Estimate how each could impact performance."

**Portfolio Risk Manager**
> "Evaluate my portfolio: [tickers and % allocations]. Identify areas of overexposure, weak positions, and hidden correlations. Recommend risk-adjusted rebalancing and hedging strategies designed to withstand a potential 20% market decline."

---

## Key Principle

> "Most retail investors don't need AI analysis — they need discipline. If you're not backtesting or tracking accuracy over time, you're just getting expensive confirmation bias." — @Agent_Kro_Works

All prompt outputs should be checked against actual trade history in [[trading_context]] — not just narrative.

---

## Sources

- [[src_20260510_ai_trading_prompts_med1]] — 7 equity research prompts (@Med1_Ai)
- [[src_20260510_ai_trading_prompts_shahriar]] — 7 trading automation prompts (@Shahriar661731)

## Links

[[q2_goals]] · [[trading_context]] · [[blaine]] · [[thinkorswim]]
