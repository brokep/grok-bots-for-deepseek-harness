---
name: add-competitor
description: "Use when the user names a new competitor. Provisions an identity, creates the dossier, asks for modules, runs the first pass."
---

# add-competitor

Part of the Stalk Bot agent preset.

# Add competitor

1. Ask for modules (same widget as setup) unless the user said "same as the others".
2. Provision the research identity via the identity ladder in memory.
3. Create /workspace/dossiers/<competitor>/ with index.md, subscriptions.md, snapshots/, and empty module files.
4. Run subscribe, snapshot-site, and watch-x once. Queue walk-the-product if the product module is on and offer to run it now.
5. Report the first-pass lines. Add the competitor to the pulse list.
