---
name: open-loop-audit
description: "Find explicit commitments and information that lack a completed destination or owner."
---

# open-loop-audit

Part of the GTM Loop Closer agent preset.

# Open-Loop Audit

A loop needs sourced evidence of an ask, commitment, decision, question, promised follow-up, or information that should be recorded, plus evidence that the required action or destination is still missing. Unread or old alone does not prove an open loop.

1. Pull changed artifacts inside approved CRM, mailbox, calendar, Slack/Teams, notes, and task scopes.
2. Extract explicit asks, commitments, decisions, dates, owners, and destinations.
3. Reconcile against CRM activity, tasks, sent mail, calendar, and workspace records.
4. Deduplicate the same loop across sources.
5. Classify Open, Drafted, Waiting, Blocked, Closed, or Unknown.
6. Return evidence, missing destination, proposed owner, due state, closure action, and source.

Never infer promises, owners, deadlines, or completion.

## Delegation contract

Any delegated portion of this skill follows `agent-orchestration`. Workers inherit only the selected connector visibility and scoped read access. They may return evidence, drafts, and change plans but cannot send, write, enable routines, create folders, or expand scope. The pinned agent synthesizes all lanes and applies only exact user-confirmed actions.

## Template-specific orchestration

### Pinned specialist behavior
Pin for continuous cross-system commitment reconciliation and ownership of the open-loop queue.

### Adaptive delegation map
- Single: Use for one meeting, thread, commitment, or customer fact.
- Standard, 2-3 subagents:
- Meetings and explicit commitments
- Inbox and Slack asks or promised follow-ups
- CRM, task, calendar, and workspace completion evidence
- Army: Use 4-8 workers only for named teams, account groups, or time windows partitioned without overlapping loops.

### Dependency order
Normalize people, accounts, dates, and destination systems before synthesis. The parent deduplicates the same loop across sources and owns closure state.

### Functional folder map
These are semantic jobs, not fixed names. Use the installer's saved section labels in all visible output.
Strategy: follow-through policy and ownership rules; Research: commitment evidence; Execution: loop queue and closure drafts; Operations: statuses, destinations, and receipts.
The installer may rename, merge, map, or skip these folders.

### Synthesis gate
Unread, old, or missing fields alone do not prove an open loop. Only sourced commitments or required destinations qualify.
