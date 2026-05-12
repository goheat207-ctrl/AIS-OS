---
title: Second Brain Guide
type: topic
tags: [second_brain, obsidian, guide]
source_count: 1
created: 2026-05-11
updated: 2026-05-12
---

# Second Brain — How to Use It

The second brain is a query database, not a filing cabinet. Don't add things to feel organized. Add things you intend to ask questions about later. If you can't picture asking a question about it, don't add it.

---

## The filter before you add anything

Ask yourself one question: **"Will I ask Claude something about this in the next 30 days?"**

- Yes, specific question in mind → add it
- Maybe, vague feeling it's useful → skip it
- No → trash it

---

## What belongs where

### `raw/articles/` — X posts, blog posts, short reads
**Add if:** it has a specific workflow, prompt, or technique you want to apply.
**Skip if:** it's hype, opinion without method, or you'd forget it in a week anyway.

Examples worth adding: prompt collections, step-by-step workflows, tool comparisons.
Examples to skip: "AI is changing trading" takes, meme-level content, things you saved just because they felt interesting in the moment.

### `raw/books/` — playbooks, PDFs, full documents
**Add if:** it contains setup rules, exit rules, risk frameworks, or trading psychology you want to pull from.
**Skip if:** it's general finance news, macroeconomic commentary, or anything you'd never reference while building a TOS strategy.

Don't read these yourself. Drop them in and ask Claude targeted questions when you need them:
> "What does the Ross Cameron playbook say about stop placement on gap-and-go trades?"

### `raw/data/` — CSVs, screenshots, videos, export files
**Add if:** it's actual trade data, account statements, P&L exports, TOS screenshots of setups you want to study.
**Skip if:** it's a random screenshot without context, or a video you won't reference again.

Label files with the date and ticker when relevant: `2026-05-11-CLIK-setup.png` not `screenshot.png`.

### `raw/notes/` — your own writing, ideas, observations
**Add if:** it's a pattern you noticed mid-session, a rule you broke and why, an idea for a new setup. Anything that came from your own head.
**Skip if:** it's a half-formed thought you haven't tested. Write it in your journal instead — move to notes only when you've seen it work.

---

## Daily use (takes 5 minutes)

**Morning:**
After your pre-market scan, if you add a ticker to your watchlist, drop any relevant catalyst research into a quick note or just ask Claude directly — no need to save everything.

**After a trade:**
If you had a notable win or loss, note the setup type. You don't need to write it in the second brain — that's what the trade journal is for. But if you spotted something you want to study from a playbook, ask:
> "Read the Roland Wolf playbook and find how he handles this type of setup."

**When you clip something from X:**
Before saving to `raw/articles/`, ask the filter question. If yes, save it. Claude ingests it on request — you don't need to trigger ingest immediately.

---

## Weekly use (Friday, 15 minutes)

Once a week, tell Claude: **"Ingest anything new in Agentic_OS/raw/ that hasn't been processed yet."**

Claude will:
1. Read each new file
2. Create source pages for anything worth keeping
3. Update topic and entity pages if relevant
4. Skip low-signal content with a note explaining why
5. Update index.md and log.md

This keeps the wiki current without requiring daily maintenance.

Also once a week, run `/level-up` to find one manual task worth automating.

---

## Best use cases for what you already have

### Playbook library (20+ playbooks in `raw/books/`)
Best use: **setup rule extraction before building TOS scans.**
Ask: "What entry conditions do Ross Cameron, Roland Wolf, and Kellogg all agree on for small-cap gap plays?"
The overlap is your highest-confidence rule set.

**Don't:** try to read and synthesize these yourself. That's 40+ hours of work Claude can do in 10 minutes.

### Schwab account statement (`raw/data/2026-05-11-AccountStatement.csv`)
Best use: **identifying loss patterns by date range and ticker.**
Ask: "What were my 5 worst trading days from January through March? What tickers were involved?"
Cross-reference with the live journal for the full picture.

### Trading videos (SOBR, CLIK sessions in `raw/data/`)
Best use: **studying your own L2 and T&S reading in real setups.**
Claude can't watch videos, but you can note key moments and ask questions about what you observed.
Label new clips with ticker + date so you can find them: `2026-05-11-CLIK-morning-session.mp4`.

### X post articles
Best use: **prompt templates and workflow patterns** — not market takes.
Filter hard. 1 in 10 is worth keeping. The other 9 are noise that feels important in the moment.

### Market research PDFs (AI bubble, JPMorgan, defense stocks)
These are macro context, not trading setups. Add only if you plan to trade a specific sector based on the thesis. Otherwise skip — this is noise for your style.

---

## What the second brain is NOT for

- Saving things to feel organized (this is the most common mistake)
- General finance news or market commentary
- Content you read once and won't reference again
- Backup storage for random files
- Replacing the decisions log (that's for your decisions, not research)

---

## The ingest command

When you want Claude to process new raw files:

> "Ingest everything new in Agentic_OS/raw/ that hasn't been processed yet."

Or for a specific file:

> "Ingest Agentic_OS/raw/books/ross_cameron_playbook.html into the wiki."

Claude reads SCHEMA.md and follows the rules automatically.

---

## Signs the second brain is working

- You ask a question and Claude finds the answer in under 30 seconds using wiki pages
- Your TOS scans are built from rules extracted across multiple playbooks
- Your win rate is improving and you can point to a specific insight that changed your behavior
- You stop adding random content because the filter question blocks it

## Signs it's breaking down

- Files sit in raw/ for weeks without being ingested
- You have no idea what's in the wiki anymore
- You keep asking Claude questions it should already know from your context files
- The index grows faster than the quality of questions you're able to ask

Run `/audit` if any of those signs appear.
