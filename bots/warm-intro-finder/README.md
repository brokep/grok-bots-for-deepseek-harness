# GTM Connections
Finds credible ways into a target account through mutual contacts, past conversations, shared history, and prior meetings. Ranks the best paths, drafts the introduction ask, and tracks what happened.
Converted from the Grok Bot marketplace template by Brian Joseph (@): https://x.ai/bot/marketplace/bots/warm-intro-finder

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/warm-intro-finder"
```

Then start a session and pick **GTM Connections** in the preset selector. The bot's 3 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Warm-path follow-through queue**: Disabled by default. Surface identified paths and intro requests whose next action is due or stalled.

## Integrations the original bot used
- Gmail: 
- Google Calendar: 
- Salesforce: 
- Notion: 
- Google Sheets: 
- Slack: 
