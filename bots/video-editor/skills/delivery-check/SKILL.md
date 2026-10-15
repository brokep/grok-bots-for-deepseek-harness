---
name: delivery-check
description: "Use before every delivery, or when the user asks to check a finished video for sync, glitches, and loudness."
---

# delivery-check

Part of the Video Editor agent preset.

# Delivery check

## When to use
Before every delivery, and when the user asks to check a finished video. For a video made elsewhere, skip the checks that need the raw takes or a plan.

## Steps
1. Confirm every requested change landed.
2. Full transcript diff: no repeated or missing lines, and captions match the speech.
3. A/V sync measured at every cut.
4. Frame checks before and after every cut for zoom jumps and glitches.
5. Freeze and black checks, especially at the end (ffmpeg freezedetect and blackdetect).
6. Re-check the best-take choices against all raw takes.
7. Overlay timing and centering.
8. Loudness against the targets in cut-and-render.
Verify every finding with extracted frames and audio before reporting it.

## Output
A pass/fail list, one line per check, with the timestamp of every fail. Then what was fixed, or what needs the user.
