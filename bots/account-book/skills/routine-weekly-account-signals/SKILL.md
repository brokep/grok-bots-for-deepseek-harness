---
name: routine-weekly-account-signals
description: "Scheduled routine: Every Monday morning, checks your accounts for public news, funding, leadership, and hiring signals, and reports only what matters to the deal."
---

# Weekly account signals

Part of the Account Research Desk agent preset.

Schedule, as written by the template author: Every Monday morning, checks your accounts for public news, funding, leadership, and hiring signals, and reports only what matters to the deal.

## What to do on each run

Run every Monday at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the account list and every account file, including the date of the last check. When the list is tiered, check the weekly accounts every run and the monthly ones on the first run of the month. Check each company's own newsroom, blog, and careers page first, then the open web for anything published since that date. Keep only what clears the signal bar in the Account signals refresh skill, plus anything the user asked you to always flag. Write one line per signal with the account, what happened, the date, the source URL, and one plain line on what it means for that deal. Group by account, newest first, and end with one line naming the accounts with nothing new. Call out any signal that should change an account plan, and name the part it changes. Save every signal dated into the account file. A week with nothing across the whole list gets one line saying it was quiet and no summary. Never invent news, a number, a quote, or a date, and never post or send this anywhere without an explicit yes.
