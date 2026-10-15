# Pipeline Pulse
Scans your full pipeline for movement, stale next steps, forecast risk, and CRM gaps. Shows what changed across the book and drafts the updates needed to keep the forecast honest.
Converted from the Grok Bot marketplace template by Krista Letz (@kristaletz): https://x.ai/bot/marketplace/bots/pipeline-health-and-forecast

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/pipeline-health-and-forecast"
```

Then start a session and pick **Pipeline Pulse** in the preset selector. The bot's 3 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekday pipeline pulse**: Disabled by default. Scan an approved opportunity view for new signals, stale next steps, and forecast risk.

## Integrations the original bot used
- Salesforce: 
- Gmail: 
- Slack: 
- Granola: 
- Notion: 
- Google Sheets: 
