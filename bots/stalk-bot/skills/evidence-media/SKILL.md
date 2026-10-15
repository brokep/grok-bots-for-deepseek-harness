---
name: evidence-media
description: "How I capture visual evidence: exhaustive screenshots on every pass, a mandatory onboarding video and a clip per key feature for every product walkthrough, and how the recording is produced. Read before any walkthrough, pulse, or test drive."
---

# evidence-media

Part of the Stalk Bot agent preset.

# Evidence media

Every finding a user reads should come with the picture that proves it. Files on disk are the archive. Attachments in chat are the evidence.

## Screenshots, always
1. Take a full-page screenshot of every watched page on every snapshot (home, pricing, changelog, docs index, about, careers, plus user additions). Store under /workspace/dossiers/<competitor>/snapshots/<date>/<page>.png.
2. During a product walk, screenshot everything: every onboarding step, every main surface, every modal and drawer, every empty state, every error, every plan gate or upsell, every settings and billing page, every integration list, before and after each feature action. Store under /workspace/dossiers/<competitor>/walk/<date>/<nn>-<step>.png. Expect 40 to 120 screenshots per walk; fewer than 25 means the walk was shallow, keep going.
3. For X: screenshot the launch or positioning post itself (not the timeline) for anything that lands in a pulse. Store under /workspace/dossiers/<competitor>/x/<date>/.
4. For open roles: screenshot the careers page and each new role's posting. Store under /workspace/dossiers/<competitor>/hiring/<date>/.
5. Attach in chat, not just link (the HTML report carries everything, chat carries the highlights): for every change in a pulse, attach the before and after screenshots side by side (compose a single before/after image with ImageMagick or Pillow when both exist, otherwise attach the after and say "first seen"). For Website pros and cons, attach the page the bullet cites. For hiring, attach the careers page. Cap: 8 images per competitor per pulse, then a line "N more in the dossier."
6. Onboarding test drive (Beat 4 of stalk-setup): attach the first competitor's home and pricing screenshots, the research inbox screenshot showing its address, and the confirmation email screenshot when it arrives. The user should see proof, not a description of proof.
7. Never attach a screenshot that shows the user's own credentials, another customer's data, or the research identity's password.

## Video, required for every product walkthrough
1. Every product walkthrough produces (a) one onboarding video from landing page through first value and (b) one clip per key feature tested, 20 to 90 seconds each. Recording is not optional; only the method varies. Order of attempts: (a) the browser tool's own recording if it offers one, (b) screen capture with ffmpeg against the display the browser runs on (for example `ffmpeg -f x11grab -video_size 1280x800 -i :0.0 -r 10 -t <seconds> walk.mp4` on Linux), (c) if neither works, stitch the step screenshots into a slideshow with ffmpeg (`ffmpeg -framerate 0.5 -pattern_type glob -i '*.png' -vf "scale=1280:-2,format=yuv420p" walk.mp4`), 2 seconds per step, in order. Option (c) always works when screenshots exist.
2. Store as /workspace/dossiers/<competitor>/walk/<date>/00-onboarding.mp4 and /workspace/dossiers/<competitor>/walk/<date>/feature-<nn>-<slug>.mp4. Onboarding video under 4 minutes (cut to landing through first value plus the pricing or billing surface if longer). Feature clips 20 to 90 seconds. All go into the HTML report; the onboarding video and up to 3 feature clips are also attached in chat.
3. Pulses: no video by default. If a pulse includes a positioning or pricing change on the homepage, offer a 20 to 30 second before/after clip stitched from the two snapshots only when the user asks.
4. Say plainly which method produced each video. The stitched slideshow (method c) always works when screenshots exist, so a walkthrough with no video at all means screenshots were not taken, which is a failed walkthrough: redo it. Never claim a recording happened when it did not.

## Naming
Filenames carry competitor, date, and page or step so a folder listing reads as a timeline without opening anything.
