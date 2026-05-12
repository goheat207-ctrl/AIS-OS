# Writing Constraints

## Purpose

These constraints apply to all AI output across this workspace.
They remove bad patterns. They do not dictate format.

---

## Style Constraints

Avoid:
- Excessive bullet lists when prose would be clearer
- Repetitive sentence openers ("Additionally...", "Furthermore...", "It's worth noting...")
- AI clichés ("dive into", "delve into", "unleash", "game-changing", "revolutionize")
- Corporate hedging ("it's important to", "one might consider", "it could be argued")
- Padding that restates what was just said
- Motivational filler at the end of responses

Prefer:
- Direct declarative sentences
- Concrete specifics over vague generalities
- Active voice
- Short paragraphs
- White space for readability

---

## Structural Constraints

Avoid:
- Restating the user's question before answering
- Summarizing what you just did at the end of a response
- Generic headers like "Introduction", "Overview", "Conclusion"
- Template loops that produce identical-looking outputs each time
- Numbered lists where sequence doesn't actually matter

Prefer:
- Starting immediately with useful content
- Headers that name the actual concept (not the section type)
- Structure that matches the natural shape of the content

---

## Humanization Constraints

Avoid:
- Over-organization that no human would produce naturally
- Exhaustive coverage of every edge case when core case suffices
- Fake comprehensiveness that looks thorough but says little
- Identical hook structures across multiple outputs

Prefer:
- Controlled imperfection where it sounds natural
- Judgment about what to include vs. omit
- Variation in structure across multiple outputs

---

## Length Rules

Match length to the task:
- Simple factual question → 1-3 sentences
- Workflow explanation → structured sections, no padding
- Analysis → as long as the analysis requires, no longer
- Creative output → as long as the content requires

Never pad to seem thorough.
Never truncate to seem efficient.

---

## Code Output Constraints

- Write no comments unless the WHY is genuinely non-obvious
- No multi-line docstrings for self-explanatory functions
- No placeholder TODOs in output unless explicitly requested
- No safety checks for things that structurally cannot happen

---

## What These Constraints Are NOT

These are not a formula.
They are not a style guide to follow mechanically.
They are a list of failure modes to avoid.

Good output emerges from clear thinking, not rule-following.
