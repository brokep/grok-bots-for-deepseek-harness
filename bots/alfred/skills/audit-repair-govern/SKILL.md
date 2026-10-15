---
name: audit-repair-govern
description: "Use this for a noisy or inaccurate Bot, stale Skill, failing Routine, duplicated Bots, unclear ownership, portfolio drift, permission drift, weak value, or a company change that may have made the Bot organization outdated."
---

# Audit, Repair & Govern

Part of the Alfred agent preset.

---
name: 'Audit, Repair & Govern'
description: >-
  Use this for a noisy or inaccurate Bot, stale Skill, failing Routine,
  duplicated Bots, unclear ownership, portfolio drift, permission drift, weak
  value, or a company change that may have made the Bot organization outdated.
---
# Audit, Repair & Govern

Diagnose and improve one Bot or the complete Bot portfolio.

## Single-item workflow

1. Inspect the current configuration and evidence.
2. Compare intended with actual behavior.
3. Identify likely root cause: wrong outcome, scope too broad, duplicated ownership, conflicting instructions, weak instructions, missing or stale source, connector failure, weak output contract, incorrect Skill, broad Routine trigger, incorrect schedule, missing retry or duplicate handling, wrong approval boundary, changed company workflow, or work that should not be automated.
4. Support the diagnosis with evidence.
5. Propose the smallest patch.
6. Show a before-and-after diff.
7. Preserve the prior configuration.
8. Define regression tests.
9. Stop for approval before any live change.

## Portfolio workflow

Review: durable outcome, human owner, usage, downstream value, human corrections, failures, sources, permissions, Skills, Routines, overlap, current relevance, last successful test, review age.

Classify components as: Keep, Improve, Merge, Reposition, Pause, Hide, Retire, Investigate, Create.

Return no more than three immediate portfolio actions.

Default new Bot recommendations to zero.

Never delete automatically. Hiding a Bot does not automatically pause its Routines or remove connectors, files, browser sessions, or credentials. Agents cannot be deleted by another agent; the user deletes from the sidebar.

## Output

For a single item: diagnosis with evidence, smallest patch, before/after diff, preserved prior config, regression tests, exact live change awaiting approval.

For a portfolio: health, value evidence, keep/improve/merge/reposition/pause/hide/retire recommendations, shared-Skill opportunities, source or permission risks, no more than three decisions, unknowns.

## Stop point

Stop before every live edit, pause, enable, hide, merge, retire, delete, permission change, or schedule change.
