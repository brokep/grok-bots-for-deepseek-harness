# Event Request Desk
Scores every event, sponsorship, and speaking ask, then drafts your yes or no. Works from a Slack channel or a paste, and never sends without you.
Converted from the Grok Bot marketplace template by Emma Weyrauch (@): https://x.ai/bot/marketplace/bots/event-request-desk

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/event-request-desk"
```

Then start a session and pick **Event Request Desk** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekday intake sweep**: Every weekday morning, logs and scores every event ask that came in overnight and names the ones that need a decision today.
- **Weekly queue review**: Every Monday morning, the whole event request queue grouped by what needs a decision, what is stale, and what is already committed.
- **Weekly commitment check**: Every Thursday morning, what the team still owes organizers for events already said yes to, with anything overdue first.

## Integrations the original bot used
- slack: Read new event and sponsorship asks out of the channel where people already ask.
- notion-workspace: Keep the event queue and the weekly review where your team looks things up.
- linear: Track what you owe an organizer after a yes as issues with owners and due dates.
- figma: Pull the logo pack, booth artwork, or slides an organizer is waiting on.
- hex: Chart event spend against your cap and your yes rate over a quarter.
- Gmail: Search, read, draft, and manage email.
- Google Calendar: Search events and schedule meetings.
- Google Drive: Read the tracker sheet and organizer files your team already keeps in Drive.
- Google Sheets: Read and write Google Sheets.
