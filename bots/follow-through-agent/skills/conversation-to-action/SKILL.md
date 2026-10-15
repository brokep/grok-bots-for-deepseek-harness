---
name: conversation-to-action
description: "Turn a meeting, thread, or note into assigned actions and approval-ready updates."
---

# conversation-to-action

Part of the GTM Loop Closer agent preset.

# Conversation to Action

Confirm the artifact, extract explicit decisions and commitments, ask about missing owners or destinations, map each item to a reply, CRM update, task, calendar hold, workspace record, or no action, then show a dry-run change plan. Create drafts only. Return a receipt with Drafted, Applied, Skipped, Blocked, or Unknown per item.

## Delegation contract

Any delegated portion of this skill follows `agent-orchestration`. Workers inherit only the selected connector visibility and scoped read access. They may return evidence, drafts, and change plans but cannot send, write, enable routines, create folders, or expand scope. The pinned agent synthesizes all lanes and applies only exact user-confirmed actions.
