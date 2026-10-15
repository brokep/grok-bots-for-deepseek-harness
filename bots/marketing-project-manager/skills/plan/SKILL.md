---
name: plan
description: "Use when building or changing the plan: turning a goal and a date into workstreams with a deliverable, an owner, a due date, a dependency, and the gate each one needs. Holds the backwards schedule, the critical path rule, the work item ledger format, and the plan file layout."
---

# plan

Part of the Project Manager agent preset.

# Plan

One goal, one date, five workstreams, one file that is the truth.

## When to use
At setup, when the goal or the date changes, when a workstream is added or cut, and whenever the
work items and the plan file disagree.

## Inputs
The goal and the date from the user. Whatever the tracker, the shared drive folder, or a paste
already contains. The teammate roles found. No connector is required. With nothing connected, the
plan is built from what the user said and what the site shows.

## The five default workstreams
1. Research: what the market and the competitors already say. Deliverable: a research brief with
   sources and dates. Gate: none.
2. Positioning: the claim, the audience, the proof, plus the messaging angles that are approved
   and the ones that are ruled out. Deliverable: a positioning document. Gate: sign-off, before
   anything public uses the claim.
3. Landing page: the page itself. Deliverable: the page change proposed as a pull request with a
   preview link. Gate: merge.
4. Ads: the campaign shells and the copy. Deliverable: a review document of copy variants, then
   paused campaigns that nobody enables. Gate: spend, covering create, enable, and any budget
   raise.
5. Analytics: how the launch is measured. Deliverable: the metric list, where each number comes
   from, and the report shape. Gate: none.

Cut a workstream the goal does not need. Add one it does need, for example a docs update or a
partner announcement. Every added workstream carries the same five fields.

Ads and analytics have no connector, so their inputs are exports: a CSV in the shared drive
folder, a spreadsheet the user names, or a paste. Say which one is in use and the date it was
read.

## Schedule backwards from the date
1. Put the date on the wall. Count working days to it.
2. Order the chain: research precedes positioning, positioning precedes page copy and ad copy, ad
   copy is ready before the page merges, the page merges before any campaign is enabled, and
   analytics is in place before launch, not after.
3. Give each workstream a due date that leaves room for the gate ahead of it. A gate takes at
   least one working day of the user's time and can take longer.
4. Mark the critical path: the chain where a slip moves the launch date. Say which chain it is in
   one line.
5. When the arithmetic does not fit, say so in one line with the number of days short, and offer
   the two options that exist: move the date, or cut scope. Never quietly compress a gate.

## Work item ledger
/workspace/pm/items.md, one line per item, newest change first:

`<id> | <workstream> | <deliverable in 8 words> | owner: <you or a teammate role> | due:
<YYYY-MM-DD> | depends: <id or none> | gate: <merge, spend, sign-off, or none> | status: <not
started, in progress, blocked, waiting on you, done> | artifact: <path, link, or none>`

Rules: one owner per item, never two. One date per item, never a range. The owner defaults to the
user when no teammate does that job. Status blocked always names what it is blocked on and since
when. An item cannot be done while its artifact is none.

## Plan file
/workspace/pm/plan.md holds the goal in the user's words, the date, days remaining, the
workstreams with their five fields, the critical path line, the gate calendar (which gate is
expected on which date), and a dated changelog of every plan change with who asked for it.

## State file
/workspace/pm/state.md holds the setup state, one labeled line each: the current STATE pointer
text on line one, then GOAL, PLAN, DESTINATION, TEAMMATES. The work items stay in items.md.
Rewrite the PLAN line after every plan change: goal, date, workstream count, the next gate and
its date, and the path to the file. Keep it under 480 characters. plan.md is the truth,
state.md is the index, and memory holds one STATE pointer fact. When a plan change makes that
pointer wrong, forget the old fact with its exact text, write the new one, and keep its exact
text as the first line of state.md.

## Output
The timeline in chat: one line per workstream with owner and date, the critical path in one line,
the next gate and when it is expected, and anything already late. Then the file path.

## Never
Invent a date the user did not agree to. Move a date without saying what moved and why. Assign an
owner that does not exist. Let plan.md and items.md disagree after a change. Compress or skip a
gate to make the arithmetic work.
