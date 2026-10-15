# GTM Prospecting
Turns an ideal customer profile into a focused prospect list, adds useful context, and checks for existing relationships. Drafts first-touch email and LinkedIn messages for your review.
Converted from the Grok Bot marketplace template by Caro Scalercio (@): https://x.ai/bot/marketplace/bots/prospector

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/prospector"
```

Then start a session and pick **GTM Prospecting** in the preset selector. The bot's 3 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly prospecting hygiene**: Disabled by default. Audit selected lists for duplicates, stale ownership, recent touches, and suppression conflicts.

## Integrations the original bot used
- Gmail: 
- Google Sheets: 
- Notion: 
- Salesforce: 
