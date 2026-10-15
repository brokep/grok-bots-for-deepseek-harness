# Cooper
News agent for AI, tech, venture capital, and business. Delivers a tight daily Slack briefing of top stories at 8am, plus weekday mid-day competitor alerts only when something truly clears the bar.
Converted from the Grok Bot marketplace template by Tommy Hansen (@TommyHansenTA): https://x.ai/bot/marketplace/bots/cooper

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/cooper"
```

Then start a session and pick **Cooper** in the preset selector. The bot's 0 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily AI/tech/VC briefing**: Every day at 8:00 AM — tight Slack DM briefing of top AI/tech/VC stories.
- **Midday competitor alert**: Weekdays at 1:00 PM — Slack DM only if a top competitor/hire/priority-company story clears the bar; otherwise stay silent.
- **Afternoon competitor alert**: Weekdays at 4:00 PM — Slack DM only if a top competitor/hire/priority-company story clears the bar; otherwise stay silent.

## Integrations the original bot used
- Slack: Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
