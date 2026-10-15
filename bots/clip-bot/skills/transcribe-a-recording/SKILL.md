---
name: transcribe-a-recording
description: "Use when the user hands over a recording, an upload, a link, or an audio file, and you need a timestamped transcript before anything else can happen."
---

# Transcribe a recording

Part of the Clip Bot agent preset.

Inputs: an uploaded video or audio file, a public link to a talk, podcast, or webinar, or an exported recording of a call.

1. Say in one line what you received: length, format, and how many voices you can hear. Ask nothing yet.
2. Pull the audio and transcribe it with word-level timestamps. Post progress as you go so the user sees movement inside a minute, for example "27 minutes of 58 done".
3. Split by speaker where the voices are distinguishable. Call them Speaker 1 and Speaker 2 until the user names them. Never guess a name from context.
4. Keep the words exactly as spoken, filler included. Cleanup happens at cut time, not here.
5. Write the transcript with a timestamp on every line, plus a subtitle file and a plain reading version without timestamps.
6. Show the first 10 lines in chat with the length, the speaker count, and anything you could not hear.

Output: the timestamped transcript, the subtitle file, and a short paragraph on what the recording covers.

Fallbacks: a link you cannot fetch gets named plainly and you ask for an upload instead. A recording behind a login is out of reach, say that rather than guessing at the content. Rough audio gets a note on which stretches are unreliable, and you mark those lines instead of inventing words.

Save under the clip library in a folder named for the recording, then hand the transcript to the moment finder.
