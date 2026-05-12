# Context Engineering

## Core Principle

Context engineering > prompt engineering.

A well-structured workspace produces better outputs than a better prompt in a worse workspace.

---

## The 3-Layer Context Model

```
Layer 1 — Global Map
  Purpose: workspace overview, routing rules, global constraints
  Files:   CLAUDE.md, folder_architecture.md
  Load:    every session

Layer 2 — Domain Context
  Purpose: task-specific rules, workflow, role identity
  Files:   per-folder context files
  Load:    only when task matches domain

Layer 3 — Work Artifacts
  Purpose: actual outputs, drafts, data, research
  Files:   ACTIVE_PROJECTS contents
  Load:    only when working on specific artifact
```

Never collapse all three layers into one context dump.
Load incrementally. Load selectively.

---

## Context Loading Rules

Load a file when:
- The current task directly requires its domain
- The file contains rules that constrain the current output
- The file contains reference patterns you need to match

Do NOT load a file when:
- The task is in a different domain
- The file is "interesting but not necessary"
- You are trying to give the AI "full context"

Full context is not an optimization. It is a cost.

---

## Context Boundaries

Each domain has a boundary:

| Domain         | Context Boundary                            |
| -------------- | ------------------------------------------- |
| Trading        | Do not load content or agent context        |
| Content        | Do not load trading or technical context    |
| Agent Systems  | Do not load trading or content context      |
| Research       | Load thinking models, not workflow details  |

Enforce boundaries. Cross-domain context degrades quality.

---

## File Size Rule

If a markdown file grows past ~150 lines:
- Check if it covers more than one concern
- If yes: split into focused sub-files
- If no: trim redundancy

One file. One concern. One purpose.

---

## Session Context Hygiene

At the start of a session:
1. Load CLAUDE.md (routing + global rules)
2. Identify task domain
3. Load only the 1-3 relevant domain files
4. Begin work

At the end of a session:
1. Identify what was produced or decided
2. Update relevant context files if conventions changed
3. Archive outputs to correct folder

---

## Routing Is Context Management

The routing table in CLAUDE.md is not a convenience feature.
It IS the context management system.

Follow it.
