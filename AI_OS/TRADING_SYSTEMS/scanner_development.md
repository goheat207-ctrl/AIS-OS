# Scanner Development

## Purpose

This file defines how to approach building and iterating trading scanners.

---

## Scanner Development Workflow

```
1. Define the setup
2. Translate to criteria
3. Build the scan logic
4. Test against historical examples
5. Refine criteria
6. Iterate
```

Never skip step 4. Untested scanners generate noise, not signal.

---

## Setup Definition (Before Writing Any Code)

Answer these questions first:
- What pattern or condition are we scanning for?
- What timeframe does this setup live on?
- What is the expected behavior after the setup triggers?
- What market conditions is this setup valid in?
- What conditions would invalidate this setup?

Document answers in a `[setup-name]_scanner.md` file before touching ThinkScript.

---

## Criteria Translation

Convert the setup definition into measurable criteria:

| Setup Element      | Measurable Criteria                          |
| ------------------ | -------------------------------------------- |
| Momentum           | Price % change, volume ratio, ATR multiple   |
| Float              | Shares outstanding < [threshold]             |
| Catalyst           | News presence flag (manual filter)           |
| Technical level    | Price relative to MA, VWAP, prior high       |
| Volume             | Relative volume > [multiplier] vs average    |

Start with 3-5 criteria. More criteria = smaller universe = potentially over-fit.

---

## ThinkScript Notes

Key patterns:
- Use `reference` to pull data from other timeframes
- Use `Average()` for moving averages and average volume
- Use `Sum()` for cumulative conditions over N bars
- Watchlist columns are different from scan conditions — build both

---

## Iteration Protocol

After first test run:
1. How many results? (too many = criteria too loose, too few = too tight)
2. Do the results match the intended setup? (spot-check 10-20)
3. What false positives appear? (what criteria would filter them?)
4. What true setups are being missed? (what criteria is over-filtering?)

Adjust one criterion at a time.
Document each version.

---

## Scanner File Naming

```
[setup-type]_scanner_v[N].md     ← Documentation + criteria
[setup-type]_scanner_v[N].ts     ← ThinkScript code
```

Keep versions. Do not overwrite without saving prior version.
