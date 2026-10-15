---
name: routine-weekly-x-recap
description: "Scheduled routine: Every Friday, pulls the week's briefs into the themes that held, the voices worth adding, the accounts that went quiet, and what to read this weekend."
---

# Weekly X recap

Part of the X Brief agent preset.

Schedule, as written by the template author: Every Friday, pulls the week's briefs into the themes that held, the voices worth adding, the accounts that went quiet, and what to read this weekend.

## What to do on each run

Run every Friday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the dated briefs from the last seven days instead of refetching the week, then top up with anything posted since the last brief. Write the recap in short sections. The date range and how many items you logged. Two to four themes that held all week, each with the two or three posts that carried it, a link on every line, and which way the argument moved. New voices, the accounts that showed up more than once and are not on the watch list, with one line on who they are and an offer to add them. Went quiet, the accounts on the list with nothing all week. Still open, the questions the field has not answered. Read this weekend, up to five links with one clause each. Save the recap dated, attach it, and deliver it to the destination they picked. A week with almost nothing gets three lines instead of a padded recap. Never invent a post, a quote, or a count, and never post or send anything without an explicit yes.
