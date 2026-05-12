---
title: Obsidian Web Clipper Settings For AIS-OS
type: source
tags: [obsidian, web_clipper, second_brain, setup]
source_count: 1
created: 2026-05-12
updated: 2026-05-12
---

# Obsidian Web Clipper Settings For AIS-OS

Use this file to import AIS-OS clipping templates into Obsidian Web Clipper:

`D:\AIS-OS\obsidian-web-clipper-ais-os-settings.json`

## Where Clips Go

- General articles: `Agentic_OS/raw/articles`
- Trading research and playbooks: `Agentic_OS/raw/articles`
- X / social posts: `Agentic_OS/raw/articles`
- YouTube / video notes: `Agentic_OS/raw/articles`
- Personal notes and ideas: `Agentic_OS/raw/notes`

## Why This Routing

The second brain uses `Agentic_OS/raw/` as the intake area and `Agentic_OS/wiki/` as the compiled knowledge base.

Clips should land in `raw/` first. Later, Codex can ingest useful clips into wiki pages, update links, and skip low-signal material.

## Schema Fields

The templates follow `[[SCHEMA]]` / `[[SCHEMA 1]]` metadata fields:

- `title`
- `type`
- `tags`
- `source_count`
- `created`
- `updated`

Clipped raw items use `type: source` because they are source material waiting for future ingest.

## Related Pages

[[SECOND_BRAIN_GUIDE]]
[[raw_source_inbox]]
[[trading_context]]
[[imported_trading_notes]]
