---
name: design-to-code-handoff-notes
description: "Use when a frame is going to an engineer: mapping Figma components to code, values in the stack's terms, the behavior a design cannot show, and the open questions."
---

# Design to code handoff notes

Part of the figma bro agent preset.

Inputs: a spec you already wrote or a frame, the stack the engineers build in, and the code's existing components when a repo or a paste is available.

1. Map each Figma component in the frame to the code component that already exists, naming the file or path when you can see the repo. Anything with no match is marked new.
2. For every mapped component, write the props an engineer needs: variant, size, state, and content slots, in the naming the stack uses.
3. Translate the values into that stack. Tailwind gets the class or the nearest token, CSS gets custom properties, SwiftUI and Compose get their own type and spacing names. When a Figma value has no clean equivalent, say so and give the raw value.
4. Write the behavior a design cannot show: what happens on submit, what the loading state waits on, the error copy, what the empty state says, focus order, and what a screen reader should read.
5. Pull in the motion rows when the frame has prototype interactions, or say plainly that the motion is unspecified.
6. List the assets to export and where they should land.
7. Numbered open questions, each addressed to designer or engineer, each answerable in one line.

Output: a note an engineer can start from without asking a question first. Component map, props, values in stack terms, behavior, motion, assets, open questions.

Never invent a code component, a path, or a prop name you have not seen, and never call a design final. When Linear is connected, offer one draft issue per open question. When Slack is connected, offer to post the note to the channel the engineers read. Neither goes out without an explicit yes.

Save under design handoff.
