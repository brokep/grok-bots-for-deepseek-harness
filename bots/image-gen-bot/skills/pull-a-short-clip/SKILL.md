---
name: pull-a-short-clip
description: "Use when the user names a time range in a recording and wants a clip, a silent loop, or a GIF out of it."
---

# Pull a short clip

Part of the Stills & Clips Desk agent preset.

Inputs: the file, a start and an end (or "about ten seconds around this"), and where the clip plays.

1. Confirm the range back with the in and out timecodes and the duration before you render anything.
2. Add a beat on each end, about a third of a second, so the clip does not start or stop mid-motion. Ask first if that pushes past the range they named.
3. Cut from the original file, not from a copy you already re-encoded. Keep the audio when someone is talking, mute it when the clip is there to show motion.
4. Loop check when they asked for a loop: the first and last frame have to match closely enough that the wrap does not read as a jump. Say plainly when the range cannot loop and offer the nearest range that can.
5. Render the shapes the size sheet calls for: 16:9 for a site or a doc, 1:1 and 9:16 for feeds, plus a GIF or a WebP under the weight limit for anything embedded in docs or mail. Give the duration and the file weight for each one, and say when a long range makes a file too heavy for where it is going.
6. Cut the range they named. They know their footage, so do not talk them down to a shorter one. When the ask is really an edit, several ranges stitched together with captions burned in, say that plainly and offer the strongest single range instead.
7. Hand the result to Export sizes, captions, and alt text.

Fallbacks: a range you cannot render in a format gets the formats you can plus one line naming the one you could not. Footage with no clean loop point gets delivered as a plain clip with the reason.

Save every render in this recording's folder under the asset desk folder, original untouched.
