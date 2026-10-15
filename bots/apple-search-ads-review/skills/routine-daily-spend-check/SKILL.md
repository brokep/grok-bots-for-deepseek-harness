---
name: routine-daily-spend-check
description: "Scheduled routine: Each weekday morning, checks for a new export and speaks up only about groups over target or spending with nothing to show."
---

# Daily spend check

Part of the Apple Search Ads Review agent preset.

Schedule, as written by the template author: Each weekday morning, checks for a new export and speaks up only about groups over target or spending with nothing to show.

## What to do on each run

Run once each weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Look for a new export: a file the user dropped in, a connected sheet, or a warehouse query if one is set up. Nothing new means send nothing at all. With a new export, read the targets sheet and compare the newest range against it. Send one short message only when something needs a person: a group past its tolerance band, a keyword or campaign with spend and zero installs, a daily cap spent out before the day ended, or a cost per install that jumped further than that group's normal daily swing. One line each with the campaign or keyword, the number, the target, and the money involved. Nothing over the line means stay quiet. Do not write a full review here, the weekly one covers trends. Say when a day is too thin to judge instead of ringing an alarm. Never invent a number and never edit the ad account.
