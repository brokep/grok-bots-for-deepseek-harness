---
name: clip-pack-from-one-recording
description: "Use when the user wants several clips out of one talk, episode, or call in a single pass instead of picking them one at a time."
---

# Clip pack from one recording

Part of the Clip Bot agent preset.

Inputs: one recording, how many clips they want (5 to 10 is the useful range), and their shape and length prefs.

1. Transcribe first if there is no transcript, then run the moment finder end to end.
2. Show the ranked shortlist and take one round of edits. Do not render ten clips off your own taste.
3. Cut every approved moment with the cut skill. Post each clip as it finishes instead of holding them all to the end.
4. Build a contact sheet, one row per clip: number, hook line, timestamp range, length, and filename.
5. Write one line of post copy per clip, just enough to tell them apart. Full post text is the caption skill.
6. Finish with what you skipped and why, in two or three lines.

Output: the rendered clips, the contact sheet, and the updated clip log.

Fallbacks: a long recording that will take a while gets the shortlist inside the first minute and the renders as they land, never silence. Fewer strong moments than the number they asked for means you cut what is actually good and say why the rest did not make it.

Save under the clip library with the recording.
