# Tradbot
Watches your personal email and calendar so school forms, bills, and RSVPs don't slip. Drafts the reply, catches the pickup clash, and never sends without you.
Converted from the Grok Bot marketplace template by Claire Vo (@clairevo): https://x.ai/bot/marketplace/bots/tradbot-2

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/tradbot-2"
```

Then start a session and pick **Tradbot** in the preset selector. The bot's 3 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekday family digest**: Every weekday morning, one short brief of the household things that need you today, and quiet when nothing does.
- **Afternoon pickup check**: Every weekday afternoon, a one line check that today's pickup is covered, and the fix when it is not.
- **Kitchen table newspaper**: Every weekday morning, the printable one-page kitchen newspaper kids can read at the table.
- **Weekend preview**: Every Friday evening, the weekend and the week after it with the collisions, what to prepare, and everything still owed.
- **Monthly parent note**: On the first of each month, local events worth considering plus age-adjusted development and parenting notes.

## Integrations the original bot used
- Gmail: Search, read, draft, and manage email.
- Google Calendar: Search events and schedule meetings.
- Slack: Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
