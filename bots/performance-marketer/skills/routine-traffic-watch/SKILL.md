---
name: routine-traffic-watch
description: "Scheduled routine: Disabled by default. Daily at 9am in the user's timezone. Reads every enabled campaign in the signed-in platform against its test plan and its spend cap, attaches the screenshots behind the numbers, pauses at the total cap, and says nothing at all when no campaign is enabled."
---

# Traffic watch

Part of the Performance Marketer agent preset.

Schedule, as written by the template author: Disabled by default. Daily at 9am in the user's timezone. Reads every enabled campaign in the signed-in platform against its test plan and its spend cap, attaches the screenshots behind the numbers, pauses at the total cap, and says nothing at all when no campaign is enabled.

## What to do on each run

# Traffic watch

This routine ships disabled. Confirm timezone, the daily 9am schedule, the destination, the total
spend cap, and that this routine never enables anything, before turning it on.

When enabled:
1. Read /workspace/ads/state.md for ACCOUNTS and the LAUNCHES lines: the enabled campaigns, their
   platforms, enable dates, daily budgets, total spend caps, checkpoint dates, and test
   thresholds. If that file is missing or no campaign is enabled, do nothing and say nothing.
2. Run the traffic-watch skill for each enabled campaign. Pull the numbers from the signed-in
   platform interface, and screenshot what they came from. If a session is logged out, say so once
   in this run, ask once for a fresh sign in, and do not retry anything. Do not repeat that ask on
   every later run, carry it in the next run's one line instead.
3. Deliver in this chat, or to the channel saved in setup: source and date, status and spend, per
   variant metrics, progress against the minimum clicks and minimum days, anything broken, and one
   recommendation. A 72 hour read is marked directional unless both thresholds are already met.
4. On a checkpoint date, compare spend to the total cap. At or over the cap, pause the campaign,
   screenshot the paused state, and report it in the same run.
5. Never enable a campaign, raise a budget, add a payment method, change a bid strategy, edit
   copy, or change targeting. Never run the launch-gate skill. Pausing to protect the cap is the
   only write this routine ever makes.
6. Stay quiet when nothing is enabled and when nothing changed since the last run.

Fires on:
- cron `0 9 * * *`

Ask the importing user for:
- Timezone
