---
name: routine-friday-week-ahead
description: "Scheduled routine: Disabled by default. Fridays at 4pm in the user's timezone. Lists what is due in the next 7 days, what the user has to decide to keep the date, and what is already late, read from the plan and the work items. Quiet when nothing is due and nothing is late."
---

# Friday week ahead

Part of the Project Manager agent preset.

Schedule, as written by the template author: Disabled by default. Fridays at 4pm in the user's timezone. Lists what is due in the next 7 days, what the user has to decide to keep the date, and what is already late, read from the plan and the work items. Quiet when nothing is due and nothing is late.

## What to do on each run

# Friday week ahead

This routine ships disabled. Confirm timezone, the Friday 4pm schedule, and the destination before enabling.

When enabled:
1. Read /workspace/pm/state.md for GOAL and the plan summary, then read /workspace/pm/plan.md and /workspace/pm/items.md. If the state file or the plan is missing, do nothing and say so once.
2. List what is due in the next 7 days, one line each with owner and date, critical path items first.
3. List every decision the user has to make next week to keep the date: which gate is expected, on what date, and what will be waiting for them. Do not open a gate here.
4. List anything already late, with the days late and who owns it.
5. Recompute the days remaining and say in one line whether the date is still reachable, with the arithmetic.
6. Deliver to the saved destination in under 15 lines. No report unless the user asks for one.
7. Stay quiet when nothing is due, nothing is late, and no gate is expected.
8. Never merge, publish, enable a campaign, spend, or approve anything.

Fires on:
- cron `0 16 * * 5`

Ask the importing user for:
- Timezone
