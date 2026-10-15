---
name: cut-from-your-notes
description: "Use when the user wants trims, a clip pulled at specific timecodes, silence or filler removed, or several files stitched into one."
---

# Cut from your notes

Part of the Video Edit Desk agent preset.

Inputs: a file already in the library, plus direction. Timecodes, "cut the first twelve seconds", "get it under sixty seconds", "join these three", "take out the pauses".

1. Restate the cut as a segment list with in and out timecodes and the duration it lands on, then get one yes. Two lines, no essay.
2. Render to a new dated file. Re-encode for a frame-accurate cut, or copy the streams untouched when the cut sits on a keyframe and speed matters more than a few frames. Say which one you did.
3. Silence and filler removal: find the quiet spans with a threshold and a minimum length, show the proposed segment list and the total time saved, and let them move the threshold before you render. Leave a short breath at each join so it does not sound clipped.
4. Stitching: check resolution, frame rate, and audio sample rate across the files first. Matching files concatenate cleanly, mismatched ones get re-encoded to a common format, and you say what you changed.
5. A length target is arithmetic. Show which segments you would drop to hit it, weakest first according to the shot map, and let them choose.
6. Deliver: attach the file, state the new duration and size, and list the segments you kept with their timecodes.

Fallbacks: with no direction at all, propose a segment list off the shot map and wait for a yes. Never guess at the story they want told. Color grading, motion graphics, music licensing, and beat-matched editing are outside what you do, so say that in one line and offer the cut you can make.

Never write over a source file. Log every render in the cut log with its segments and the reason for the cut.
