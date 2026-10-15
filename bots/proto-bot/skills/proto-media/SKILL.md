---
name: proto-media
description: "Use for images, edits, memes, product shots, looping avatars, voiceovers, and short videos on FAL, Higgsfield, or Grok Imagine, with the model picks."
---

# proto-media

Part of the Proto Bot agent preset.

# proto-media

Images, edits, memes, looping avatars, and short videos on the media provider in proto.py status. No key yet: offer one per proto-connect, never GenerateImage. Price first (proto.py fal price <id>, higgs price <id> --input <json>, or grok price) and ask above spend_cap. Open asks get 2 or 3 parallel variants.

## FAL

proto.py fal run <endpoint> --input <json> --name <slug>. Local paths in the input upload to public links. Check the endpoint with proto.py fal find <words> and its inputs with proto.py fal schema <id>. Defaults:
- Images and edits: fal-ai/nano-banana-pro and fal-ai/nano-banana-pro/edit.
- Exact text, posters, UI copy: openai/gpt-image-2 and openai/gpt-image-2/edit, run on FAL.
- Photoreal or a strong style: the newest Flux on FAL.
- Motion: the newest Kling or Seedance image-to-video.
- Voice, voice clone, lip-sync: fal find by task.

## Higgsfield

proto.py higgs run <model id> --input <json> --name <slug>, local paths uploading like FAL's. Defaults: higgsfield-ai/soul/v2/standard for stills, bytedance/seedance-2.0/image-to-video for motion (image_url, end_image_url, generate_audio false for loops). Other models and inputs: docs.higgsfield.ai/docs/llms.txt.

## Grok Imagine

xAI's models. Local files go inline, never as public links. Stills and edits: proto.py grok image <prompt> --aspect 1:1 (--image <file>, up to 3). Motion: proto.py grok video <prompt> --duration 5 (--image start frame, --ref character, --voice preset, --video mp4 to restyle).

## Images

Product shots and UI art start from real screenshots (<home>/screens/ or the app) as references. Characters, comics, and meme remakes: name the layout and reuse the same references for consistent characters. Mangled text: rerun the edit with the exact text in quotes, then GPT Image 2 edit on FAL, then rebuild the text as a static HTML page over the image, screenshotted in my browser, and say so.

## Loops and avatars

1. Square still, subject centered with margin, plain background.
2. Image-to-video from the still (also the end frame where the model allows), 5 seconds, a small idle motion (blink, bob, sway), no camera move.
3. proto.py loop <video> --size 512 makes a seamless mp4, gif, and webp, with a hint when one is too big.
4. Send the gif and webp. Wear one only when asked (update_state avatar.set). Another bot's: the user drops the file in that bot's chat.

## Video

Remakes and restyles: Seedance or Kling video-to-video, or a Grok Imagine restyle, one shot at a time, with a shot list in <home>/projects/<slug>/shots.md when longer. Voiceover: text-to-speech on FAL, then proto.py mux --video <v> --audio <a>. Join shots with proto.py concat and check them with proto.py sheet <video>.
