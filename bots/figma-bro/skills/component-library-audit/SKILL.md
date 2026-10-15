---
name: component-library-audit
description: "Use when the user asks about the health of their component library: duplicates, detached instances, naming, variant coverage, or what to clean up first."
---

# Component library audit

Part of the figma bro agent preset.

Inputs: a connected Figma library or file, or a pasted list of component names.

1. List every component and component set with its variants. Count instances of each when the file is connected.
2. Find duplicates: near-identical names, two components doing the same job under different names, and local one-offs that should be library instances.
3. Find detached instances, and instances that drift from their master with hand-set padding, color, or type.
4. Check naming against their convention. Ask for it once, otherwise report the dominant pattern in the file and flag what breaks it. Category/Component/Variant is a common shape. Call out leftovers like Frame 427 and Group 12 by name.
5. Check variant coverage: the sizes, states, and boolean props each component should carry, and what is missing.
6. Flag components with zero instances as delete candidates, and name the five most-used components as the ones worth keeping clean.

Output: a table of component, variants, instance count, and the issue found, sorted by what the issue costs. Then a fix list in three tiers, rename, merge, and rebuild, each with a count and a rough time.

Fallback: with only a screenshot of the assets panel or a pasted name list, audit naming and duplicates and say instance counts are unavailable.

Never rename, merge, delete, or publish anything yourself. Write the fix list, and if they want you to make a change, get an explicit yes on each one. When Linear is connected, offer the fix tiers as issues they approve first.

Save under design handoff.
