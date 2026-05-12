# Token Economy

## Core Idea

Tokens are AI attention.
Every token loaded into context costs attention that could go to the task.

Overloaded context produces:
- lower quality outputs
- worse instruction following
- context drift mid-session
- diluted reasoning

---

## The Token Budget Model

Think of every session as having a fixed attention budget.

```
Session Budget
├── CLAUDE.md (routing)           ~200 tokens    [always]
├── 1-3 domain context files      ~500-1500 tokens [task-specific]
├── Work artifact (if needed)     ~500-2000 tokens [optional]
└── Available for output          [everything remaining]
```

The goal: spend the minimum tokens on context to maximize tokens on output quality.

---

## File Size Guidelines

| File Type            | Target Length   | Maximum |
| -------------------- | --------------- | ------- |
| CLAUDE.md            | 60-80 lines     | 100     |
| Domain context files | 80-120 lines    | 150     |
| Workflow files       | 60-100 lines    | 130     |
| Templates            | 40-80 lines     | 120     |
| Work artifacts       | As needed       | —       |

When a file exceeds its maximum: split by concern.

---

## Selective Loading Rules

Always ask before loading a file:
1. Is the task in this file's domain?
2. Does this file contain rules that constrain the current output?
3. Would the output be meaningfully worse without it?

If the answer to all three is "no" — do not load it.

---

## Context Drift

Context drift happens when:
- Too many unrelated concepts are in context simultaneously
- A long session accumulates context from multiple task switches
- Domain boundaries blur over time

Signs of drift:
- Output quality decreasing mid-session
- AI mixing rules from different domains
- Responses feel generic or unfocused

Fix: start a new session. Load only the relevant files.

---

## Token-Efficient Markdown Design

Write markdown files that:
- Use headers to enable partial reading
- Put the most important rules first
- Front-load context so later lines can be truncated if needed
- Avoid restating concepts from other files

Avoid:
- Repeating rules that exist in CLAUDE.md or ai_philosophy.md
- Long preambles before the actual content
- Examples that consume tokens without adding new information

---

## Workspace Compounding

Every time you refine a context file to be more precise and shorter:
- Future sessions get the same value at lower token cost
- The workspace compounds in efficiency over time

Refining files is not maintenance. It is optimization.
