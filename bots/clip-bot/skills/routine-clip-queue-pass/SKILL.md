---
name: routine-clip-queue-pass
description: "Scheduled routine: Every weekday morning, transcribes any new recording waiting in the clip queue and comes back with the moments worth cutting."
---

# Clip queue pass

Part of the Clip Bot agent preset.

Schedule, as written by the template author: Every weekday morning, transcribes any new recording waiting in the clip queue and comes back with the moments worth cutting.

## What to do on each run

Run every weekday morning at the hour the user picked, in the timezone saved in memory. Compute the cron from that timezone and never assume Pacific or UTC. Check the clip queue for recordings added since the last run. Nothing new means send nothing at all. For each new recording, transcribe it with timestamps, then run the moment finder and post one message: the recording name, its length, the top five moments with the hook line quoted exactly, the timestamp range, and the length in seconds, then one question, which ones to cut. Do not render anything on your own. Save the transcript and the moment list with the recording and mark it processed so the next run skips it. Name any recording you could not open or hear and say why in one line. Never invent a quote or a timestamp, and never publish or upload a clip.
