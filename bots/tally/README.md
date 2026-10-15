# Paid Media Report Desk
Turns your Google Ads, Meta, and LinkedIn exports into one weekly report with commentary. Answers reporting asks in Slack with real numbers, and never posts without your yes.
Converted from the Grok Bot marketplace template by Miguel Cruz (@cruzmiguel000): https://x.ai/bot/marketplace/bots/tally

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/tally"
```

Then start a session and pick **Paid Media Report Desk** in the preset selector. The bot's 6 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Reporting ask watch**: Through the working day, checks the channels you named for paid media reporting asks and brings you a drafted reply to approve.
- **Weekly paid media report**: Once a week, builds last week's paid media report from the exports on hand, or names exactly which export it still needs.
- **Monthly paid media report**: On the first business day of the month, builds the closed month's report with the three-month trend, campaign rollup, and budget pacing.

## Integrations the original bot used
- slack: Watch your channels for reporting asks and post the reports you approve.
- notion-workspace: Keep every weekly and monthly report where your team looks things up.
- linear: Turn something a report says to fix into an issue in your backlog.
- hex: Read spend and conversion data that already lands in your warehouse.
- Databricks SQL: Query spend and conversion tables straight from your warehouse.
- Gmail: Pick up the scheduled export emails the ad platforms send.
- Google Sheets: Read exports you keep in a sheet.
