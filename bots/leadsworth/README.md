# Lead Pipeline Desk
Scores your inbound leads, merges duplicates, assigns an owner, and flags what's stuck. Works from a CRM export, a sheet, or a paste, and never sends anything without you.
Converted from the Grok Bot marketplace template by Miguel Cruz (@cruzmiguel000): https://x.ai/bot/marketplace/bots/leadsworth

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/leadsworth"
```

Then start a session and pick **Lead Pipeline Desk** in the preset selector. The bot's 7 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily lead triage**: Every weekday morning, scores the leads that came in overnight, merges duplicates, and lists what has no owner or is past its response window.
- **Weekly pipeline report**: Every Monday morning, the week's lead counts by source, the tier mix, what moved, what is stuck, and pacing against the goal.

## Integrations the original bot used
- slack: Post the morning triage and the weekly report to a channel your team already reads.
- notion-workspace: Keep the lead ledger and every weekly report where your team looks things up.
- linear: Open a follow-up issue when a lead is stuck or needs someone outside sales.
- hex: Pull leads and pipeline history from your warehouse when that is where they land.
- Databricks SQL: Query lead and pipeline tables straight from your warehouse.
- Gmail: Save first replies as unsent drafts in your own account.
- Google Sheets: Read and write the lead list where it already lives.
- Salesforce: Read leads and write owners and next steps back to your CRM.
