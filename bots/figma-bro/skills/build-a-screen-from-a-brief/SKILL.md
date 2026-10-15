---
name: build-a-screen-from-a-brief
description: "Use when the user wants a screen made rather than read: a brief, a spec, a reference, or a description of what the screen has to do."
---

# Build a screen from a brief

Part of the figma bro agent preset.

Inputs: a brief, a spec you already wrote, a reference screen, or a plain description of the job the screen does. Plus their component library when Figma is connected.

1. Get the job of the screen in one line, the platform, and the width. Ask only what you cannot infer from the brief.
2. Inventory what already exists before you draw anything new. Read their library and list the components that cover parts of this screen, with the variant to use. Anything with no match is new, and you say which.
3. Write the structure as a layer tree: frame, auto layout direction, gap, padding, alignment, hug or fill on every layer, and the component instance or type style at each leaf. Use their token names for spacing, color, radius, and type, and raw values only where no token exists.
4. Write the real content. No lorem. Ask for copy you cannot know instead of inventing product names, prices, legal text, or numbers.
5. Cover the states in the same pass: empty, loading, error, and the long-content case. Each gets its own layer notes.
6. Build it in the file when the connection lets you write, on a new page named for the request, never inside frames that already exist. When it does not, hand over the tree as a build sheet a designer can assemble in minutes, plus a rendered SVG or PNG mock so they can see it before they build it.
7. Show it, then take one round of edits.

Output: the layer tree with values and token names, the component list split into reuse and new, the content, the states, and a mock or the built page.

Never publish, never overwrite an existing frame, and never change a component in their library. Anything that touches work they already have needs an explicit yes first.

Save under design handoff.
