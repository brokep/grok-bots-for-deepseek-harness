---
name: teardown
description: "Use on demand for a side-by-side onboarding comparison between one competitor and the user's product."
---

# teardown

Part of the Stalk Bot agent preset.

# Teardown

## Inputs
Competitor dossier teardown.md (run walk-the-product first if missing), the user's own onboarding (ask the user to describe it or walk it myself if I have a test account they provide).

## Output
A two-column comparison: steps to first value, minutes to first value, required fields at signup, card required, skippable steps, first screen after signup, empty state quality, integrations offered during onboarding, first upsell moment, what they do better (3), what we do better (3), one suggestion per gap that is a question not a directive. Screenshots side by side where I have both. Written to /workspace/dossiers/<competitor>/teardown-vs-us.md, built into an HTML report (html-report) with both sides' screenshots and the competitor's onboarding video embedded, and summarized in 6 lines in chat with the report attached.
