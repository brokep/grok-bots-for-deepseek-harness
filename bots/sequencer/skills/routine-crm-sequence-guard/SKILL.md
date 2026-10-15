---
name: routine-crm-sequence-guard
description: "Scheduled routine: Disabled by default. Weekday evenings at 6pm in the user's timezone. Pauses tracker rows where the CRM shows the saved open-opportunity stage, so nobody gets a cold touch mid-deal. Quiet when nothing changed."
---

# CRM sequence guard

Part of the Sequencer agent preset.

Schedule, as written by the template author: Disabled by default. Weekday evenings at 6pm in the user's timezone. Pauses tracker rows where the CRM shows the saved open-opportunity stage, so nobody gets a cold touch mid-deal. Quiet when nothing changed.

## What to do on each run

# CRM sequence guard

This routine ships disabled. Before enabling, confirm the timezone, the weekday evening cadence, which CRM case applies, the ownership scope, the pause stage, the tracker, and the quiet-when-empty behaviour.

When enabled:
1. Read `/workspace/sequencer/state.md` for the CRM mapping, the pause stage, the owner filter, and the tracker reference. If no CRM is available, do nothing beyond one reminder that tracker-only manual pause rules are in effect.
2. For active rows that carry CRM ids, read the opportunity and stage fields through crm-adapter, using the discovered field names, never assumed labels.
3. Where the row is past the saved pause stage, set tracker status to paused, stop drafting for that row, and write the reason in notes.
4. Where a row was paused and the CRM now shows it clear, propose unpausing it. Do not unpause without a yes.
5. Post the paused list only when something changed.
6. Stay quiet if nothing changed.

This run is unattended. It reads the CRM and writes only to the tracker. It never writes to the CRM, never sends anything, and never invents stage data.

Fires on:
- cron `0 18 * * 1-5`

Ask the importing user for:
- Timezone
