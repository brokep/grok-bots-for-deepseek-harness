---
name: pull-a-still-from-footage
description: "Use when the user wants a frame out of a video as an image: a thumbnail, a hero still, a product shot, or the frame at a timestamp or moment they name."
---

# Pull a still from footage

Part of the Stills & Clips Desk agent preset.

Inputs: the video file or a link, a timestamp or a rough window, and where the still is going.

1. Read the file first and say its resolution, frame rate, and length in one line, so they know what a still from it can honestly be.
2. Turn their pointer into a window. An exact timestamp gets about a second around it. "The bit where the dashboard loads" gets a window you name back to them before you pull anything.
3. Pull every frame in that window at full resolution off the original file. Never a frame off a re-encoded preview and never a screen grab of a player.
4. Score the candidates and keep the best three: in focus, no motion blur, eyes open, mouth not caught mid-word, the interface fully drawn rather than half loaded, and nothing crossing the subject.
5. Show those three side by side with the timecode on each, say which one you would use and why in one line, and let them pick.
6. Clean the pick: straighten it, take out the player chrome, the cursor, and any overlay that crept in, and lift the exposure only as far as the source allows.
7. Hand it to Export sizes, captions, and alt text in the same message. A thumbnail gets its text set afterward in their font from the size sheet, never generated into the image.

Fallbacks: a 1080p source means you name the largest honest size and refuse the upscale. Heavily compressed or interlaced footage gets cleaned as far as it goes and you say the frame is soft. A link you cannot download gets one ask for the upload.

Save the candidates and the pick in this recording's folder under the asset desk folder, original untouched.
