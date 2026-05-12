# Content Operating System

## What This Is

Master context file for all content production.
Load at the start of any content creation session.

---

## Content Philosophy

Content is compressed knowledge.
It is not performance. It is not volume. It is not consistency theater.

Good content:
- Contains a real idea the reader didn't have before
- Respects the audience's intelligence
- Has a clear point of view
- Earns the reader's attention before asking for it

---

## Content Production Pipeline

```
Idea → Angle → Structure → Draft → Review → Publish
```

### Idea
Raw capture. No editing. Just write it down.

### Angle
What is the specific take? What makes this version of the idea worth reading/watching?
A topic is not an angle. "Trading psychology" is a topic. "The trade you were most confident about reveals your biggest blind spot" is an angle.

### Structure
How does the idea unfold? Beginning → middle → end (even for short-form).

### Draft
Write to completion first. No editing during draft.

### Review
Apply voice_constraints.md. Cut anything that doesn't serve the core idea.

### Publish
Format for platform. Store final in project `finals\` folder.

---

## Platform-Specific Notes

| Platform    | Priority                          | Format            |
| ----------- | --------------------------------- | ----------------- |
| YouTube     | Hook (first 30s), retention       | Script + b-roll   |
| X / Twitter | First line hook, punchy           | Thread or single  |
| Newsletter  | Subject line, first paragraph     | Long-form prose   |
| Blog        | SEO headline, opening hook        | Structured prose  |

Load platform-specific context only when working on that platform.

---

## AI Role in Content

AI can:
- Generate angles from a topic and audience context
- Draft structures from approved angles
- Write drafts based on approved structures
- Apply voice_constraints.md in review
- Repurpose existing content across formats

AI cannot:
- Determine if an idea is worth pursuing (human judgment)
- Replace the creator's point of view
- Know if the hook actually works (requires audience feedback)
