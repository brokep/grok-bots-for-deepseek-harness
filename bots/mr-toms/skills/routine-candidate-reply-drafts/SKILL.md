---
name: routine-candidate-reply-drafts
description: "Scheduled routine: Through the workday, leaves an unsent draft reply for each new candidate email so the user only edits and sends."
---

# Candidate reply drafts

Part of the Recruiting Coordinator agent preset.

Schedule, as written by the template author: Through the workday, leaves an unsent draft reply for each new candidate email so the user only edits and sends.

## What to do on each run

Run a few times through the workday on weekdays, during the interview hours saved in memory, in the user's timezone. Compute the cron from that timezone. This one needs Gmail. Without it, stay quiet. Read candidate and interviewer mail that arrived since the last run. For each new thread that needs an answer, write a draft reply in the user's voice: three to five sentences, the specific next step, and a date to answer by. Scheduling replies use real times from the tracker, never times you made up. Leave every draft unsent and post one summary in chat listing the thread, the candidate, and a line on what the draft says. Never send, and never accept or move a time on the user's behalf. Do not draft a rejection or an offer, flag those for the user to ask for instead. Stay quiet when nothing new needs an answer.
