# Sequencer
Runs outbound as a staff function: queues prospects that match your ICP, keeps sequence state on your tracker, and stages every touch as a draft in your voice learned from your sent mail. Never sends, never writes to your CRM without your yes, and never invents research or contacts.
Converted from the Grok Bot marketplace template by Simon Lackowski (@): https://x.ai/bot/marketplace/bots/sequencer

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/sequencer"
```

Then start a session and pick **Sequencer** in the preset selector. The bot's 9 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Sequencer daily**: Disabled by default. Weekday mornings at 8am in the user's timezone. Advances every due sequence step, stages the next touch as a draft, writes state back to the tracker, and posts one review list. Quiet when nothing is due.
- **Daily prospects**: Disabled by default. Weekday mornings at 7am in the user's timezone. Queues new prospects that match the confirmed ICP onto the tracker, up to the saved daily cap. Quiet when the cap is already filled.
- **Inbox triage**: Disabled by default. Hourly from 9am to 5pm on weekdays in the user's timezone. Flags inbound mail and messages from people already on the tracker, with a suggested next action. Quiet when nothing needs a reply.
- **CRM sequence guard**: Disabled by default. Weekday evenings at 6pm in the user's timezone. Pauses tracker rows where the CRM shows the saved open-opportunity stage, so nobody gets a cold touch mid-deal. Quiet when nothing changed.

## Integrations the original bot used
- Gmail: Recommended, and the usual voice source when the user's mail runs here. Reads sent outbound and booked-meeting threads to build the voice card, and stages each touch as a draft. If their mail is elsewhere, about 3 pasted samples do the same job and drafts are staged as text in chat.
- Google Sheets: Recommended. The sequence tracker lives here when the user works in sheets, one row per contact per sequence. A CSV upload carries the same columns when it does not.
- Salesforce: Optional, and one CRM option among peers. Supplies ownership, open-opportunity stages for the pause guard, and title winners during discovery. A CRM with no connector runs through a browser sign-in or a CSV export instead.
- Google Calendar: Optional. Confirms which threads really ended in a booked meeting, so the voice card weights the touches that worked, and blocks review time for sending.
- Slack: Optional. Adds team chat to inbox triage when a sequenced contact reaches the user there. Read only, never used to train cold voice.
