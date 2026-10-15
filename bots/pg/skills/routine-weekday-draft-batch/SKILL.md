---
name: routine-weekday-draft-batch
description: "Scheduled routine: Every weekday morning, researches the next few names on the target list and leaves a first-touch draft for each one, waiting on your yes."
---

# Weekday draft batch

Part of the Outbound Prospecting agent preset.

Schedule, as written by the template author: Every weekday morning, researches the next few names on the target list and leaves a first-touch draft for each one, waiting on your yes.

## What to do on each run

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Read the target list and take the next batch at the size they set, five by default. Prefer strong-fit rows that are new or enriched and have never been touched. Research each one on the public web first, then write the opening message on the channel they picked, holding to the no-invented-facts rule in the draft skill. Post the drafts in one message, each with its source links underneath and one line on what you left out. Set those rows to drafted and write the list back. Skip any row you could not verify and name it at the end with the reason. When there is nothing left worth drafting, say so in one line and name where the next ten names should come from. Never send, never message anyone, and never draft from a row you could not research.
