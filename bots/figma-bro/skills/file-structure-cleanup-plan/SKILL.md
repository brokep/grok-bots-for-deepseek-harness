---
name: file-structure-cleanup-plan
description: "Use when a frame's structure fights the design: nesting too deep to reason about, auto layout that will not resize, absolute positions where a stack belongs, or a frame that needs flattening for export or handoff."
---

# File structure cleanup plan

Part of the figma bro agent preset.

Inputs: the frame, and what they need it to do, whether that is resize cleanly, export flat, become a component, or just get simpler.

1. Read the layer tree. Report the depth, the count of frames and groups, and where the nesting goes past what the design needs.
2. Name the specific problems: groups that should be auto layout frames, auto layout frames pinned to fixed sizes where they should hug or fill, absolute-positioned children inside a stack, redundant wrapper frames, and layers still called Frame 427.
3. Write the plan as an ordered list of changes. Each one names the layer, the change, and what it fixes. The changes that unblock the others go first.
4. For a flatten, list exactly what collapses and what stays. Components, text layers, and anything carrying a variant stay intact. Say what gets hard to edit afterward, because a flatten only goes one way.
5. Include the layer renames in the plan, with the new names written out.
6. Offer a before and after view of the tree so the change is easy to approve.

Output: the plan, the flatten list when one applies, the rename list, and one line on what to do first.

Fallback: with no file access, work from a pasted layer tree or a screenshot of the layers panel and plan from that.

Never restructure or flatten anything without an explicit yes on the plan, and never flatten a component or a published library asset.

Save under design handoff.
