---
name: routine-post-event-recap-draft
description: "Scheduled routine: Two days after the event, drafts the recap from the trackers and asks for the three numbers it cannot know."
---

# Post-event recap draft

Part of the Event Producer agent preset.

Schedule, as written by the template author: Two days after the event, drafts the recap from the trackers and asks for the three numbers it cannot know.

## What to do on each run

Run two days after the event date at the hour the user picked, in the timezone saved in memory. Take the event date from the event brief and compute the cron from that date and timezone. Read the guest list, the vendor tracker, and the measures set in the brief. Draft the recap: the outcome against those measures, invited against registered against attended with the show rate, quoted against actual spend by category and the total against budget, what worked, what did not, and every follow-up that needs a message, skipping anyone who opted out. Then ask for the three things you cannot know: actual attendance, any spend that never hit the tracker, and how the room felt. Mark every number you are estimating rather than counting. Save the recap dated and attach it here. Never invent an attendance figure, a cost, or a quote. Do not send a thank you, a follow-up, or a survey from this run.
