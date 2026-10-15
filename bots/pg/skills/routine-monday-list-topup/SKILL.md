---
name: routine-monday-list-topup
description: "Scheduled routine: Every Monday, adds new companies and named people that match your ideal customer so the list never runs dry."
---

# Monday list top-up

Part of the Outbound Prospecting agent preset.

Schedule, as written by the template author: Every Monday, adds new companies and named people that match your ideal customer so the list never runs dry.

## What to do on each run

Run every Monday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read the target list first and count the untouched strong-fit rows. When more than two weeks of names are still waiting at the current pace, say that in one line and add nothing. Otherwise find ten companies on the public web that match the ideal customer saved in memory, score each strong, maybe, or weak with one line of reason, and add the strong ones with one or two named people each. Confirm every title on a public page and leave it blank when you cannot. Deduplicate against every row already on the list, against the do-not-contact list, and against anyone marked a customer, an open deal, or a no. Post what you added with the fit reason and the source for each company, then name what you skipped and why. Never guess a contact, never draft in this run, and never send anything.
