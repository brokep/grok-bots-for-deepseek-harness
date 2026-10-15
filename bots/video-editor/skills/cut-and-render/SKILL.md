---
name: cut-and-render
description: "Use after the user approves an edit plan, and for every revision: cuts, syncs, captions, mixes, renders, and delivers."
---

# cut-and-render

Part of the Video Editor agent preset.

# Cut and render

## When to use
After the user approves the edit plan, and for every revision.

## Inputs
The approved plan, the chosen takes, the SETUP fact, and the video assets folder. Tools per video-tools.

## Steps
1. Join the A-roll as re-encoded, frame-accurate segments. Never use stream-copy concat or cut with an fps filter, which pushes first frames late and causes growing drift.
2. Cut before the speaker's eyes glance away from the camera, and end the video when they finish talking: no hand over the camera, frozen, or black frames at the end.
3. Camera audio can run 60 to 115 ms late against the lips (mic delay). Measure lip sync on this video (SyncNet, or the fallback in video-tools) and correct it.
4. Captions come from a transcript of the cut and match what was said, in the user's font, with key words in their highlight color.
5. B-roll and graphics as planned, in the style the plan named. Graphics in Remotion.
6. Keep the music bed quiet, roughly 12 to 15 LU below the voice. About 7 to 9 LU under is too loud. Master to -14 LUFS integrated and -2 dBTP max.
7. Render H.264, 1080x1920, 30 fps, AAC, faststart.
8. Run delivery-check and fix every fail before delivering.
9. Deliver to the delivery spot in SETUP: a Google Drive preview link, their computer, or a download in this chat. Keep only the newest version of each video in the delivery folder and delete the previous version once the new one is verified. File new assets in the video assets folder and add them to its index.

## Revisions
For small text fixes to an already-rendered edit (caption wording, overlay labels), change only the on-screen text on the existing video instead of re-cutting segments. Bigger changes go back through edit-plan.

## Never
Post or publish anything. Touch the raw footage.
