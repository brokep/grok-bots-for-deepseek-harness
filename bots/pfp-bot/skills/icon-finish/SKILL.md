---
name: icon-finish
description: "After the previews: upscale to HD and X size, edit one thing, try again, or send the backup."
---

# icon-finish

Part of the Pfp Bot agent preset.

# icon-finish

Runs when the user picks from the previews in make-icon.

## Upscale

Run python3 /workspace/pfp-bot/pfp.py finish --pick <a, b, or e1> --base <base>. Send one text message with the hd and x400 files in images: "Here's you in HD. The 400 px one is sized for X." If it says resized false, send the hd file alone with "Here's you." Then one line and this widget:
"I can edit it, start over from a different photo, or make one for a friend who says yes."
{"prompt":"How's that?","options":[{"label":"Love it","value":"love","style":"primary"},{"label":"Edit it","value":"edit","description":"Change one thing, keep the rest"},{"label":"Different photo","value":"photo"}],"allowCustom":true}
- "love": python3 /workspace/pfp-bot/pfp.py love, then: "Saved as a style reference. Want it on a bot too? Send it to that bot and ask it to set it as its avatar. I can wear one too if you ask."
- "photo": ask for the new photo or handle, then run make-icon.
- They ask me to wear one: update_state target "avatar", action "set", path set to the HD file. Only ever when asked.

## Edit

If they did not say which take, ask with a two-option widget. Then:
{"prompt":"What should change?","options":[{"label":"Eyes","value":"eyes"},{"label":"Hair","value":"hair"},{"label":"Glasses or accessories","value":"accessories"},{"label":"Skin tone","value":"skin"},{"label":"Framing","value":"framing"}],"allowCustom":true}
Make one GenerateImage call with reference_image_paths [that draft, then the photos] and this description: "Square 1:1 profile icon. The first reference image is the current icon. Keep it exactly the same except: <change>. The remaining images show the person, for reference only. Keep two solid near-black vertical capsule eyes, no mouth, no nose, and the near-black charcoal background." In pet mode, say "its simplified mouth and nose" instead of "no mouth, no nose". Check it with make-icon step 4, run pfp.py preview --edit <path> --base <base>, send it, and offer Upscale this, Edit again, or Try again. A lasting preference also goes in pfp.py tweak "<preference>".

## Try again

Run make-icon step 3 with the same prep output.

## Backup

Two misses in a row: one text message with the better draft and the source photo in images: "Grok's not nailing it this time. The style's official site does it with ChatGPT: open https://grokbot-icon-studio.serio-ai.chatgpt.site/en, copy the full prompt, open ChatGPT, attach the photo I'm sending, and send." That site is the only official one. Never send anyone to a look-alike.
