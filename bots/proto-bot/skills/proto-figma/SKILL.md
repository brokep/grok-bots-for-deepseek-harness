---
name: proto-figma
description: "Use for Figma screens, flows, decks, diagrams, and design reviews: outlines frames from the real UI and draws them through a cloud agent or the Figma connector, or reviews a file for taste and copy."
---

# proto-figma

Part of the Proto Bot agent preset.

# proto-figma

Screens, flows, decks, and diagrams follow the DESIGN rules in memory.

## Build

1. Read the source and any Figma file they point at with the Figma connector.
2. Outline frames from the map's real components, tokens, and copy style. A deck: share the outline before building more than 3 slides.
3. Write <home>/briefs/<slug>-figma.md: the file link (or "a new file in my drafts"), a Frames: list with copy, the components and tokens, and which screenshots show the real UI. Then proto.py brief <file> --kind figma.
4. figma_mode agent: CloudAgent launch with that prompt, the repo, build_model, and the screenshots as file:// images, then proto.py build add <agent id> --kind figma --name <title> and CloudAgent watch. When it lands, check the frames with get_screenshot, send them with the file link per proto-share, and proto.py build done <agent id>. No Figma tools there: proto.py set figma_mode bot.
5. figma_mode bot: draw it myself with use_figma, reading the connector's figma-use skill first, one frame per call. A plugin in figma_plugin: follow its SKILL.md too, with the product's own brand.

Optional: proto.py figma install <zip> adds the user's own Figma plugin.

## Decks and diagrams

Decks in Figma Slides the same way, with 4 to 7 speaker-note bullets per slide citing sources. FigJam the same way, or generate_diagram. No Figma: a hand-written SVG, screenshotted in my browser, sent with its source.

## Review

For a file, frame, or screenshot: a findings table of frame, issue, fix. Taste: hierarchy, spacing, alignment, states (empty, loading, error), fit with the codebase components. Copy: clear, sentence case, no filler, numbers over adjectives, one main action per screen. Lead with the 3 fixes that matter most.

## Never

Edit anyone's file without asking, publish a file, change sharing, or post a link without a yes.
