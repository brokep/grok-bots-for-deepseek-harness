---
name: workflow-automation-decision
description: "Use this for one workflow, recurring task, bottleneck, automation idea, proposed Bot responsibility, or candidate identified by organization discovery. Use before creating a new Bot, expanding an existing Bot, or creating a Routine."
---

# Workflow & Automation Decision

Part of the Alfred agent preset.

---
name: Workflow & Automation Decision
description: >-
  Use this for one workflow, recurring task, bottleneck, automation idea,
  proposed Bot responsibility, or candidate identified by organization
  discovery. Use before creating a new Bot, expanding an existing Bot, or
  creating a Routine.
---
# Workflow & Automation Decision

Decide how one recurring job should be handled. Use before creating a new Bot, materially expanding an existing Bot, or creating a Routine.

## Required inputs

- Desired outcome
- Current trigger, workflow, and owner
- Inputs and authoritative sources
- Decisions and exceptions
- Frequency and volume
- Current errors, delay, cost, or rework
- Output and recipient
- Existing Bots, Skills, Routines, and automation
- Failure consequences
- Approval requirements
- Success evidence

## Workflow

1. Establish the desired outcome.
2. Map trigger → inputs → steps → decisions → owner → handoffs → output → recipient → completion evidence.
3. Determine what currently goes wrong.
4. Determine whether the problem is material.
5. Check existing Bots, Skills, Routines, and automations for overlap.
6. Test whether the job recurs, the outcome is stable, a human owner exists, trusted inputs exist, output can be defined, success can be observed, exceptions can be bounded, and the workflow can be tested safely.
7. Choose exactly one primary recommendation from: no change; stop or simplify; clarify human ownership; repair process or source; deterministic automation; one-time AI assistance; human + AI; improve or merge an existing Bot; add a Skill; add a Routine to a proven workflow; create one new Bot.
8. Define the smallest safe pilot.
9. Identify evidence that could reverse the recommendation.

Use the smallest sufficient intervention. Default new Bot recommendations to zero.

A Routine becomes eligible only when: the manual workflow already worked; its trigger is stable; required sources are reliable; a human owner exists; output destination is known; missing-data, stale-data, retry, duplicate, and approval behavior are defined; a safe test succeeded.

Prefer a Skill instead of a new Bot when the parent Bot already owns the outcome and the work is one method inside that responsibility.

## Output

Return an Automation Decision Brief containing:

- Decision and confidence
- Business outcome
- Current workflow
- Root problem
- Evidence
- Selected architecture
- Why it is the smallest sufficient intervention
- Human accountable owner
- Scope and non-goals
- Risk and approval boundary
- Rejected alternatives
- Safe pilot
- Success evidence
- Assumptions and unknowns
- Next decision

## Stop point

Do not create or edit anything.

Stop for approval of the Automation Decision Brief. After approval, route to Grok Bot System Design if a Bot, Skill, or Routine must be designed.
