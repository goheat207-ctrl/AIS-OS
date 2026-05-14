---
bike-method-phase: 1  # Phase 1 — Training wheels. Run manually. Review every output before filing.
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.
name: wiki-ingest
description: Routes a raw note, article, or insight into the correct neuron in the second brain. Classifies domain, formats as wiki entry, presents for review before filing.
trigger: manual — run when you have something worth saving to the second brain
---

# /wiki-ingest

Takes a raw source or note from `Agentic_OS/raw/` (or a note you paste directly) and routes it into the correct neuron folder. AI classifies and drafts. You review before anything is filed.

**Phase 1 rule: read the output, correct it by hand if wrong, approve before writing. Do NOT auto-file until you've validated 10+ entries.**

---

## How to run

**Option A — file already in raw/**
> `/wiki-ingest` — I'll show you what's in `Agentic_OS/raw/` and ask which one to process.

**Option B — paste content directly**
> `/wiki-ingest [paste your note or content here]`

**Option C — specify a file**
> `/wiki-ingest Agentic_OS/raw/your-file.md`

---

## What this skill does

### Step 1 — Read the source
Read the raw file or pasted content in full.

### Step 2 — Classify the domain
Pick exactly ONE of these five neurons:

| Neuron | When to use |
|--------|-------------|
| `trading` | Setups, strategies, price action, tape reading, risk, catalysts, trade reviews, market knowledge |
| `coding` | Python, HTML/CSS/JS, ThinkScript, tools, APIs, build patterns, debugging |
| `business` | Startups, client work, local business tools, AI consulting, monetization ideas |
| `os_design` | AI OS architecture, skills, agents, automation systems, workflows, Claude Code |
| `general` | Mental models, productivity, cross-domain content, personal philosophy |

Show the classification and a one-sentence reason. Ask: "Does this classification look right?"

### Step 3 — Draft the wiki entry
Format as:

```markdown
# [Title — descriptive, not the filename]

**Source:** [URL, filename, or "direct note"]
**Date ingested:** [YYYY-MM-DD]
**Neuron:** [domain]
**Tags:** [2-4 relevant tags]

## Summary
[3-5 bullet points. What is the core insight? What is actionable? What is the key takeaway?]

## Key Points
[Numbered list of the most important specifics — facts, rules, patterns, techniques]

## How to apply
[1-3 sentences on when and how Blaine uses this. Concrete, not generic.]

## Raw notes
[Optional — paste any quotes or raw extracts worth preserving verbatim]
```

Show the full draft. Ask: "Looks good to file, or any changes?"

### Step 4 — File it (only after approval)
Once approved:

1. Write the entry to `Agentic_OS/wiki/neurons/{domain}/{slug}.md`
   - Slug = `YYYY-MM-DD_{short_title}.md` (snake_case, no spaces)

2. Append one line to `Agentic_OS/wiki/neurons/{domain}/index.md` under the Entries table:
   ```
   | {slug}.md | {title} | {YYYY-MM-DD} |
   ```

3. If the source substantially adds to what's known in the domain, append 1-2 bullet points to `Agentic_OS/wiki/neurons/{domain}/current_state.md` under the relevant section.

4. If the raw file came from `Agentic_OS/raw/`, confirm with user before moving or leaving it.

### Step 5 — Confirm
Print:
```
Filed: Agentic_OS/wiki/neurons/{domain}/{slug}.md
Neuron: {domain}
current_state.md: [updated / no change needed]
```

---

## Rules

- **Never file without explicit approval.** Show the draft, wait for "yes" or "go" or "file it."
- **One file per run.** Don't batch multiple sources in one pass.
- **Classify to ONE neuron only.** If it crosses two domains, pick the primary one.
- **Don't rewrite the source.** Summarize and extract. The raw file is the source of truth.
- **Don't touch files outside `Agentic_OS/wiki/neurons/`.** No modifications to CLAUDE.md, existing topics/, or any other file.

---

## The five neurons

```
Agentic_OS/wiki/neurons/
├── trading/       — price action, setups, risk, catalysts, tape reading
├── coding/        — Python, HTML, ThinkScript, tools, APIs
├── business/      — startups, clients, local apps, consulting
├── os_design/     — AI OS, skills, agents, automation, workflows
└── general/       — mental models, productivity, cross-domain
```

---

> *Adapted from The Three Ms of AI™ © 2026 Nate Herk. All rights reserved.*
> *Bike Method Phase 1 — run manually, watch every output, advance phases only when validated.*
