---
name: asset-consistency-check
description: "Use when the user hands over art and wants to know whether it holds together: palette drift, canvas and grid errors, stray anti-aliasing, outline or light inconsistency, naming, or readability at game size."
---

# Asset consistency check

Part of the Game Art Director agent preset.

Inputs: images in chat, a zip, a folder, or a sheet, plus the style guide and the spec. Without a guide, ask for the palette and the canvas size, or infer them from the set and say you inferred them.

1. Measure first, with a script, one row per file: exact colour count, every colour outside the locked palette with its hex and its pixel count, canvas size against spec, whether the art sits on the pixel grid, semi-transparent and anti-aliased edge pixels, alpha halos, the trim box and the padding, and the file name against the convention.

2. Then look at the set yourself for what no script catches: light direction, outline weight, saturation and value drift across the set, detail density, and whether the silhouette still reads. Downscale to the real in-game size and look again, because most art fails there first.

3. Report per file. Either it passes, or you name the finding with the number behind it. Never write that something looks inconsistent without the measurement that says so.

4. Sort the findings into three groups. Breaks the build: wrong canvas, off grid, bad name. Breaks the look: off-palette colours, wrong light direction, outline drift. Worth a second pass: detail density, readability at size.

5. Offer only the fixes you can actually run. Snap off-palette colours to the nearest palette entry with a before and after preview. Strip anti-aliasing. Trim or pad to the spec canvas. Rename to the convention. Run them on a yes, leave the originals untouched, and write the fixed copies next to them.

Fallbacks: if the image library is missing, install it. If that fails, do the visual review, say plainly which checks you could not measure, and hand them the script to run locally.

Save the dated report under the game art folder.
