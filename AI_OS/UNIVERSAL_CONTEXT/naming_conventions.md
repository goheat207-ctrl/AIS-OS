# Naming Conventions

## Universal Standard

All files use `snake_case.md` — no exceptions.

---

## File Naming Pattern

### Context and System Files

```
[concept].md
```

Examples:
- `ai_philosophy.md`
- `trading_operating_system.md`
- `risk_framework.md`
- `voice_constraints.md`

### Work Artifacts (dated output)

```
YYYY-MM-DD_[topic]_[stage].md
```

Examples:
- `2026-05-07_aapl_analysis_draft.md`
- `2026-05-07_scanner_momentum_v2.md`
- `2026-05-07_youtube_script_final.md`

Stage suffixes:
- `_draft` — in progress
- `_review` — ready for review
- `_final` — approved output
- `_archive` — completed, stored

### Templates

```
_template_[type].md
```

Leading underscore marks it as a scaffold, not content.

Examples:
- `_template_project_claude.md`
- `_template_trading_journal.md`
- `_template_research_brief.md`

---

## Folder Naming

All folders use `SCREAMING_SNAKE_CASE`:
- `ACTIVE_PROJECTS`
- `TRADING_SYSTEMS`
- `CONTENT_SYSTEMS`

This visually separates folder architecture from file contents.

---

## Version Tracking

Append `_v[N]` only when you need to preserve history alongside a new version.

Prefer overwriting the file directly if git or session history handles versioning.

---

## Anti-Patterns

Avoid:
- `New_Document(1).md`
- `final_FINAL_v3_real.md`
- `notes.md` (too vague)
- `misc.md` (a warning sign — split the concern)
- Spaces in filenames
- CamelCase in filenames
- Generic names that don't describe the content

---

## Why This Matters

Consistent naming is lightweight indexing.
It reduces:
- search time
- routing ambiguity
- token waste on finding files
- cognitive load when returning to old work

The filename should describe the content precisely enough that you never have to open it to know what's inside.
