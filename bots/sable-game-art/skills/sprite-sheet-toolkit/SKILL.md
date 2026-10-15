---
name: sprite-sheet-toolkit
description: "Use when the user has sprite sheets or loose frames that need slicing, packing, renaming, rescaling, or turning into an atlas their engine can read."
---

# Sprite sheet toolkit

Part of the Game Art Director agent preset.

Inputs: a sheet or a set of frames, plus the frame size when they know it.

1. Find the grid before you cut. Scan for the empty rows and columns, then report the frame size, columns, rows, margin, and spacing you found. Say the numbers out loud and wait for a correction when they look odd.

2. Slice: cut the frames, drop the empty cells, name them to the convention, and hand back a zip plus a contact sheet with the frame numbers printed on it so a bad cut is obvious at a glance.

3. Pack: frames into one sheet with a stated cell size, a fixed grid, and a one or two pixel extrude, plus the atlas file the engine wants. A Godot resource or JSON, a note on Unity sprite metadata, a TexturePacker style JSON, or the hash format Phaser reads.

4. Rescale: nearest neighbour only for pixel art, and whole number factors only. Say no to 1.5x and name the clean options above and below it.

5. Other jobs worth offering: trim uniform padding, split a sheet into one animation per row, mirror a set for the opposite facing, recolour a set to a palette for variants, and build a GIF or strip preview at the spec frame rate so the animation gets judged instead of imagined.

6. Report what you did per file with counts included, and never say a file was written until the write succeeded.

Fallbacks: if the image library is missing, install it. If that fails, give them the exact commands to run locally and stay on the parts you can do by measurement.

Save the output under the game art folder next to the originals.
