# PM bot
Acts as your PM. Writes the dated cut: what's in, what's out, and how you'll know it's done. Engineering doesn't start until you approve it.
Converted from the Grok Bot marketplace template by Ulysses Ng (@): https://x.ai/bot/marketplace/bots/pm-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/pm-bot"
```

Then start a session and pick **PM bot** in the preset selector. The bot's 3 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekday attention list**: Weekday morning quiet digest of open cuts, Eng/QA blockers, and decisions waiting on the owner; stays silent when nothing changed.
