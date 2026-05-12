---
title: "Post by @milesdeutscher on X"
source: "https://x.com/milesdeutscher/status/2053855320737472996"
author:
  - "[[@milesdeutscher]]"
published: 2026-05-11
created: 2026-05-11
description: "I stack Hermes agents with OpenClaw for financial research, and the results should be illegal. I track every politician, insider trader, an"
tags:
  - "clippings"
---
I stack Hermes agents with OpenClaw for financial research, and the results should be illegal.

I track every politician, insider trader, and I know EXACTLY what moves they're making.

If you can't beat them, join them.

The exact playbook for printing money from insider trading (copy me):

Requirements:

• OpenClaw setup

• Hermes Agent setup

Step 1. Define your research thesis

Before you send any prompts to either tool, you'll need to clarify exactly what you're trying to research.

This could be: a specific industry, asset class, market sector, and so on.

Examples:

• Tracking smart money buys in the semiconductor industry

• Tracking smart money buys in crypto

• Tracking a specific politician and where they're bidding (like Nancy Pelosi)

Step 2. Deploy Hermes agents to track the smart money (in parallel)

Hermes is your data layer. Spin up 5 agents at the same time, each with one job:

Agent 1: Track every politician's disclosed trades from the last 30 days (House and Senate stock disclosures)

Agent 2: Pull insider transactions (Form 4 filings, CEO/CFO buys and sells)

Agent 3: Scrape X sentiment from top 50 accounts on the topic

Agent 4: Pull on-chain data (whale wallets, TVL, exchange flows) \*if applicable\*

Agent 5: Monitor news, regulatory filings, and announcements from the last 30 days

Each agent runs independently. You're not waiting for one to finish before the next starts.

Step 3. Consolidate the output

Once your Hermes agents finish, dump every output into a single document.

(don't filter or summarize) - you want OpenClaw to see the raw data.

Step 4. Feed it all into OpenClaw

Open OpenClaw and paste the consolidated research file with this prompt:

"Act as an elite macro analyst. Below is raw data gathered from multiple sources on \[thesis\], including politician disclosures and insider transactions. Synthesize the findings, identify the strongest signals and contradictions, flag any unusual smart-money activity, and give me a clear directional view with conviction levels. Flag any data gaps that need follow-up."

OpenClaw will go deep, run its own reasoning chain, and produce a synthesized report.

Done. Now you're literally tapping into the financial data they don't want you to see (it's all public - you just had to find it).

Make sure to save this playbook so you don't lose it!

---

## Comments

> **Arbwick @Arbwickk** · [2026-05-11](https://x.com/Arbwickk/status/2053858056954388520)
> 
> @milesdeutscher Exactly. The key point is that this is public-data research, not insider trading.
> 
> The real edge is workflow speed: tracking disclosures, Form 4s, on-chain flows, news, sentiment, and market data continuously, then synthesizing them into cited, auditable outputs.

> **Xalecta @xalecta** · [2026-05-11](https://x.com/xalecta/status/2053920439102231005)
> 
> May I ask how much you are spending to build and have it run? I’ve become a token maxi and can go through over $1K in a month, and that’s just building stuff, without automated feeds.

> **OxVibly @0xVibly** · [2026-05-11](https://x.com/0xVibly/status/2053855723663299053)
> 
> I ship code, not insider trading bots. That playbook is just a jail sentence waiting to happen.