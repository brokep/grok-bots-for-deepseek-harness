---
name: routine-friday-stage-audit
description: "Scheduled routine: Every Friday afternoon, audit each of the owner's opportunities that was created or moved stage this week against the qualification framework and stage the CRM updates."
---

# Friday stage audit

Part of the Deal Inspector agent preset.

Schedule, as written by the template author: Every Friday afternoon, audit each of the owner's opportunities that was created or moved stage this week against the qualification framework and stage the CRM updates.

## What to do on each run

# Friday stage audit

Runs unattended on Fridays at 16:00 in the owner's timezone.

1. List the owner's opportunities created or moved to a later stage since the last run (from the CRM stage history). Skip closed-won and closed-lost.
2. Run `stage-gate-audit` on each. Cap at ten per run, highest amount first, and list the rest by name.
3. Run `crm-writeback` to build the diff for each audit. Apply nothing.
4. Deliver one message to the owner (and the manager only if memory says so): a summary table (Opportunity, Stage, Verdict, Top gap), then each scorecard, then the diffs, ending with "Apply the CRM changes? Name the deals or say all."
5. If no recorder has calls for a deal, report it as Insufficient Data with the questions the next call must answer.

Unattended runs never write to the CRM and never ask clarifying questions; they label uncertainty and move on.

## Schedule

Create this routine paused, on cron `0 16 * * 5` read in the owner's timezone.
That is the default; if the owner named a different day or hour while setting up,
use theirs instead. Turn it on only when the owner says yes.
