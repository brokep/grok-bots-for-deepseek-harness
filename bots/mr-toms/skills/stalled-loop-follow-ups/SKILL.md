---
name: stalled-loop-follow-ups
description: "Use when the user asks what is stuck, who owes them something, or wants nudges drafted for candidates, interviewers, or a hiring manager."
---

# Stalled loop follow-ups

Part of the Recruiting Coordinator agent preset.

Inputs: the tracker, plus anything the user pasted or forwarded since the last check.

What counts as stalled, unless the user set their own bar:
- A candidate waiting on feedback more than two business days after an interview
- A scorecard missing more than one day after the slot
- An offer out past the date the candidate was asked to answer by
- A scheduling request older than three days with no loop booked
- A candidate who has gone quiet after two touches
- An interviewer who has not accepted an invite inside 24 hours of the loop

Steps:
1. Re-read the tracker and fold in anything new first.
2. Group by who is holding it up: the user, an interviewer, the hiring manager, or the candidate. Sort each group oldest first.
3. One line per item: candidate, role, stage, days stuck, and the single action that unblocks it.
4. Draft the nudge for each one. Three to five sentences. Name the specific thing you need and a date to answer by. Keep candidate details out of anything headed for a group channel.
5. Update the tracker with the date you checked and a note that a follow-up is drafted.

Output: the grouped list, then the drafts ready to copy. Never send. With Gmail connected, leave each one as an unsent draft and say it is sitting there.

When the same item stalls twice, say so and raise it: name the person, the days lost, and what it is costing the loop.

Save under the hiring folder.
