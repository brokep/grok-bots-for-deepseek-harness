---
name: make-icon
description: "Every icon: prep, confidence gate, two drafts in parallel, checks, and small previews with Upscale, Edit, or Try again."
---

# make-icon

Part of the Pfp Bot agent preset.

# make-icon

Run for every icon. The drawing prompt is in icon-prompt. When the user picks from the previews, run icon-finish.

## 1. Prep, one call

If /workspace/pfp-bot/pfp.py is missing or errors, run the install command in icon-setup first. Then run one of:
- Typed handle: python3 /workspace/pfp-bot/pfp.py prep --name "<my name>" --handle <handle>
- X connector: python3 /workspace/pfp-bot/pfp.py prep --name "<my name>" --url <profile_image_url> --handle <username>
- Photos: python3 /workspace/pfp-bot/pfp.py prep --name "<my name>" --photo <path> [<path>]
Add --source selfie for a selfie. Photo paths come from the note that starts "The user attached". A path on their computer needs CopyToBox first (ListMachines for the machineId, box_path under /workspace/pfp-bot/).

It prints JSON with sources, refs (up to two style references), base, and tweaks.
- "no_x_photo": say so and offer an upload or a selfie.
- "unreadable_photo": ask for a JPEG or PNG, or a screenshot of the photo.
- "media_not_found": ask them to drop their photo in this chat, then rerun prep with that photo. Its path tells pfp.py which folder is mine.
- CopyToBox blocked: skip --photo, work from what I see, and use the no-photo opening in icon-prompt.

## 2. Look, then gate

An X photo needs one Read of sources[0]. Chat uploads are already in view.
Trait card: skin tone, hair color, hair shape, each rated high, medium, or low, plus up to three must-keep features, most identifying first. TWEAKS override the photo.
Any low: do not draft. Say what I could not read in one line, then run icon-guide. Medium: draft, then name the guess.

## 3. Two drafts at once

Fill icon-prompt once. Call GenerateImage TWICE IN THE SAME TURN with that description: the first with reference_image_paths [refs[0], then up to two photos], the second with [refs[1], the same photos], aspect_ratio "1:1" on both. Use the paths GenerateImage returns. One ref: use it for both. No refs: pass the photos alone. No photo: pass the reference alone.

## 4. Check both

1. Eyes: two solid near-black capsules, upright, same size, nothing inside. Sideways eyes are the top failure. Fix: "Draw two solid near-black vertical capsule eyes, upright, same size, with nothing inside them."
2. No mouth or nose (pet mode: a small simplified one). Fix: "Remove the mouth and nose completely. The face has only the two capsule eyes and blush."
3. Framing: the face peeks from the lower left, the edge cuts the left side and chin, the upper right is empty, both eyes show. Fix: "Move the face to the lower left, cut by the left and bottom edges, with the upper right empty."
4. Skin tone matches the card, never defaulting pale.
5. Hair color and shape match.
6. Every must-keep feature is there, glasses never hiding the eyes. Glasses and small accessories drop most often.
7. One flat 2D icon, no text, frame, texture, or character sheet.
8. Near-black charcoal background.
For 4 to 8, the fix is the check as an order, like "Make the face color deep brown."

A draft passes with no fail on 1 to 3 and at most one other fail. Both fail: redraft once in one call, with "Must fix:" lines under the first sentence and the better draft's reference. Still failing: the backup in icon-finish.

## 5. Small previews

python3 /workspace/pfp-bot/pfp.py preview --a <passing draft> [--b <second passing draft>] --base <base>
If it prints folder_moved, my folder was guessed wrong and is fixed now: redo step 3 once with the sources and refs it prints, then preview again.
Send ONE SendToUser text message, content "Two quick takes." plus any guess line, with both previews as file:// urls in its images field (alt "Take A" and "Take B"). Then this widget:
{"prompt":"Which one?","options":[{"label":"Upscale A","value":"up-a","style":"primary","description":"HD 2048 px plus 400 px for X"},{"label":"Upscale B","value":"up-b"},{"label":"Edit one","value":"edit","description":"Change one thing, keep the rest"},{"label":"Try again","value":"again","description":"Two fresh takes"}],"allowCustom":true}
Only one passing draft: preview it alone and offer Upscale, Edit, and Try again. If they say they cannot see the previews, resend them at once.
