# Copy Humanizer
Edits and rewrites drafts, emails, and pages so they read like a person wrote them. Keeps your voice, shows every change and why, and never invents a fact.
Converted from the Grok Bot marketplace template by Massimo De Luisa (@massimodeluisa): https://x.ai/bot/marketplace/bots/human-copywriter

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/human-copywriter"
```

Then start a session and pick **Copy Humanizer** in the preset selector. The bot's 7 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly shipped check**: Every Friday afternoon, asks what copy actually went out this week and folds the edits the user made into their voice profile.

## Integrations the original bot used
- notion-workspace: Keep the voice profile and every draft where your team already writes.
- slack: Drop a draft in the channel where people give you feedback.
- figma: Read the copy sitting in a design frame and hand back rewritten lines.
- linear: Turn shipped issues into release notes a customer can read.
- Gmail: Search, read, draft, and manage email.
