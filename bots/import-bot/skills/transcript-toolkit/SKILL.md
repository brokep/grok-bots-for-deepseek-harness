---
name: transcript-toolkit
description: "use this after parsing: normalize every transcript into one shape, search across all sessions, and build each expert's history seed"
---

# transcript-toolkit

Part of the Import Bot agent preset.

# Transcript toolkit

One reader for every harness, search across every session, and history seeds for the experts. It is part of `import-tools.py`, which parse-import copies out of the import-scripts skill. Plain Python on this computer, nothing to install. It reads the shapes each tool writes on disk (Claude Code JSONL, Cowork records and audit logs, Codex rollouts, Hermes state.db, OpenClaw databases, ChatGPT and Claude.ai conversation JSON) into one common document per session, text only.

## 1. Normalize (parse-import already ran it)

The parse step ends by normalizing every conversation. After more arrives, run it again on its own:

```bash
python3 /workspace/migration/tools/import-tools.py normalize /workspace/migration
```

It writes `/workspace/migration/pack/sessions/<harness>-<id>.json` and `index.json` (id, harness, title, dates, message counts, connectors seen, tools used). Re-run any time more arrives. Say one line: "N conversations across <harnesses>."

A document: `{"id","harness","title","timestamp","last_activity","cwd","model","messages":[{"role","text","timestamp"}],"tools":{name:count},"connectors":[...]}`. Tool calls are counted for connector evidence, never carried as text. Scaffolding the harnesses inject (`<environment_context>`, `<system-reminder>`, uploaded-file manifests) is dropped.

## 2. Search (the workflow hunt in plan-experts)

```bash
python3 /workspace/migration/tools/import-tools.py search /workspace/migration "every friday" -n 20
python3 /workspace/migration/tools/import-tools.py search /workspace/migration "draft" --from cowork
```

Literal, case-insensitive, across titles and every message. Ranked by hit count, three matching lines per session. Search the verbs that reveal routines ("every", "weekly", "each morning", "draft", "summarize", "follow up", "brief", "prep", "review"), the user's named workflows, and the account, product, and people names from memory.

## 3. View

```bash
python3 /workspace/migration/tools/import-tools.py view /workspace/migration cowork-local_0000 --max 40
```

Compact numbered text of one session. Use it on the top search hits to read what the user actually asked for before writing a playbook.

## 4. Seed (per expert, in spawn-experts)

```bash
python3 /workspace/migration/tools/import-tools.py seed /workspace/migration <slug> "cowork-local_0000...,chatgpt-c1,hermes-h1" --max-sessions 12 --max-messages 40
```

Writes `pack/<slug>-history.md` (readable, one heading per source conversation) and `pack/<slug>-history.jsonl` (the same turns as role and message envelopes). Newest sessions first, 40 messages per session, 400 KB total, redacted text stays redacted.

The `.md` becomes the expert's `<slug>-history` skill (description "use this when the user refers to something we discussed before in Cowork, ChatGPT, or another tool"), so the expert can read its own past even though those conversations were not in Grok Bot. Nothing uses the `.jsonl` today.
