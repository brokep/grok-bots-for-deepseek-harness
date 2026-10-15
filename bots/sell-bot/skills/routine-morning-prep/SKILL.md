---
name: routine-morning-prep
description: "Scheduled routine: Disabled by default. Weekdays 7am: prep pages for today's watched calls."
---

# Morning prep

Part of the Sell Bot agent preset.

Schedule, as written by the template author: Disabled by default. Weekdays 7am: prep pages for today's watched calls.

## What to do on each run

This routine ships disabled. Before enabling, confirm the timezone and the calls to watch.

When enabled:
1. Read memory and setup.md in my folder (MY FOLDER fact). No fact, no file, or Morning prep not under Routines on: stop silently.
2. Find today's watched calls (a title pattern with an outside attendee, a known account's domain, or a call I booked), skipping canceled events and ignored domains. Add new ones to calls.csv. An unknown outside call gets one line asking whether to watch it.
3. Run @prep-page for calls with prep empty, and draft confirm notes now for calls the hourly check misses (before 7:55am or after 6:55pm).
4. One message: calls in time order, each with its 5 lines and page. No watched calls: quiet. Reads and drafts only.

Fires on:
- cron `0 7 * * 1-5`

Ask the importing user for:
- Timezone
