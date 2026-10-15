---
name: frame-to-build-spec
description: "Use when the user wants a spec for a screen or component: a frame link, a connected file and node, or an export they need turned into exact values an engineer can build from."
---

# Frame to build spec

Part of the figma bro agent preset.

Inputs: a Figma frame link, a connected file and node id, or an export plus whatever the user can tell you.

1. Confirm which frame. Read the layer tree rather than the picture when the file is connected. Name the frame and its size back before you write anything.
2. Pull the values as they exist. Frame level: width, height, layout direction, gap, padding, alignment, and whether it hugs, fills, or is fixed. Element level: layer or component name, type style (family, size, weight, line height, letter spacing), fills as the token or style name plus the hex, radii, borders, shadows, opacity.
3. Where a value comes from a variable or a style, give the token name first and the resolved value in parentheses. Where it is raw, write hardcoded and name the token it should have used when one exists.
4. States and variants: default, hover, focus, active, disabled, loading, empty, error. List the ones the file actually has, then list the missing ones as open questions instead of inventing them.
5. Responsive behavior: read the constraints and resizing rules and say what happens at the widths next to this one. When only one width exists, say so and ask which breakpoints matter.
6. Assets: the icons and images that need exporting, with format and scale.
7. Motion: when the frame has prototype interactions on it, say so in one line and offer the motion notes rather than burying the transitions in the spec.

Output: frame name and link, layout, a table of elements with their values, states, responsive notes, assets, then numbered open questions a designer can answer in one pass.

Fallback: with only an image, measure from it, label every number measured, and say you need the file or a pasted inspect panel for exact values. Never present a measured guess as a token value.

Attach the spec here. When Notion or Slack is connected, offer to file it or post it where the team reads, and send nothing without a yes.

Save under design handoff with the frame name and the date.
