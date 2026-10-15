---
name: routine-top-prompt-spot-check
description: "Scheduled routine: Twice a week, re-runs the top five prompts and speaks up only when the user drops out of an answer or a new name shows up."
---

# Top prompt spot check

Part of the AI Search Visibility agent preset.

Schedule, as written by the template author: Twice a week, re-runs the top five prompts and speaks up only when the user drops out of an answer or a new name shows up.

## What to do on each run

Run twice a week on the two mornings the user picked, or Tuesday and Thursday when they did not pick, at the hour saved in memory and in their timezone. Compute the cron from that timezone. Read the prompt list and check only the five prompts marked top prompt. Compare each answer to the last capture. Send a message only when one of three things happened: the user dropped a rung, a name that was not in the last capture now appears, or an answer says something about the user that is wrong. Then send one short message with the prompt, what changed, the quoted sentence, the link, and one line on why it matters. Nothing changed means send nothing at all. Save the capture either way and write what you found to the spot check log so the weekly brief consolidates it instead of reporting it twice. Skip the citation audit and the scoreboard, the weekly brief covers those. Never invent a change or a quote, never score a reworded sentence with the same meaning as a change, and never post or email anything without an explicit yes.
