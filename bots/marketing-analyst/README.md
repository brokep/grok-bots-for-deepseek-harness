# Marketing Analyst
Turns your ad platform exports into weekly and monthly paid media reports with commentary, answers reporting asks with the real number and its source, and watches spend against the thresholds you set. Never touches a campaign, never changes a budget, and never sends without your yes.
Converted from the Grok Bot marketplace template by Josh Kim (@joshkim): https://x.ai/bot/marketplace/bots/marketing-analyst

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/marketing-analyst"
```

Then start a session and pick **Marketing Analyst** in the preset selector. The bot's 9 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Reporting ask watch**: Disabled by default. Hourly during weekday working hours in the user's timezone. Reads the mailbox or label the user named for paid media reporting asks, drafts a reply with the real number, the date range, and the source file, and stays quiet when there is no new ask.
- **Weekly paid media report**: Disabled by default. Monday mornings in the user's timezone. Builds last week's paid media report from the exports on hand, or names exactly which export and which date range is still missing. Draft only.
- **Monthly paid media report**: Disabled by default. The 1st of the month in the user's timezone. Builds the closed month's report with the three month trend, the campaign rollup, and budget pacing when a budget is on file. Draft only.

## Integrations the original bot used
- Google Sheets: Recommended. Reads the export sheet or tab you name, and is one place the column map and the metrics history can live as a sheet instead of a file. Read only unless you ask for a sheet to be written.
- Google Drive: Recommended. Reads the folder where your ad platform CSV exports land, newest file first, and holds the dated reports. A pasted file works instead.
- Gmail: Optional. Reads the mailbox or label where reporting asks arrive, and holds the drafted reply and the delivered report as a draft. Sends only when you say send.
- Slack: Optional. A destination for the weekly report, the monthly report, or a spend ping, in a channel you name. Nothing is posted without your explicit yes.
