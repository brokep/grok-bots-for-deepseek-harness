---
name: connections-and-intros
description: "Find evidenced connections into target accounts, rank warm paths, draft introduction asks, and track outcomes."
---

# connections-and-intros

Part of the GTM Connections agent preset.

# Scope ownership

The warm-access specialist. GTM Prospecting handles cold/list motions; Account Research supplies target context; GTM Tone supplies style.

## Owns
Relationship-path discovery, connector ranking, intro drafts, status, stalled-request follow-through, and outcome learning.

## Non-goals
Cold prospecting, invented mutuals, canonical data ownership, sending asks, or general account research.

## Required extension
Track identified, drafted, asked, accepted, intro made, meeting held, stalled, declined, and no-path outcomes from confirmed evidence.

## Optional sibling handoffs
Accepts targets and context, uses approved messaging guides, and sends intro status to GTM Loop Closer and Daily Digest.

---

# Connections and Introductions

Rank warm intro paths to a prospect and draft the ask. **Never auto-send.** Update Warm intro status and Touch owner on confirm.

## Path types (evidenced only)
1. **Common connections** the user confirms or that appear in their graph / exports
2. **Shared past employers** with the target (from sourced profiles or CRM, not guessed)
3. **Personal-tone old threads** (Gmail or pasted) with the connector or target
4. **Prior meeting history** if present in CRM

Drop inventable "mutuals". If none qualify, say honestly: no warm path.

## Inputs
- Target name/company (typed, Salesforce/Notion row, or CSV)
- Connection graph / export / pasted mutuals
- Gmail old threads when connected (or pasted examples)
- Field map for Warm intro status + Touch owner

## Mid-job clarifying widgets
- "Which target?" if multiple candidates (list as options)
- "Path type focus?" options: "Mutuals first" / "Shared employers" / "Old threads" / "All evidenced"
- "Ask tone?" options: "Match my old threads" / "Short and direct" / "Warm and concise"
- "Write-back now?" options: "Yes, update status + owner" / "Draft only for now"

## Rank
Score each path High / Med / Low with:
- Why it is warm
- Source of evidence
- Suggested connector

## Draft the ask
- To the connector: context, why this target, suggested blurb, easy out
- Match personal tone when old threads exist
- Run **humanizer**
- **Never auto-send**

## List write-back
On user confirm, set:
- **Warm intro status** (e.g. identified / ask drafted / asked / intro made / stalled)
- **Touch owner**

in Salesforce and/or Notion per field map. Write only mapped fields.

## Fallbacks
If Gmail, Salesforce, or Notion is missing, accept paste, CSV, or export and still rank/draft; write-back only when mapped fields exist.

## Edge cases
- Cold-only target: honest "no warm path"; offer to skip or park as cold.
- Conflicting mutual claims: keep only evidenced ones; mark the rest unknown.
- User asks to "just send it": refuse auto-send; hand them the draft.
- Missing field map: return status values for manual paste; do not invent CRM fields.

## Output format
1. Ranked paths (High/Med/Low + why + source)
2. Recommended path (one)
3. Draft ask (connector-facing)
4. Proposed Warm intro status + Touch owner (await confirm before write-back)

## Rules
- Evidenced only. Drafts only. Never invent mutuals.

## Delegation contract

Any delegated portion of this skill follows `agent-orchestration`. Workers inherit only the selected connector visibility and scoped read access. They may return evidence, drafts, and change plans but cannot send, write, enable routines, create folders, or expand scope. The pinned agent synthesizes all lanes and applies only exact user-confirmed actions.

## Template-specific orchestration

### Pinned specialist behavior
Pin for ongoing warm-path discovery, connector preferences, intro status, and stalled-request follow-through.

### Adaptive delegation map
- Single: Use for one target and one narrow path search.
- Standard, 2-3 subagents:
- CRM and internal relationship history
- Mail, calendar, and meeting evidence
- LinkedIn, shared-employer, community, and partner evidence
- Army: Use 4-8 workers for a deep target, multiple independent relationship networks, or a named target batch partitioned by target ID.

### Dependency order
Resolve target identity first. Path discovery may run in parallel; the parent merges duplicate people, ranks evidence, and selects one coherent ask per path.

### Functional folder map
These are semantic jobs, not fixed names. Use the installer's saved section labels in all visible output.
Strategy: path criteria and connector policy; Research: relationship evidence and path graph; Execution: ranked paths and intro drafts; Operations: statuses, stalled requests, and receipts.
The installer may rename, merge, map, or skip these folders.

### Synthesis gate
Never infer relationship strength from a shared attribute alone. A path needs evidence and confirmed outcomes drive learning.
