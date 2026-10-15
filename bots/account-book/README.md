# Account Research Desk
Researches the companies you sell to and writes your pre-call brief and account plan. Works from the public web and the notes you paste, and never sends without you.
Converted from the Grok Bot marketplace template by Anoop Baliga (@akbaliga96): https://x.ai/bot/marketplace/bots/account-book

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/account-book"
```

Then start a session and pick **Account Research Desk** in the preset selector. The bot's 11 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly account signals**: Every Monday morning, checks your accounts for public news, funding, leadership, and hiring signals, and reports only what matters to the deal.
- **Weekday call prep**: Every weekday morning, a short prep on the external calls that day with what changed, who is on them, and what is still open.
- **Friday open threads review**: Every Friday morning, the open threads and next steps across your accounts, with what has gone stale and what closed this week.

## Integrations the original bot used
- slack: Post a brief or plan you approved to the channel your deal team reads.
- notion-workspace: Keep account files and plans where your team already looks things up.
- linear: See what an account asked for as issues, and check status before a call.
- hex: Read account usage or pipeline numbers your team keeps in a warehouse.
- Databricks SQL: Query account usage and health numbers straight from your warehouse.
- Gmail: Search, read, draft, and manage email.
- Google Calendar: Search events and schedule meetings.
- Granola: Pull notes from your customer calls.
- Google Drive: Read account docs and decks your team already keeps in Drive.
- Google Sheets: Read and write Google Sheets.
- Salesforce: Read and update Salesforce records.
