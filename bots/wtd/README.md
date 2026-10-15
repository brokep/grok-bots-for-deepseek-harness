# WTD
WTD is a VIP hospitality planning partner for marketing ops — project-plan and status rhythm across tentpoles and ticket banks, nomination-sheet tracking, marketing-visible status hubs, and decks or agendas. Sales owns guest inviting; this bot keeps the plan and status clean without dumping private notes onto shared pages.
Converted from the Grok Bot marketplace template by Jenna Nanpei (@jennananpei): https://x.ai/bot/marketplace/bots/wtd

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/wtd"
```

Then start a session and pick **WTD** in the preset selector. The bot's 6 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **VIP Plan status refresh**: Weekday morning refresh of the marketing-visible VIP project plan / status hub (status only).

## Integrations the original bot used
- Notion: Notion Skills + Notion MCP server packaged as a Cursor plugin.
- Slack: Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
- Gmail: Search, read, draft, and manage email.
- Google Drive: Search, read, create, and share files.
