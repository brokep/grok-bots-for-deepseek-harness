# Hiring Signals
Tracks hiring activity across selected companies and job sources. Highlights meaningful changes, matches them to accounts and owners, and passes the right context into research or prospecting workflows.
Converted from the Grok Bot marketplace template by Simon Lackowski (@): https://x.ai/bot/marketplace/bots/hiring-activity-monitor

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/hiring-activity-monitor"
```

Then start a session and pick **Hiring Signals** in the preset selector. The bot's 3 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekday hiring signal digest**: Disabled by default. Ingest selected sources, write normalized rows to the confirmed system of record, and deliver new or materially changed high-fit signals to the confirmed private destination.

## Integrations the original bot used
- Google Sheets: 
- Notion: 
- Slack: 
- Salesforce: 
