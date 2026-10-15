---
name: cut-a-clip
description: "Use when the user picks a moment or gives you a timestamp range and wants the actual short clip file with captions."
---

# Cut a clip

Part of the Clip Bot agent preset.

Inputs: the source recording, a start and end timestamp, and the user's clip shape, length, and caption preference.

1. Read the range back in one line with the quoted first sentence, so a wrong pick gets caught before the render.
2. Trim on sentence boundaries and leave about half a second of air at each end. Never clip a word in half.
3. Reframe to the shape they picked. Vertical crops to whoever is speaking. When a wide shot holds two people and a crop would cut someone out, keep the full frame on a padded background and say that is what you did.
4. Burn in captions word by word from the transcript, high contrast, inside the safe area, two lines at most. Ship the subtitle file next to the clip either way.
5. Add a source card when the user wants one: the show or talk name, the speaker, and the timestamp it came from.
6. Render, check the file plays and the length matches, then attach it here with the timestamp range and a one-line description.

Output: the clip file, the subtitle file, and a row in the clip log with the source, the range, the shape, and the date.

Fallbacks: an audio-only source gets a captioned waveform or a static card with the speaker name. A failed render gets the reason in plain words and one alternative, a shorter range or a different shape, never a silent retry loop.

Save under the clip library with the recording and mark the moment as cut in the moment list.
