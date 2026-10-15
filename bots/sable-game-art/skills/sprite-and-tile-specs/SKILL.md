---
name: sprite-and-tile-specs
description: "Use when the user needs the numbers before art gets made: canvas sizes, animation frame counts, pivots, tile grids, seam and padding rules, naming, and engine import settings."
---

# Sprite and tile specs

Part of the Game Art Director agent preset.

Inputs: the engine, the target resolution, and the base unit, either a tile size or a character height in pixels.

1. Set the grid first. Pick a tile size of 16, 32, 48, or 64, a character canvas that is a whole multiple of it, and the pixels-per-unit and camera zoom that keep every pixel on a whole number. When their numbers land on a half pixel, say so and give the nearest clean values.

2. Build the animation table per character: state, frame count, frames per second, loop or once, canvas, pivot, and notes. Starting points, not law: idle 4 frames at 6fps, walk 6 to 8 at 10fps, run 8 at 12fps, attack 4 to 6 at 12fps, hit 2, death 6 to 8. Say they are starting points and adjust to their genre.

3. Put the pivot in words as well as numbers, usually bottom centre on the feet, and keep it identical across every state so the character does not hop between animations.

4. Tilesets: the grid, whether they need a 16 tile edge set or a 47 tile blob set, the seam rule, the autotile shape their engine expects, and a one or two pixel extrude so neighbouring tiles do not bleed.

5. Write the naming convention once and hold to it everywhere. Lower case, no spaces, `subject_state_direction_frame`, frame numbers zero padded.

6. Give the engine import settings and name the ones to check rather than guessing at them. Godot: filter off, mipmaps off, imported as sprite frames. Unity: point filter, no compression for pixel art, pixels per unit, sprite mode multiple, pivot set to match the spec. GameMaker and Unreal by name. Atlas JSON for Phaser or Pixi. Say when you are unsure of a setting name.

7. Finish with the shot list: every asset still to make, with its canvas, frame count, and priority. That list is what the weekly review measures progress against. If Linear is connected, offer to open it as issues, one per asset, on a yes. If Notion is connected, offer to keep it there so the team can see it.

Fallback: no engine chosen means you write engine-neutral numbers and flag the two settings that always differ.

Save the spec and the shot list under the game art folder.
