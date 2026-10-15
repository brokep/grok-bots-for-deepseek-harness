# Customer Call Coach & Assistant
Briefs you before customer calls and coaches you after based on your performance.
Converted from the Grok Bot marketplace template by Anoop Baliga (@akbaliga96): https://x.ai/bot/marketplace/bots/customer-call-coach

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/customer-call-coach"
```

Then start a session and pick **Customer Call Coach & Assistant** in the preset selector. The bot's 0 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Friday Coach Refresh**: Quiet Friday afternoon refresh of coaching signals from meetings and Slack; stays silent unless a connector fails. Ships paused until Enable.

## Integrations the original bot used
- Granola: Your meetings in your workflow. Granola gives Cursor access to what your team discussed, decided, and committed to.
- Slack: Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
- Gmail: Search, read, draft, and manage email.
