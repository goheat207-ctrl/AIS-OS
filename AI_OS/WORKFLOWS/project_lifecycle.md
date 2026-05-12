# Project Lifecycle

## A Project's Full Journey

```
1. Inception    → Idea captured, rough brief written
2. Setup        → Project folder created from template
3. Active       → Work in progress, in ACTIVE_PROJECTS\
4. Complete     → Output delivered, archived
5. Reference    → Available to inform future projects
```

---

## Stage 1 — Inception

Capture:
- What is this project?
- What domain does it belong to? (trading / content / research / agent / etc.)
- What does done look like?

Write a 3-5 line brief. No more.

---

## Stage 2 — Setup

1. Create folder: `ACTIVE_PROJECTS\[project-name]\`
2. Copy `PROJECT_TEMPLATES\_template_project_claude.md` → `CLAUDE.md` inside the project
3. Update the project CLAUDE.md with project-specific context
4. Identify which AI_OS domain files this project inherits from

Do not start building until setup is complete.
A disorganized start creates a disorganized project.

---

## Stage 3 — Active

Work lives in `ACTIVE_PROJECTS\[project-name]\`.

At the start of each session working on this project:
1. Read the project CLAUDE.md
2. Read the relevant AI_OS domain context files
3. Read session_handoff.md if resuming

At the end of each session:
1. Update session_handoff.md
2. Update the project CLAUDE.md if conventions changed

---

## Stage 4 — Complete

When the project is done:
1. Move the folder out of ACTIVE_PROJECTS
2. Archive to the appropriate domain folder or an ARCHIVE subfolder
3. Write a 3-line summary of what was built and any key learnings

Do not leave completed projects in ACTIVE_PROJECTS.
ACTIVE_PROJECTS should contain only live, current work.

---

## Stage 5 — Reference

Completed projects can be referenced in future work.
Key outputs may be extracted to the relevant domain folder (e.g., a scanner to TRADING_SYSTEMS).

The project folder itself is the archive.
Do not maintain a separate "learnings document" for every project — that creates accumulation without use.

---

## Project Folder Structure (Minimum)

```
ACTIVE_PROJECTS\[project-name]\
├── CLAUDE.md         ← Project-specific instructions (inherits from AI_OS)
├── brief.md          ← What this is and why
├── spec.md           ← How we're building it (optional for small projects)
└── [output files]    ← The actual work
```

Keep it lean. Only create files that serve a real purpose.
