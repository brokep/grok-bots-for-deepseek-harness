---
name: routine-post-meeting-recap-draft
description: "Scheduled routine: After a meeting ends, drafts the recap from your notes and leaves it here for you to check."
---

# Post-meeting recap draft

Part of the Meeting Recap Deck agent preset.

Schedule, as written by the template author: After a meeting ends, drafts the recap from your notes and leaves it here for you to check.

## What to do on each run

Run on the hour through the user's working day on weekdays, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Check the calendar for meetings that ended since the last run with someone outside the user's company on them. For each one, look for the notes in the source saved in memory. Notes that have not synced yet mean wait for the next run instead of writing anything. When the notes are there, build the recap with the Build the recap deck skill and the saved template profile, then send one short message: the meeting, the date, the slide text, and the deck attached. Add one line on what was thin in the notes. Nothing that ended, or nothing with notes, means send nothing at all. Never draft from a calendar title alone, never invent a quote or a commitment, and never send, share, or publish the recap to anyone.
