---
title: "7 Prompts to Put Trading on Autopilot — @Shahriar661731"
type: source
tags: [prompts, trading-automation, backtesting, journal-analysis, daily-plan]
source_count: 1
created: 2026-05-11
updated: 2026-05-11
---

Source: https://x.com/Shahriar661731/status/2053521524099875249
Published: 2026-05-10
Author: @Shahriar661731 on X

## Summary

7 trading-focused prompts emphasizing automation and workflow — from idea generation to daily planning. More operationally focused than the Med1 set. Prompts 4, 6, and 7 are directly actionable for Blaine's current build.

## The 7 Prompts

**1. Trade Idea Generator**
> "Analyze today's market and identify 5 high-probability trade opportunities for [stock/index/sector]. For each setup, provide the suggested entry price, profit targets, stop-loss level, and expected risk-to-reward ratio. Also explain the technical and fundamental reasoning."

**2. Automated Technical Analyst**
> "Evaluate [stock/ticker] using both daily and weekly timeframes. Identify key support and resistance zones, trendlines, moving averages, and momentum indicators. Then deliver a clear Buy, Hold, or Sell signal with step-by-step reasoning."

**3. News-to-Trade Converter**
> "Summarize the most recent news related to [company/sector] and convert it into actionable trading insights. Outline the potential short-term and long-term impact, expected price movement range, and suggested positioning."

**4. Strategy Backtester**
> "Backtest the [trading strategy, e.g., moving average crossover, RSI divergence] on [stock/index] over the past [time period]. Report the win rate, profit factor, maximum drawdown, and suggest potential improvements to enhance performance."

**5. Portfolio Risk Manager**
> "Evaluate my portfolio: [tickers and % allocations]. Identify areas of overexposure, weak positions, and hidden correlations. Recommend risk-adjusted rebalancing and hedging strategies designed to withstand a potential 20% market decline."

**6. Trading Journal Analyzer**
> "Analyze my last 20 trades: [trades with entry, exit, and results]. Identify recurring errors, missed opportunities, and behavioral biases. Then provide 3 personalized rules to improve consistency immediately."

**7. Fully Automated Trade Plan**
> "Create a structured daily trading plan for [market/asset]. Include a pre-market scan, opening execution strategy, midday adjustments, and closing approach. Present the plan as a time-stamped checklist I can follow step by step."

## Relevance to Blaine

- **Prompt 3 (News-to-Trade)** — core of the `small-cap-catalyst` agent. Already implemented; this confirms the workflow.
- **Prompt 4 (Strategy Backtester)** — directly maps to Q2 goal (TOS backtester). Can be run manually now using [[fincept_tools]] backtesting module.
- **Prompt 6 (Journal Analyzer)** — the `trade-pattern-analyst` agent does this automatically against the live PythonAnywhere data. Prompt version useful when you want a quick one-off on pasted trades.
- **Prompt 7 (Daily Trade Plan)** — implemented as a skill in [[blaine-os]] dashboard. Produces a time-stamped checklist.

## Links

[[trading_prompts]] · [[q2_goals]] · [[trading_context]] · [[Blaine]]
