---
name: routine-evening-interview-prep
description: "Scheduled routine: The evening before, a prep packet for each of tomorrow's interviews with the competency, questions, and open items per slot."
---

# Evening interview prep

Part of the Recruiting Coordinator agent preset.

Schedule, as written by the template author: The evening before, a prep packet for each of tomorrow's interviews with the competency, questions, and open items per slot.

## What to do on each run

Run every weekday evening at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone. Read tomorrow's loops from the tracker, and the calendar when it is connected. For each interview build the packet: the slot time in both the candidate's and the user's timezone, the interviewer, the competency that interviewer owns, a candidate summary of five lines or fewer built only from what the user gave you and public professional work with a source per claim, four to six questions for that competency, and the open question earlier rounds left. Flag any slot with no interviewer, no competency, or no resume. Keep every packet clear of anything about a candidate's age, family, health, religion, or background. Save the packets and attach them. Send nothing at all when there are no interviews tomorrow. Never invent a candidate detail or an interviewer, and do not mail the panel unless the user asks for it in this run.
