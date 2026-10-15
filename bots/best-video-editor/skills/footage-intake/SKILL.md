---
name: footage-intake
description: "Use when the user uploads, links, or sends a new video or audio file, or asks what is in footage you already have."
---

# Footage intake

Part of the Video Edit Desk agent preset.

Inputs: an uploaded video, a set of clips, an audio file, or a public link.

1. Read the file with ffprobe before you say a word about it. Report duration, resolution, frame rate, codec, audio channels, and file size. Never take a spec from a filename or a guess.
2. A link gets downloaded first, and you say that you did. Anything behind a login you cannot read, so ask for an upload or a public link instead.
3. Pull stills across the whole file, one every few seconds for something short and one every thirty seconds for something long, and attach the strip. It is the visual index both of you work from.
4. Transcribe on this machine whenever there is speech, and hand the transcript to Captions and transcript. A silent clip gets one line saying there is no audio to work with.
5. Build the shot map, one row per continuous shot: start, end, duration, what is on screen in one clause, whether anyone is speaking, and any problem you can see or hear. Problems worth naming: out of focus, clipped or hissing audio, a hard camera shake, blown highlights, wrong orientation, and long dead air.
6. Reply with the specs in one line, the three most usable moments with timecodes, every problem you found, and one question: what do they want out of it.

Fallbacks: take the upload as it comes and start reading it. Only if an upload actually fails do you ask for a link or a smaller export, and you say the same cut can be re-run against the full-size file later. A file that will not decode gets its codec named and one re-encode attempt before you ask them for anything. Audio only still gets a transcript and a map of who speaks when.

Never edit the file in this skill. Save the media report and the shot map beside the footage in the footage library.
