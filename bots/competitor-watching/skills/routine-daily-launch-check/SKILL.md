---
name: routine-daily-launch-check
description: "Scheduled routine: Each weekday morning, checks changelog, release note, and blog pages across the watch list and speaks up only when a competitor ships something."
---

# Daily launch check

Part of the Competitor Watch agent preset.

Schedule, as written by the template author: Each weekday morning, checks changelog, release note, and blog pages across the watch list and speaks up only when a competitor ships something.

## What to do on each run

Run once each weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the watch list and check only the changelog, release note, and blog pages on it. Compare each to the saved copy from the last check. When a competitor has shipped or announced something, send one short message: the competitor, what shipped, the source URL, the date, and one line on why it matters to this user. Nothing new means send nothing at all. Write what you found to the launch log so the weekly brief consolidates it instead of reporting it twice, and save the new snapshot either way. Skip pricing, product, and careers pages, the weekly brief covers those. Never invent a launch, never infer one from a job post or a rumor, and never post or email anything without an explicit yes.
