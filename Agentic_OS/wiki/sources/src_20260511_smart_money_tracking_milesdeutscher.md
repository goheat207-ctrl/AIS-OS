---
title: "Smart Money Tracking Playbook — @milesdeutscher"
type: source
tags: [research-workflow, insider-tracking, form4, politician-trades, parallel-agents]
source_count: 1
created: 2026-05-11
updated: 2026-05-11
---

Source: https://x.com/milesdeutscher/status/2053855320737472956
Published: 2026-05-11
Author: @milesdeutscher on X

## Summary

Workflow for tracking politician and insider trades using public disclosure data. Parallel agent approach (5 agents simultaneously) feeds into a synthesis step. The tools mentioned (Hermes, OpenClaw) aren't in Blaine's stack, but the workflow maps directly to existing AIOS tools.

## The Workflow

**Requirements in the original:** Hermes agents + OpenClaw
**Blaine's equivalent:** Claude Code agents + fincept_tools EDGAR module + TradingAgents sentiment analyst

**Step 1 — Define research thesis**
Pick what to track: a sector, a politician (e.g., Nancy Pelosi), a specific event type (FDA decisions, defense contracts).

**Step 2 — Run 5 parallel data pulls**
- Agent 1: Politician trades (House/Senate stock disclosures) → SEC EDGAR `forms_insider.py`
- Agent 2: Form 4 filings (CEO/CFO buys and sells) → `sec_data.get_insider_trading()`
- Agent 3: X/social sentiment on top accounts in the space → TradingAgents sentiment analyst
- Agent 4: On-chain data (if applicable — not Blaine's style)
- Agent 5: News, regulatory filings, announcements → TradingAgents news analyst

**Step 3 — Consolidate output** (raw, don't filter yet)

**Step 4 — Synthesize with LLM**
> "Act as an elite macro analyst. Below is raw data gathered from multiple sources on [thesis], including politician disclosures and insider transactions. Synthesize the findings, identify the strongest signals and contradictions, flag any unusual smart-money activity, and give me a clear directional view with conviction levels. Flag any data gaps that need follow-up."

## Key Comment

> "The key point is that this is public-data research, not insider trading. The real edge is workflow speed: tracking disclosures, Form 4s, news, and sentiment continuously, then synthesizing them into cited, auditable outputs." — @Arbwickk

## Relevance to Blaine

- Form 4 tracking is already in `fincept_tools/edgar/forms_insider.py`
- Politician trades aren't a Blaine priority (small-cap momentum focus) but the **parallel agent pattern** is relevant to the `trading-agents-team`
- The synthesis prompt maps to the TradingAgents Research Manager role
- Cost note from comments: heavy parallel agent usage can hit $1K/month — keep runs targeted, not automated

## Links

[[trading_prompts]] · [[trading_agents]] · [[trading_context]]
