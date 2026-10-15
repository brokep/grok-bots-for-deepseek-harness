---
name: routine-weekday-status-check-in
description: "Scheduled routine: Disabled by default. Weekdays at 9am in the user's timezone (the user can pick a different time or cadence). Runs one status pass across the workstreams, attaches a screenshot for every artifact it names, chases anything past its date once, and lists the gates waiting on the user. Quiet when nothing moved."
---

# Weekday status check-in

Part of the Project Manager agent preset.

Schedule, as written by the template author: Disabled by default. Weekdays at 9am in the user's timezone (the user can pick a different time or cadence). Runs one status pass across the workstreams, attaches a screenshot for every artifact it names, chases anything past its date once, and lists the gates waiting on the user. Quiet when nothing moved.

## What to do on each run

# Weekday status check-in

This routine ships disabled. Confirm timezone, the weekday 9am schedule, the destination, and that nothing gets merged, published, or spent before enabling.

When enabled:
1. Read /workspace/pm/state.md for GOAL, the plan summary, and the destination, then read /workspace/pm/plan.md and /workspace/pm/items.md for the work items. If the state file or the plan is missing, do nothing and say so once.
2. Run the check-in skill end to end: refresh what is readable, capture a screenshot for every artifact that changed, update statuses, and chase anything past its date once.
3. Deliver to the saved destination: one line per workstream, the blocked list, the gates waiting on the user, and the report from the html-report skill when anything changed.
4. List open gates here, never open a new one. A gate is asked in a live conversation, not by a scheduled message.
5. Stay quiet when nothing moved, nothing is newly blocked, and no gate is waiting. One line at most.
6. Never merge, publish, enable a campaign, spend, approve anything, or contact a customer.

Fires on:
- cron `0 9 * * 1-5`

Ask the importing user for:
- Timezone
