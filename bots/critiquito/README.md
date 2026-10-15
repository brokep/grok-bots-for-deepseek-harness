# Critiquito: Design Critique
Turns a screenshot or Figma link into a design critique with ranked, concrete fixes. Covers hierarchy, type, color, copy, and accessibility, and never edits your files.
Converted from the Grok Bot marketplace template by Manuel Muñoz Solera (@mamuso): https://x.ai/bot/marketplace/bots/critiquito

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/critiquito"
```

Then start a session and pick **Critiquito: Design Critique** in the preset selector. The bot's 7 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly open fixes**: Every week, lists the critique findings still open on each screen and offers to re-check the ones with a new version.

## Integrations the original bot used
- figma: Read a frame straight from a file link instead of waiting on a screenshot.
- slack: Post a critique you approved into the channel your team reviews in.
- notion-workspace: Keep the critiques and open fix lists on a page your team can read.
- linear: File the blockers as tickets on the right team, drafted for your yes.
