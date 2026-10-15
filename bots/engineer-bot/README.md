# Lingxi's Engineer Bot
A hands-off engineering supervisor. It boards work, launches cloud agents, watches PRs on a 30-minute cadence, and only asks you to merge. For anyone who wants this pipeline without a specific repo.
Converted from the Grok Bot marketplace template by Lingxi Li (@lingxi): https://x.ai/bot/marketplace/bots/engineer-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/engineer-bot"
```

Then start a session and pick **Lingxi's Engineer Bot** in the preset selector. The bot's 1 skills come with the bundle.

## Integrations the original bot used
- Notion: Notion Skills + Notion MCP server packaged as a Cursor plugin.
