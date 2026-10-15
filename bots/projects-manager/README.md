# Projects Manager
Runs your team's projects from Notion: one row per project, a channel per project, and tasks your specialist bots claim. You decide, agents execute, and it never does the specialist work itself.
Converted from the Grok Bot marketplace template by Eric Zakariasson (@ericzakariasson): https://x.ai/bot/marketplace/bots/projects-manager

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/projects-manager"
```

Then start a session and pick **Projects Manager** in the preset selector. The bot's 1 skills come with the bundle.

## Integrations the original bot used
- Notion: Notion Skills + Notion MCP server packaged as a Cursor plugin.
- Slack: Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
