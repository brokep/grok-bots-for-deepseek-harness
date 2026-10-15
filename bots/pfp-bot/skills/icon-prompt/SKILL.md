---
name: icon-prompt
description: "The drawing prompt for every draft, with reference wording, must-keep rules, edge cases, and pet mode."
---

# icon-prompt

Part of the Pfp Bot agent preset.

# icon-prompt

The GenerateImage description for every draft. Fill the braces, keep the rest word for word, and keep it about this long. With no style reference, leave out the "Copy from the style reference" line.

Square 1:1 profile icon. {REFERENCES}
Must keep from the person: {MUST_KEEP}. Do not copy the expression, the smile, or the realistic face structure.
Copy from the style reference only its drawing style, eye shape, blush, framing, crop, and background. Never copy its hair, skin tone, glasses, or clothing.
Face: a huge round smooth bot face, one flat color field in the person's skin tone, soft cheek-to-chin curve. No mouth, no nose, no eyebrows, no smile. Small faint oval blush on both cheeks.
Eyes: exactly two solid near-black vertical capsules with rounded ends, same size, parallel, each about three times taller than wide. No iris, no whites, no highlights, no lashes.
Composition: extreme close-up. The face fills most of the canvas and peeks in from the lower left, tilted about 15 to 20 degrees clockwise so the screen-left eye sits higher. The canvas edge cuts through the left side of the head and through the chin. Empty dark background at the upper right. No body, no hands.
Hair and color: a few large smooth hair masses, flat soft 2D color fields, almost no outlines, one step of broad soft shading.
Background: one solid near-black charcoal color.
Exclude: frames, badges, text, logos, particles, photorealism, 3D render, painterly texture, character sheets, multiple views.
If rules conflict: 1) two plain black capsule eyes, 2) round face with no mouth or nose, 3) tilted close-up with both eyes visible, 4) the person's colors and must-keep features, 5) everything else.
Must keep, again: {MUST_KEEP_SHORT}.

{REFERENCES} is one of:
- Style reference plus photos: "The first reference image is a style and framing example only. The remaining reference images show the person to convert."
- Photos only: "The reference photos show the person to convert. Draw a cute flat illustration, not a portrait."
- No photo: "The reference image is a style and framing example only. Draw a fictional bot wearing this look." Put skin tone in MUST_KEEP.

{MUST_KEEP}: features first (glasses with frame shape, color, and "around both eyes, the eyes visible inside the frames", facial hair, headwear, earrings), then hair color and shape, then skin tone in plain words, then a collar color if it helps. A feature the last try dropped moves to the front. {MUST_KEEP_SHORT}: the features only.

Edge cases, added to MUST_KEEP when they apply:
- Facial hair stays as one flat shape that never reads as a mouth.
- Bald or covered hair stays that way. Never add bangs, accessories, or parts the person does not have.
- Bangs that would cover the eyes get shorter or move aside but keep their flow.
- A key accessory the crop would cut gets shifted or shrunk so part stays visible.

Pet mode, for an animal whose mouth, muzzle, or beak makes it recognizable (most dogs, cats, and birds): "No mouth, no nose, no eyebrows, no smile." becomes "Include the mouth and nose, simplified as much as possible." and "2) round face with no mouth or nose" becomes "2) round bot face". Everything else stays, capsule eyes included. Name species features in MUST_KEEP, like a cat's whiskers, a dog's ear shape, or a bird's beak color. Fur or surface color becomes the face color. Drawn characters the user owns follow the person rules.
