---
name: drop-competitor
description: "Use when the user stops watching a competitor. Unsubscribes the research identity, archives the dossier, removes it from the pulse."
---

# drop-competitor

Part of the Stalk Bot agent preset.

# Drop competitor

1. Confirm which competitor.
2. Unsubscribe the research identity from every list in subscriptions.md (List-Unsubscribe header or link, only for confirmed subscriptions). If a teammate identity bot holds the inbox, send AUTH REQUEST need unsubscribe.
3. Move /workspace/dossiers/<competitor>/ to /workspace/dossiers/_archive/<competitor>-<date>/.
4. Remove from the pulse list and the feature matrix.
5. Report in two lines.
