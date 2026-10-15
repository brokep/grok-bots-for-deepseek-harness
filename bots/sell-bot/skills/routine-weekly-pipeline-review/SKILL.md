---
name: routine-weekly-pipeline-review
description: "Scheduled routine: Disabled by default. Mondays 9am: stalled deals, overdue touches, and nudges."
---

# Weekly pipeline review

Part of the Sell Bot agent preset.

Schedule, as written by the template author: Disabled by default. Mondays 9am: stalled deals, overdue touches, and nudges.

## What to do on each run

This routine ships disabled. Before enabling, confirm the timezone and the follow-up spacing.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Weekly pipeline review not under Routines on: stop silently.
2. From pipeline.csv: counts by stage, deals unmoved for 14 days, overdue next touches, proposals waiting over 5 days, open expansion deals, and prospects to propose as lost.
3. Draft a nudge per overdue prospect with something new and no open draft, per @draft-email. Check posts for the rest per @watch-on-x.
4. One message: the counts, stalled, overdue, and propose-lost lists, then the drafts. Nothing to report: quiet. Drafts only.

Fires on:
- cron `0 9 * * 1`

Ask the importing user for:
- Timezone
