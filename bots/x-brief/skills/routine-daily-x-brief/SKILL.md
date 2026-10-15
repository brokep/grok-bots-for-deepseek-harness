---
name: routine-daily-x-brief
description: "Scheduled routine: Once a day at the hour you pick, reads your watch list and sends the day's items grouped by theme with a link on every line."
---

# Daily X brief

Part of the X Brief agent preset.

Schedule, as written by the template author: Once a day at the hour you pick, reads your watch list and sends the day's items grouped by theme with a link on every line.

## What to do on each run

Run once a day at the hour the user picked, on the days they picked, weekdays by default, in the timezone saved in memory. Compute the cron from that timezone. Read the watch list and the seen log first, then fetch every account and search on the list for the window since the last brief, through the X connector when it is connected and through public pages when it is not. Keep only what clears the signal bar in the Daily X brief skill, or the user's own bar when they set one, and cap the brief at 12 items. Use the shape that skill defines: the count line, the one thing that matters most and why, two to four named themes with one line per item ending in the link and the local time, what the field is arguing about, up to three things worth reading in full, the quiet accounts, and anything you could not open. Log every reported link so tomorrow never repeats it. Save it dated, attach it, and deliver it to the destination they picked. A day with nothing that clears the bar gets one line saying it was quiet. Never invent a post, a quote, a handle, or an engagement count, and never post, reply, like, or DM from this run.
