# Call Follow-Ups
Turns each recorded call into a follow-up email in your voice, a next-steps note, and the CRM updates, including the qualification fields your team runs on. Watches Gong and Granola for new calls, and nothing sends or saves without your yes.
Converted from the Grok Bot marketplace template by Daniel Brill (@danielbrill_): https://x.ai/bot/marketplace/bots/call-follow-ups

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/call-follow-ups"
```

Then start a session and pick **Call Follow-Ups** in the preset selector. The bot's 6 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **New call watch**: Every 30 minutes on weekdays, find calls the owner hosted that finished since the last run and stage the post-call pack for approval.

## Integrations the original bot used
- Gong: Finished calls, summaries, and transcripts. Granola covers the meetings it did not record.
- Granola: Transcript source for meetings your recorder did not capture. Works alongside Gong or on its own.
- Salesforce: Where next steps, stage, close date, and new contacts are proposed. Connect the one CRM you use.
- HubSpot: CRM alternative to Salesforce.
- Attio: CRM alternative to Salesforce.
- Gmail: Learns your voice from sent mail and saves follow-ups as drafts. Use Outlook instead on Microsoft 365.
- Outlook: Email alternative for Microsoft 365 users.
- Google Calendar: Matches a call to its meeting and attendees when the recorder's participant list is thin.
- Slack: Deliver the post-call pack as a DM.
- Notion: Keep post-call notes and the open promises where your team already looks.
- Linear: Turn a commitment from a call into a ticket, drafted for you to approve.
- Hex: Pull account numbers before a call when your team keeps them in a warehouse.
