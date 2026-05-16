---
title: "Playbook Library — Small-Cap & Momentum Trader Collection"
type: topic
tags: [playbooks, setups, small-cap, momentum, reference-library]
source_count: 20
created: 2026-05-11
updated: 2026-05-11
---

## What This Is

A collection of 20+ trader playbooks, strategy guides, and books stored in `Agentic_OS/raw/books/`. Most are small-cap and momentum focused. Blaine also has his own playbook in this folder.

**Rule:** Don't read these individually. Use them as a query database — ask Claude to extract specific information from specific files when you need it.

---

## Blaine's Own Playbooks (start here)

| File | What it is |
|---|---|
| `Blaine Grants Small Cap Setups.html` | Blaine's unified small-cap trading operating system |
| `GRANT_MASTER_SMALL_CAP_REFERENCE.txt` | Master small-cap reference doc |
| `GRANT_SWING_SYSTEM_v1.txt` | Blaine's swing system, version 1 |

These are the source of truth for Blaine's own methodology. When building TOS scans or strategies, pull from these first.

---

## Tier 1 — Most Relevant to Blaine's Style (small-cap momentum)

| File | Trader | Known For |
|---|---|---|
| `ross_cameron_playbook.html` + `HowToDayTrade_byRossCameron_2023_DigitalGiftCopy.pdf` | Ross Cameron | Gap-and-go, small-cap momentum, strict risk rules |
| `TIMOTHY_SYKES_PLAYBOOK.txt` | Timothy Sykes | Penny stock patterns, dilution plays, short side |
| `roland_wolf_playbook orig.html` | Roland Wolf | Small-cap setups, Level 2 reading |
| `KELLOGG_SMALLCAP_PLAYBOOK.txt` | Kellogg | Small-cap specific |
| `JadeCap Playbook.pdf` + `JadeCap Playbook-1.pdf` | JadeCap | Institutional small-cap |
| `edu_trades_playbook_report.html` | Edu Trades | Momentum setups |
| `The Ignition System.html` | — | Breakout/ignition methodology |

---

## Tier 2 — Supplemental (momentum + risk)

| File | Trader | Known For |
|---|---|---|
| `Jared Playbook.pdf` | Jared | — |
| `Kyle Williams Playbook.pdf` | Kyle Williams | — |
| `Lance PlayBook.pdf` | Lance | — |
| `Marco Trades Playbook.pdf` | Marco | — |
| `Pradeep Bonde Playbook.pdf` | Pradeep Bonde | Episodic pivots, momentum |
| `Rajan Dhall Playbook.pdf` | Rajan Dhall | — |
| `Real Simple Ariel Playbook.pdf` | Ariel | — |
| `TG Capital Playbook.pdf` | TG Capital | — |
| `The Travelling Trader Playbook.pdf` | Travelling Trader | — |
| `Trader Mayne Playbook.pdf` | Trader Mayne | — |
| `Vincent Desiano Playbook.pdf` | Vincent Desiano | — |
| `Ali Crooks Playbook.pdf` | Ali Crooks | — |
| `CF Scarface Playbook.pdf` | CF Scarface | — |
| `Elite Option Trader Playbook.pdf` | — | Options-focused |
| `Mean reversion LB.txt` | — | Mean reversion strategy |

---

## Tier 3 — Classic / Foundational

| File | What it is |
|---|---|
| `jesse_livermore_playbook.html` | Livermore's tape reading and position sizing principles |
| `minervini_vcp_playbook.html` | Mark Minervini's Volatility Contraction Pattern |

---

## Market Research PDFs (books/data subfolder)

| File | Topic |
|---|---|
| `AI Investment Landscape Bubble or Breakthrough.pdf` | AI sector thesis |
| `JPMorgan Desk Says AI Selling Almost Over.pdf` | Macro signal |
| `The 2026 Market opportunity.pdf` | Market outlook |
| `Trump's Defense Stocks.pdf` | Sector rotation play |
| `Trumps plan to flood the markets.pdf` | Policy/market impact |
| `Why Hasn't The Economy-workbook.pdf` | Economic analysis |

---

## Unknown PDFs (user_18211059_*.pdf)

17 unidentified PDFs. These appear to be downloaded from a learning platform. Need to be identified — ask Claude to read the first few pages of each to classify.

---

## How to Use This Library

**Don't:** try to read and remember all of these yourself.

**Do:** ask Claude targeted questions when you need them:
- "What does Ross Cameron say about the first 5-minute candle?"
- "What are the top 3 exit rules across all my small-cap playbooks?"
- "What does the Ignition System use as an entry trigger?"

**For TOS Backtester build:** start with Blaine's own playbook + Ross Cameron + Kellogg. Extract the specific setup rules and translate to Thinkscript.

**For win rate improvement:** extract exit rules from 3+ playbooks. Find where they agree — that's the rule to adopt first.

---

## Links

[[trading_context]] · [[q2_goals]] · [[thinkorswim]] · [[trading_prompts]] · [[Blaine]]
