---
name: event-spend-and-yes-rate
description: "Use when the user asks what they have spent on events, what they said yes to, how the period is tracking against the cap or budget, or wants a recap before a budget conversation."
---

# Event spend and yes rate

Part of the Event Request Desk agent preset.

Inputs: the queue, the rubric, the spend cap and the period budget saved in memory.

Steps:
1. Pick the window. Default is the quarter to date. The user can name any window and you use theirs.
2. Count what came in and what happened: asks received, yes, no, not now, needs info, still open, and the yes rate.
3. Add up committed spend. Fees and tier costs first, then travel, booth build, and swag when they were estimated on the row. Mark every estimate as an estimate and keep it out of the confirmed total.
4. Compare against the period budget when there is one. Show committed, estimated, and what is left, plus the events still ahead and what they will cost.
5. Break it down by type and by organizer, so a conference taking three separate slices is visible as one relationship.
6. List the highest-scoring asks that were declined, one line each on what a yes would have cost, so the user can argue for more budget with real rows.
7. Name the two or three patterns you can actually see, for example that speaking slots cost hours rather than dollars, or that one organizer is asking four times a quarter.

Output: a short table of the numbers, then three lines of read on what they mean. Under 250 words unless the user asks for the full row list.

Fallbacks: with Hex or Google Sheets connected, offer to push the table there. Without either, the recap lives in the chat and in the event desk folder. Never present an estimate as an invoice, and say plainly when a cost was never named on the original ask.

Save the recap with today's date in the event desk folder.
