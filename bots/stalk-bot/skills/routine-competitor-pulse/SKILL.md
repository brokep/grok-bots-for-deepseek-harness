---
name: routine-competitor-pulse
description: "Scheduled routine: Disabled by default. Monday, Wednesday, Friday at 9am in the user's timezone (user can pick daily, weekly, or a custom cron). Runs every enabled module for every competitor and delivers the live brief with media, Against-us, For-our-site, Worth a decision, and Proactive suggestions. Quiet when nothing changed."
---

# Competitor pulse

Part of the Stalk Bot agent preset.

Schedule, as written by the template author: Disabled by default. Monday, Wednesday, Friday at 9am in the user's timezone (user can pick daily, weekly, or a custom cron). Runs every enabled module for every competitor and delivers the live brief with media, Against-us, For-our-site, Worth a decision, and Proactive suggestions. Quiet when nothing changed.

## What to do on each run

# Competitor pulse

This routine ships disabled. During setup I ask whether to turn it on, at what cadence (default Mon, Wed, Fri 9am, roughly every 2 days on weekdays), to what destination, and confirm the timezone.

When enabled:
1. Read memory for the baseline, the competitor list, each competitor's enabled modules, the destination, and the last pulse timestamp. If the baseline or competitor list is missing, do nothing and say so once.
2. Run the pulse skill.
3. Deliver to the saved destination with the pulse HTML report attached. If nothing changed, one line only and no report.
4. Update the last pulse timestamp.
5. Never post publicly, never contact anyone, never re-run product signups here.

Fires on:
- cron `0 9 * * 1,3,5`

Ask the importing user for:
- Timezone
