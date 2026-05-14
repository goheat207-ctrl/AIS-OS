---
name: summary
description: Use when Blaine asks "what am I using this for", "summarize my OS", "what does my AIOS do", "give me a summary of my system", or any variation of wanting a high-level picture of how AIS-OS is currently being used. Produces a plain-language breakdown of active domains, tools, agents, knowledge base, and gaps.
tools: Read, Glob, Bash
---

## What this skill does

Scans the live state of AIS-OS and produces a plain-language summary of:
- Which domains are active vs. scaffolded but empty
- What agents exist and what they do
- What the wiki/knowledge base contains
- What builds are in progress
- What gaps the OS itself has flagged

This is a diagnostic read — no writes, no scoring. Just an honest picture of what the system is actually doing for Blaine right now.

## Today's context

- **Date:** !`date +%Y-%m-%d`
- **Project root:** D:\AIS-OS

## Execution

### Step 1: Read the index and domain state

Read these files in parallel:

- `Agentic_OS/wiki/index.md` — what's in the second brain
- `context/priorities.md` — current Q-level priorities
- `domains/trading/README.md` — trading domain active builds
- `domains/software/README.md` — software domain state
- `domains/business/README.md` — business domain state
- `domains/automation/README.md` — automation domain state
- `domains/learning/README.md` — learning domain state

### Step 2: Scan agents and skills

- Glob `.claude/agents/*.md` — list all agents, read frontmatter for name + description
- Glob `.claude/skills/*/SKILL.md` — list all skills, read frontmatter for name + description

### Step 3: Assess domain activity

For each domain, classify as one of:
- **Active** — wiki pages exist, builds in progress, or agents actively serving it
- **Scaffolded** — folder and README exist but no content, no builds, no wiki pages
- **Not started** — missing or empty

Trading activity signal: wiki topics with `relevance: high` + agents present = Active.
All other domains: check if wiki has any pages for that domain, and if domain README has any checked items.

### Step 4: Identify flagged gaps

Read the `## Gaps Flagged` section at the bottom of `Agentic_OS/wiki/index.md`. Report these verbatim — they are gaps the OS tracked itself.

### Step 5: Output the summary

Print directly in chat. Format exactly as follows:

---

```
## What AIS-OS Is Doing For You Right Now

### {Domain Name} ({primary / secondary / inactive}) — {one-line description of activity level}

This is where {X}% of active use is. {1-2 sentences on what's populated and why.}

**{Sub-section — e.g. Knowledge base, Active agents, Active builds}**
- {item} — {what it does, one line}
- {item} — {what it does, one line}
[repeat for all items in category]

[Repeat ### block for each domain]

---

### Gaps Your Own OS Flagged

- {gap 1}
- {gap 2}
[list all gaps from wiki index verbatim]

---

### Summary

**You're using it as:** {plain-language one-liner}

**It was designed to be:** {plain-language one-liner}

{1-2 sentences on what's built vs. what's waiting. Name the most behind Q2 build target by name.}
```

---

## Output rules

- No headers beyond what the format specifies. No audit scores. No percentages unless useful.
- Domain sections only appear if there is something to say — skip fully empty domains with one line: `{Domain} — no active content yet.`
- Agents listed by what they actually do, not their file names.
- Wiki topics grouped by type (knowledge base, sources, playbooks) — not listed individually. State the count and a few representative examples.
- Gaps section always appears last, always pulled from `wiki/index.md` Gaps Flagged section — don't invent gaps.
- Tone: casual, direct, short sentences. Bullet points over paragraphs. Match Blaine's voice register.
- Length: enough to be useful, short enough to read in 2 minutes. No filler.

## Notes

- Read-only. Never modify any file.
- If `wiki/index.md` doesn't exist, say so and scan `Agentic_OS/wiki/topics/` directly.
- If a domain README is missing, classify that domain as Not Started.
- Don't editorialize beyond what the files support. If a domain is empty, say it's empty.
