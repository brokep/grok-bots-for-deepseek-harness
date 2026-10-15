---
name: account-sot-sync
description: "Map research outputs into Notion or Sheets system-of-record fields."
---

# account-sot-sync

Part of the GTM Account Research agent preset.

# Account SoT Sync

Prepare system-of-record changes from account research, then let the pinned agent apply only the exact user-confirmed fields.

## Setup
- Ask Notion DB or Google Sheet + field map on first use (multiple-choice widget for SoT choice).
- Adapters only: no lock-in beyond what they choose.

## Mid-job clarifying widgets
- "SoT target?" options: "Notion database" / "Google Sheet" / "Paste table" / "CSV file"
- "Change-plan mode?" options: "Draft append-notes change" / "Draft mapped-field changes + notes" / "Dry run only"
- "Conflict found" options: "Keep existing" / "Overwrite with new source" / "Flag both for me"

## Fallbacks
- If Notion and Sheets are not connected: offer (1) paste-ready markdown table, (2) CSV file to download/upload, or (3) keep findings in chat until they connect.
- Web-only research still produces the one-pager; SoT write waits or uses fallback.

## Apply gate
- Always show destination, canonical row, fields, old values when available, new values, and sources before asking for approval.
- The pinned agent applies only the exact confirmed change. A subagent never writes.

## Write rules
- Update only fields the user mapped and explicitly approved.
- Append Notes with date + source only after confirmation; do not overwrite history blindly.
- Flag conflicts between sources for human review.
- Never invent values to fill required fields; leave blank or unknown.

## Edge cases
- Schema drift (renamed columns): rediscover fields before write; ask with widget.
- Partial research: write only completed lanes; mark others pending.
- Duplicate account rows: ask which row is canonical before merge.

## Output
- Write receipt: fields touched, rows created/updated, conflicts flagged
- Or fallback artifact (markdown/CSV) with the same columns

## Rules
- Drafts/status only in Slack.
- Their artifact is SoT; never ship a creator file.

## Delegation contract

Any delegated portion of this skill follows `agent-orchestration`. Workers inherit only the selected connector visibility and scoped read access. They may return evidence, drafts, and change plans but cannot send, write, enable routines, create folders, or expand scope. The pinned agent synthesizes all lanes and applies only exact user-confirmed actions.
