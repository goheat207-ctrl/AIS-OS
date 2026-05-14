# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.
```

Keep it terse. Future-you will thank present-you for capturing the *why*, not just the *what*.

---

## 2026-05-11 — AIOS Day 1 setup

**Decision:** Set up AIS-OS with AIS-OS starter kit + AI_OS workspace. Not focused on selling yet — building trading tools and local apps first.

**Why:** Blaine's Q2 priorities are P&L improvement, trade journal prototype, and TOS backtester. The OS needs to support those before anything else.

**Alternatives considered:** Starting with selling/monetization first. Rejected — not ready and not the priority.

**Owner:** Blaine

## 2026-05-11 - Add Codex to AIS-OS

**Decision:** Add Codex as the AIS-OS implementation partner with a root `AGENTS.md`, a standing role file, and a wiki entity.

**Why:** Blaine needs low-friction execution support that turns ideas into working files, scripts, dashboards, and systems without adding cognitive load.

**Alternatives considered:** Leave Codex as an external chat tool only. Rejected because the OS should preserve how Codex should operate inside this workspace.

**Owner:** Blaine

## 2026-05-13 — Quick note

**Decision:** Testing main.py orchestrator - all commands working

**Owner:** Blaine

## 2026-05-14 — Neuron Architecture + wiki-ingest skill

**Decision:** Redesign the second brain around five isolated domain neurons (trading, coding, business, os_design, general). Each neuron has a `current_state.md` (what I currently know in this domain) and an `index.md` (registry of filed entries). Built `/wiki-ingest` skill to route new knowledge into the correct neuron with AI classification + human review before filing.

**Why:** The existing wiki was a flat pile — all topics mixed together. AI was loading undifferentiated context or the wrong domain entirely. Car mechanics knowledge doesn't help you cook. The neuron structure lets AI load ONLY the relevant domain per session, cutting cognitive overhead and making context actually useful.

**Autonomy level:** L2 — AI drafts and classifies, Blaine reviews and approves before filing. Advance to L3 after 10 validated entries.

**KPI:** Cut costs (cognitive overhead). Metric: sessions where AI loads correct domain context without re-explanation — target 80%+ within 2 weeks of use.

**Alternatives considered:** Continuing with flat topics/ structure. Rejected — it's the root cause of AI context failures.

**Bike Method Phase:** 1 — run manually, review every output.

**Owner:** Blaine
