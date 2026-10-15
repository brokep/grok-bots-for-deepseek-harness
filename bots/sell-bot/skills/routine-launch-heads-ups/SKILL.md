---
name: routine-launch-heads-ups
description: "Scheduled routine: Disabled by default. Weekdays 10:10am and 3:10pm: launches matched to customers who asked."
---

# Launch heads-ups

Part of the Sell Bot agent preset.

Schedule, as written by the template author: Disabled by default. Weekdays 10:10am and 3:10pm: launches matched to customers who asked.

## What to do on each run

This routine ships disabled. Before enabling, confirm the timezone and the Slack channels or changelog page for launches.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Launch heads-ups not under Routines on: stop silently.
2. No launch channels: stop. Read launch posts since the launches line under Last checks, with the Slack connector (read only) or from the changelog page.
3. Match each to open asks in requests.csv and draft heads-ups per Fixes and launches in @support-desk.
4. Update the launches line. One message: launches matched and drafts created. No match: quiet. Drafts only. Never post in Slack.

Fires on:
- cron `10 10,15 * * 1-5`

Ask the importing user for:
- Timezone
