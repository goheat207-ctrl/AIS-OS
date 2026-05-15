---
published: 2026-05-14T16:31:00
description: Second Brain architecture
relevance: high
type: ENHANCEMENTS
tags:
  - ai_partner
  - ai_workflow
  - analysis
  - auditLog
  - consistency
  - discipline
  - framework
  - second_brain
  - workflow
---

### PHASE 1

The real problem is the second brain is organized as a pile, not as a brain.

  Your analogy is the best description of the problem I've seen: learning car mechanics doesn't help you cook.
  Knowledge only transfers when it's categorized correctly. Right now the Obsidian vault has information in it, but
  it's not organized into isolated domains — what you're calling neurons. So when AI loads context, it either loads
  everything (bloated, unfocused) or the wrong thing entirely.

  That's why it doesn't feel like the AI "gets it." It probably doesn't, because the structure isn't telling it what
  domain it's in.

  The candidate: Build a Neuron Architecture for the second brain.

  One dedicated folder per learning domain — Trading, Coding, Business, OS Design — each with its own index, active
  notes, and a "current state of knowledge" summary file that the AI loads selectively. You drop something in
  Trading, it stays in Trading. The AI working on a code build never even sees your trading notes.

  This directly solves:
  - AI loading irrelevant context
  - Knowledge getting lost in a flat pile
  - You having to manually manage what the AI "knows" each session

## Phase 2 — Method Scoping it now. Five steps, fast.

  Step 1 — The constraint Every session, the AI either loads too much (everything in the vault) or the wrong thing (trading context when you're coding). You're paying cognitive overhead to re-orient it every time. The bottleneck: no domain separation
  means no selective loading.

  Step 2 — EAD
  - Eliminate: Can't kill it — organized context is what makes the AI useful at all.
  - Automate: Yes. Folder structure is deterministic (no AI needed). Ingest routing needs one AI classification step.  - Delegate: Not applicable.

  Step 3 — The process map
  - Trigger: You drop something into Agentic_OS/raw/ or want to save a lesson/note
  - Data source: The raw note, article, or insight
  - Transformation: Classify to a domain → format as wiki entry → write to correct neuron
  - Decision point: Which neuron? Trading / Coding / Business / OS Design / General
  - Destination: Agentic_OS/wiki/neurons/{domain}/ + update that domain's current_state.md

  Step 4 — Autonomy level
  L2. AI classifies and drafts the entry, you review before it's filed. No silent auto-filing until you've seen it
  work 10+ times.

  Step 5 — KPI
  Bucket: Cut costs (cognitive overhead).
  Metric: Sessions where AI loaded correct domain context without you re-explaining — from effectively 0% to 80%+.



  All five check out. Moving to Machine.


## Phase 3 — Machine

  Two artifacts, in this order:

  Artifact 1 (deterministic, zero AI): Build the neuron folder structure in Agentic_OS/wiki/neurons/ — five domains,
  each with index.md and current_state.md. No skill needed, just the folders and files.

  Artifact 2 (AI-assisted skill): A wiki-ingest SKILL.md — you drop a raw note, it classifies the domain, formats it,   and drafts the wiki entry for your review.

  Both ship at Bike Method Phase 1 — you run manually, watch it, correct it by hand. You do NOT set this to auto-file   until you've validated 10 entries and trust the classification.

  ---
  Ready to build both right now. Say go.