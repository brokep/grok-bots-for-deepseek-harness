---
name: captions-and-transcript
description: "Use when the user wants a transcript, a subtitle file, or captions burned into the picture."
---

# Captions and transcript

Part of the Video Edit Desk agent preset.

Inputs: a file in the library, the caption style saved in memory, and any names or jargon the transcript has to spell right.

1. Transcribe the audio with timestamps on this machine. Ask once for the spelling of names, products, and jargon, then apply them everywhere.
2. Mark anything you could not hear as [inaudible] with its timecode. Never fill a gap with a plausible word.
3. Deliver the transcript two ways: a clean read with speaker labels and paragraph breaks, and a timecoded version. Attach both.
4. Subtitle files: write SRT and VTT. Two lines per cue at most, around forty characters a line, and a cue length a person can actually read.
5. Burned-in captions: size the text to the frame height, keep it clear of the platform's own overlays, and cap a vertical cut at four or five words a line. Use the style in memory, and show one still for approval before you render the whole file.
6. Spot-check the finished render at the start, the middle, and the end, and say that you checked. Captions that drift are worse than no captions.

Fallbacks: heavy accents, crosstalk, or bad room audio still get a transcript, plus a warning and the low-confidence spans listed with their timecodes. If they already have a script or a subtitle file, read it as the spelling reference rather than starting from nothing. A language the transcriber does not handle gets named rather than guessed at.

Never change the user's wording in a burned-in caption without asking, even to fix grammar. Save the transcript and both subtitle files beside the footage.
