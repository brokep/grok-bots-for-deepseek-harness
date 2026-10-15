# frank
EA chief-of-staff bot for exec support: conference rooms, interview prep, leadership outreach, Slack channel inventories, sheet↔calendar checks, and birthday/anniversary calendar loads.
Converted from the Grok Bot marketplace template by Natasha Kuo (@tashatweetss): https://x.ai/bot/marketplace/bots/frank

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/frank"
```

Then start a session and pick **frank** in the preset selector. The bot's 0 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Exec interview-prep reminder**: Weekdays: check today's interviews vs a Notion prep doc.
- **Exec conference-room rundown (2 business days ahead)**: Weekday afternoon: room chart for two business days out.
- **Exec same-day conference-room check**: Weekday morning: same-day room chart for overnight changes.
- **Weekly leadership-outreach check**: Friday: Slack outreach channel vs tracker for one exec.

## Integrations the original bot used
- Google Calendar: Search events and schedule meetings.
- Gmail: Search, read, draft, and manage email.
- Slack: Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
- Notion: Notion Skills + Notion MCP server packaged as a Cursor plugin.
- Google Sheets: 
