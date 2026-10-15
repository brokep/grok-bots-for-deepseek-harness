# Office Ops Desk
Tracks office shipments, facilities issues, and team birthdays, then writes the digests. Works from a pasted list or a spreadsheet, and never sends without you.
Converted from the Grok Bot marketplace template by Erika Cabrera (@ericacabera): https://x.ai/bot/marketplace/bots/office-ops-desk

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/office-ops-desk"
```

Then start a session and pick **Office Ops Desk** in the preset selector. The bot's 7 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily shipment status**: Every weekday morning, a short status on what was delivered, what is late, and what has stopped moving.
- **Weekly facilities digest**: Every Monday morning, the open facilities issues grouped by severity with owners and days open.
- **Team celebrations reminder**: Every Friday morning, the birthdays and work anniversaries landing in the next 14 days.

## Integrations the original bot used
- slack: Post a facilities digest or shipment status you approved to a team channel.
- notion-workspace: Mirror the shipments, facilities, and celebrations ledgers into your office wiki.
- linear: File facilities issues as tickets and keep their status in step with the log.
- Gmail: Search, read, draft, and manage email.
- Google Calendar: Search events and schedule meetings.
- Google Sheets: Read and write Google Sheets.
