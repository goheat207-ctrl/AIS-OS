# AIS-OS Intake

This is the source-of-truth file for your AIOS. Fill it in by typing, voice-pasting (Wispr Flow / OS dictation), or running `/onboard` for a guided conversation. Whichever mode, this file is what `/onboard` reads to scaffold your Day-1 setup.

**Hard cap: 7 questions.** Each answerable in under 60 seconds. Don't overthink — you can edit and re-run `/onboard` any time.

---

## Q1 — Who are you, what do you sell, who do you sell it to?

Identity, offer, ICP. One paragraph each is fine.

```
I'm Blaine — a small cap stock trader and beginner coder. Right now I do it for myself, but my goal is to build the best dashboards and products that help beginner traders learn faster and get profitable quicker. I also want to build apps and web tools for family, friends, and local businesses in my area, because AI isn't widely known or used where I live yet.
```

---

## Q2 — Paste 1-2 things you've written recently. Don't edit them.

An email, a LinkedIn post, a DM, a doc — anything that sounds like you when you're not trying. **Paste verbatim.** Do not type these mid-conversation with Claude — chat-shaped samples are worse than no samples (voice contamination).

```
Are Data Centers Worth the Noise to Local Communities?

"Multiple cities of people have filed lawsuits and complaints against these data centers because of the noise."

"The first question I ask myself is, are we gonna need data centers in America? Yes, if we wanna compete in the modern world, in the modern economy, we are going to need them. They are good for society and good for the economy."

What politicians like Mamdani are missing in 2026. 

In 1970, 85% of S&P 500 wealth was tied to tangible assets. Politicians could bully the wealthy because money couldn't move.

Today, 90% is intangible: code, IP, capital.

Wealth is now mobile. Push too hard & it leaves.
```

```
Corporate convinced an entire generation that:

• Working 40+ hours = Success
• Trading time for money = Wealth
• Climbing ladders = Winning
• Retirement at 65 = Freedom

Meanwhile:

• The HVAC guy makes 3x your salary
• The laundromat owner works 5 hours/week
• The boring business owner retired at 35
• The plumber's kid will inherit millions

We studied the wrong people.
```

---

## Q3 — What are your 2-3 biggest priorities for the next 90 days?

Quarterly priorities. Not yearly aspirations. Things that, if not done by July, would make you say "I wasted Q2."

```
1. Fix my losing P&L — cut losses down to 0.25–0.33% per trade by end of July.
2. Finish my Trade Journal / backtest prototype.
3. Build a working TOS (thinkorswim) profitable strategy backtester with a Dilution Tracker, Learning System, and Thinkscript-coded study filters for watchlist scans that produce tradeable tickers.
```

---

## Q4 — Where does revenue actually land, and where is it tracked?

Multiple answers OK. Stripe? Skool? GoHighLevel? QuickBooks? A spreadsheet?

```
PayPal, multiple brokerage accounts (thinkorswim/TD Ameritrade), and several debit cards/bank accounts. No formal tracking system yet.
```

---

## Q5 — Where do you talk to customers, your team, and the outside world day-to-day?

Email (which one — Gmail / Outlook)? Slack? Teams? DMs (Skool / Discord / iMessage)? Phone?

```
Gmail, Twitter/X, Facebook, Instagram, Discord
```

---

## Q6 — Where do meeting recordings, notes, and important docs live?

Granola? Otter? Fireflies? Google Drive? Notion? Dropbox? A folder on your desktop you keep meaning to organize?

```
Obsidian
```

---

## Q7 — What's the one task that eats your week, and where do you currently track work?

The single biggest time-suck or recurring drudgery. Plus where tasks/projects live (ClickUp / Asana / Linear / Notion / a notebook).

```
Everything competes for attention. Solo operator, 41, severe ADHD/OCD — staying organized and focused is the core struggle. No single tracking system in place yet. Working on it incrementally.
```

---

When this file is filled, run `/onboard` (or re-run it) and the wizard will scaffold your Day-1 file set: `context/`, `references/voice.md`, populated `connections.md`, and a filled `CLAUDE.md`.
