---
name: wiki-search
description: Grep-based keyword search across the Obsidian wiki. Returns matching file names and line snippets. No embeddings — fast and lightweight.
trigger: manual — run with a keyword argument
---

# /wiki-search

Search the wiki for any keyword. Returns matching file paths and line-level snippets.

---

## How to run

> `/wiki-search [keyword]`

Examples:
- `/wiki-search pullback`
- `/wiki-search risk management`
- `/wiki-search catalyst`

---

## What this skill does

### Step 0 — Validate input

- If no keyword provided (empty string), respond:
  ```
  Usage: /wiki-search [keyword]
  Example: /wiki-search pullback
  ```
  Stop here.

- If keyword exceeds 100 characters, respond:
  ```
  Keyword too long (max 100 characters). Try a shorter search term.
  ```
  Stop here.

### Step 1 — Run file-level search

Use the Grep tool to search recursively across the entire wiki:
- Path: `Agentic_OS/wiki/`
- Pattern: the keyword (case-insensitive)
- Output mode: `files_with_matches`

Record the list of matching files.

### Step 2 — Run snippet search

Use the Grep tool again with:
- Path: `Agentic_OS/wiki/`
- Pattern: the keyword (case-insensitive)
- Output mode: `content`
- Show line numbers (`-n: true`)
- Limit to first 30 matches (`head_limit: 30`)

### Step 3 — Format and print results

**If zero files matched:**
```
No results for "[keyword]" in wiki.
Try a broader term or check the spelling.
```

**If files matched, print:**

```
## Wiki search: "[keyword]"
Found in X file(s)

### Files
- Agentic_OS/wiki/topics/foo.md
- Agentic_OS/wiki/neurons/trading/bar.md
[...]

### Snippets (up to 30 lines)
Agentic_OS/wiki/topics/foo.md:14  — matching line text
Agentic_OS/wiki/neurons/trading/bar.md:7  — matching line text
[...]
```

Rules:
- Show full relative path for each file (from repo root).
- Keep snippet lines trimmed — show only the matched line, no surrounding context unless the match is mid-word and context is needed.
- If more than 30 snippet lines exist, append: `(results truncated — refine your search for more precision)`
- Never modify any wiki file. This is read-only.
