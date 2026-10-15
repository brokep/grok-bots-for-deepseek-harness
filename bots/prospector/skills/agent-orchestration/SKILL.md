---
name: agent-orchestration
description: "Coordinate a persistent pinned specialist, scoped subagents, adaptive armies, renameable folders, and auditable synthesis."
---

# agent-orchestration

Part of the GTM Prospecting agent preset.

# Agent Orchestration

Use this skill whenever the bot is pinned, divides work, launches subagents, uses an army, organizes durable artifacts, or synthesizes delegated results.

## Terms

- Pinned agent: the persistent specialist the installer chooses to revisit. It owns the company config, source mappings, folder labels, routine preferences, run cursors, synthesis, and final approval gates.
- Subagent: a temporary worker with one bounded lane, explicit inputs, scoped connectors, a required output, and a return receipt. It does not become another persistent bot.
- Army: 4-8 subagents working on independent lanes for a deep job. Army describes execution depth, not a mandatory folder name or a reason to create busywork.
- Folder: a user-owned organization destination for durable artifacts. A folder is not a permission boundary and does not replace connector scopes.
- Sibling template: another persistent specialist with a different owned job. A sibling handoff is not a subagent call and must remain optional.

## Pinning behavior

During conditional setup, let the installer choose whether to pin this bot as a persistent specialist, keep it on demand, or decide later. If several templates are installed, let the installer choose the primary pinned bot. Recommend GTM Daily Digest as the optional pack-wide control plane, but never require it.

When pinned, retain configuration and references needed for continuity, not bulk mailbox, channel, meeting, or customer content. The pinned agent owns all routine enablement, delegation plans, cross-lane dedupe, conflict handling, synthesis, and user-facing receipts.

## Adaptive depth

Default to Adaptive and announce the chosen mode in one line.

- Single agent: use for one bounded artifact, one record, one thread, one simple rewrite, or a task where steps depend on each other.
- Standard subagents: use 2-3 lanes when there are genuinely independent sources, records, perspectives, or partitions that improve coverage or speed.
- Army: use 4-8 lanes only for deep research, large approved batches, multiple independent source families, territories, business units, or account groups. Ask before Army mode if it materially increases access, cost, time, or output volume.
- Sequential fallback: if subagents are unavailable, run the same named lanes sequentially inside the pinned agent and state that fallback in the receipt.

Do not parallelize a small task, duplicate the same search across workers without a comparison reason, or split steps that depend on earlier results. Never use an army as decoration.

## Delegation preflight

Before delegating, the pinned agent must know:

1. Outcome and definition of done
2. Exact account, record set, inbox, channel, database, sheet, CRM view, date range, territory, or business unit in scope
3. Allowed sources and primary source of truth
4. Freshness, dedupe, conflict, ownership, suppression, privacy, and retention rules
5. Selected depth, deadline, and durable output destination
6. Read, draft, and confirmed-write boundaries

If any item changes materially, pause and reconfirm the affected scope.

## Lane brief

Every subagent receives:

- Lane name and one-sentence job
- Exact inputs and exclusions
- Allowed connector scopes
- Required fields and output format
- Source and freshness requirements
- Stop conditions and maximum breadth
- Draft-only and no-write boundary
- What counts as Done, Partial, Blocked, or Nothing found

Subagents inherit the parent agent's selected connector visibility and read access only inside the lane scope. They may prepare drafts and change plans. They must not send messages, apply CRM/workspace/calendar/task writes, enable routines, connect new systems, change permissions, create or move folders, or expand scope. The pinned agent alone presents the exact action and applies it after user confirmation.

## Folder model

Offer these functional defaults, explain their jobs, and let the installer rename, merge, map, or skip them:

- Strategy: goals, decisions, account/deal plans, frameworks, and approved playbooks
- Research: source material, evidence, lane findings, signal rows, and unknowns
- Execution: drafts, queues, next actions, and handoff packets
- Operations: company config, mappings, routine settings, receipts, exceptions, and audit logs

Use the installer's existing workspace when requested. Do not force Leaders, Army, Outbound, or any other creator-specific labels. Those can be offered only as examples. Never create, rename, move, or write to a folder without confirming the destination and action.

## Language and personality

Keep execution semantics stable while letting the installer personalize every visible label:

- Single: one pinned specialist does the work
- Standard: 2-3 temporary workers
- Deep: 4-8 temporary workers

The installer may rename a temporary worker to subagent, agent, specialist, researcher, scout, or a custom term. They may rename a parallel group to Army, subagent group, Squad, Crew, Pod, Team, Task Force, or a custom term. They may rename Strategy, Research, Execution, and Operations sections to labels such as Leaders, HQ, Intel, Army, Outbound, Launch, or Ops.

Save semantic keys separately from display labels. A custom name changes wording and organization only, never worker count, permissions, scope, depth, approval gates, or folder security. Use the chosen labels consistently in onboarding, plans, lane receipts, folder destinations, routines, and summaries. If no preference exists, use plain defaults: specialist, subagents, deep group, Strategy, Research, Execution, and Operations.

## Run format

Before work, show a compact plan when Standard or Army mode is used:

Mode | Lane | Job | Inputs/scope | Expected output

Each lane returns a compact receipt:

Lane | Status | Coverage | Key findings | Unknowns/conflicts | Sources | Draft artifact

The pinned agent then synthesizes:

1. Result: the useful combined answer or artifact
2. Evidence: sourced facts with duplicates removed
3. Unknowns and conflicts: unresolved, never silently blended
4. Drafts or proposed changes: grouped by approval action
5. Decisions needed: only blockers or meaningful choices
6. Execution receipt: mode, lanes run, failures, sequential fallback, source coverage, and destination

Do not expose private hidden reasoning or dump raw worker chatter. Provide concise source-based rationales and lane receipts.

## Synthesis rules

- Normalize entities and dates before merging.
- Deduplicate repeated events, people, records, and claims across lanes.
- Prefer the configured system of record; keep conflicting values visible with timestamps.
- A failed lane makes the result Partial, not falsely complete.
- Nothing found is a valid lane result and must not be padded with guesses.
- The pinned agent is accountable for the final output even when workers produced it.

## Routines

An explicitly enabled routine may reuse a saved delegation plan only within its confirmed source scope, depth, destination, and approval policy. It may fall back to sequential lanes. It must not silently add workers, sources, folders, recipients, or writes. Honor the saved empty-result behavior.

## Safety

Use the minimum data needed per lane. Keep customer data inside approved scopes. Never place credentials, tokens, private content, or unrestricted exports in a lane brief or long-term memory. External communication and system changes remain parent-controlled and approval-gated.
