# AI Memory Rules

## The Problem

AI sessions are stateless.
Each new session starts with no memory of previous work.

The workspace is the memory system.
Files outlive sessions. Sessions do not outlive files.

---

## Memory Architecture

```
Persistent Memory (files)
├── UNIVERSAL_CONTEXT\     — Global rules that never need re-explaining
├── CORE_SYSTEMS\          — System mechanics
├── TRADING_SYSTEMS\       — Domain knowledge that compounds
├── CONTENT_SYSTEMS\       — Voice and workflow that stays consistent
└── ACTIVE_PROJECTS\       — Work in progress

Ephemeral Memory (session)
└── Everything discussed in the current conversation window
```

When a session ends, anything not written to a file is lost.

---

## What Belongs in Files

Write to files when:
- A decision was made that should carry forward
- A convention was established or changed
- A workflow was refined or validated
- A key insight emerged that should inform future work
- A context file needs updating based on new information

Do NOT write to files:
- Mid-task scratch work
- Temporary outputs that will be superseded
- Information that already exists in a file

---

## Cross-Session Continuity Protocol

To resume work across sessions:
1. End the session by updating MEMORY\session_handoff.md
2. At start of next session, read session_handoff.md first
3. Load the relevant domain context files
4. Continue from the handoff point

---

## Memory File Maintenance

Context files should be:
- Updated when conventions change
- Trimmed when they accumulate outdated rules
- Split when they cover more than one concern
- Never allowed to grow indefinitely

A stale context file is worse than no context file.
It actively misleads.

---

## What NOT to Memorize

Do not put these in context files:
- Information derivable from reading the current code
- Git history or recent changes (use git log)
- Debugging steps or fix recipes
- Ephemeral task details from one session

These do not generalize. They clutter context.

---

## Memory Quality Rule

Every memory file should answer the question:
> "Would a future session be meaningfully better for having loaded this?"

If the answer is no — the file does not belong in persistent memory.
