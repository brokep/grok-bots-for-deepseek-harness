---
name: find-the-clippable-moments
description: "Use when a transcript exists and the user wants to know which parts of a recording are worth cutting into clips."
---

# Find the clippable moments

Part of the Clip Bot agent preset.

Inputs: the timestamped transcript, what the user records, and who the clips are for.

What is worth cutting: a claim someone would argue with, a number or a result stated plainly, a story with a turn in it, a crisp definition of something people get wrong, a real disagreement between speakers, a question answered in one breath, and any line that stands on its own with no setup. What to pass on: throat clearing, sponsor reads, logistics, anything needing three minutes of context, and anything where the speaker talks over themselves.

1. Read the whole transcript before you rank anything.
2. Pull candidate moments with a start and an end timestamp, both landing on a sentence boundary.
3. For each one write the hook line quoted exactly from the transcript, the start and end timestamp, the length in seconds, one line on why it works, and a score of strong, maybe, or skip.
4. Drop anything past the user's length preference unless the point needs the extra time. Say so when it does.
5. Rank strong first and show the top 8 in chat as a short list. Keep the rest in the moment list.
6. Ask one question, which ones to cut. Nothing else.

Output: the moment list with every candidate, and the top 8 in chat.

Fallbacks: a recording with nothing strong in it gets an honest answer, three maybes and a line on why the material is thin, instead of eight padded picks. No transcript means run the transcribe skill first.

Never move a timestamp to make a moment look better and never tidy a quote in the moment list. Save the moment list under the clip library with the recording.
