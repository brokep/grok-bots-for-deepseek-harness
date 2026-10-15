---
name: edit-plan
description: "Use before starting any new edit, or when a change alters the cut: picks takes and B-roll and sends the edit plan for approval."
---

# edit-plan

Part of the Video Editor agent preset.

# Edit plan

## When to use
Before starting ANY new edit, and again when a requested change alters the cut.

## Inputs
Every raw take, the script if there is one, the SETUP fact, and the video assets index. No script: plan from the transcript. Footage and transcripts per video-tools.

## Steps
1. Transcribe every take with word timestamps.
2. For every line, pick the best take: usually the last one, and a measured pace over a rushed one. Never leave repeated lines or duplicate takes in an edit.
3. Compare what was said with the script. The user doesn't always follow it word for word, so captions match what they actually said, not the script text.
4. Choose the B-roll style and say which it will be. Emotional or reflective videos use full-screen cutaways of the user's own footage with hard cuts. Motivational or lesson videos use overlays (photos or clips over part of the frame). Videos in between use a mix. A style picked at setup wins.
5. Choose images and clips:
   - Mostly real photos and videos of the user and their life, never an edit built only from animations or motion graphics. Animations are occasional accents at most.
   - B-roll matches the video's tone. No cute or off-tone stock.
   - An overlay clip only where the user asked for it, and never the same clip several times in one video.
   - Company logos over photos of company buildings. For a quote from another person, play their clip with their own voice under the narration, not a still portrait or a muted clip.
   - A product's app icon only where the speaker names it as a tool they're using (pop-ins, graphics). Inside screen recordings or interface mock-ups, keep the interface's real avatar.
   - Nothing on the hard no list.
6. Pick song options from the songs in the video assets folder or tracks the user names, and note where each swells.
7. Send the plan, then wait for approval before cutting or rendering.

## Output
A bold title with the duration, then bullets for Hook (text, size, colors, layering), Hook timing, Highlight words (in the user's highlight color), Your wording vs the script, Cuts and zooms, Graphics list, Images and clips list, Ending, numbered Song options with where each swells, and Need from you (all decisions). Never a table or a beat-by-beat line list. If a tool in video-tools is missing, say which fallback the edit will use.

## Never
Cut or render before approval. Guess at a missing take or asset: put it under Need from you.
