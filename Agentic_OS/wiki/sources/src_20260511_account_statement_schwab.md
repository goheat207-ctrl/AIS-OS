---
title: "Schwab Account Statement — Jan 1 through May 11 2026"
type: source
tags: [trade-data, account-statement, schwab, p&l, raw-data]
source_count: 1
created: 2026-05-11
updated: 2026-05-11
---

Source: `Agentic_OS/raw/data/2026-05-11-AccountStatement.csv`
Account: 13660337SCHW (Individual)
Period: 2026-01-01 through 2026-05-11

## What's In It

Raw Schwab cash balance and trade history CSV. Contains:
- Daily cash balance snapshots (BAL rows)
- Individual trade executions (TRD rows) — BOT (buy) and SOLD entries
- Ref numbers, prices, share counts, amounts, running balance
- Starting balance: ~$61.52

## Data Format

```
DATE, TIME, TYPE, REF#, DESCRIPTION, Misc Fees, Commissions & Fees, AMOUNT, BALANCE
```

## Early Tickers Visible (first few weeks)

UAVS, IVPR, ECDA, KALA, EVTV — all micro-cap / sub-$2 tickers consistent with small-cap momentum style.

## Relevance

- **Cross-reference source** for the live trade journal at goheat207.pythonanywhere.com
- **Starting balance context**: very small account — sizing and risk calculations should account for this
- **Full P&L history**: 4.5 months of data gives a complete picture of performance trajectory
- Can be parsed to extract: win rate, avg winner, avg loser, best/worst days, loss streak patterns

## How to Use

Ask Claude to analyze specific date ranges:
> "Read the Schwab CSV and pull all trades from January. Show win rate, avg winner, avg loser, and the 3 worst trades."

Or cross-reference with journal:
> "Compare the Schwab CSV with the journal API for February. Flag any discrepancies."

## Links

[[trading_context]] · [[q2_goals]] · [[Blaine]]
