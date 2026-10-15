# Meeting Recap Deck
Turns your meeting notes into a recap deck in your slide template. Works from notes you paste or upload, and never invents a quote.
Converted from the Grok Bot marketplace template by Krista Letz (@kristaletz): https://x.ai/bot/marketplace/bots/echo

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/echo"
```

Then start a session and pick **Meeting Recap Deck** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Post-meeting recap draft**: After a meeting ends, drafts the recap from your notes and leaves it here for you to check.
- **Friday recap roundup**: Every Friday, the recaps that went out this week, the drafts still sitting unsent, and the next steps that are past their date.

## Integrations the original bot used
- figma: Read the template slide you point at and build the recap deck in it.
- Google Slides: Build the recap deck in your Google Slides template.
- notion-workspace: Pull meeting notes from your pages and keep finished recaps where your team reads them.
- slack: Post a recap you approved to the channel your team already reads.
- linear: Turn the next steps you agreed to into tickets with owners and dates.
- Gmail: Search, read, draft, and manage email.
- Google Calendar: Search events and schedule meetings.
- Granola: Your meetings in your workflow. Meeting notes, decisions, and commitments.
- Gong: Pull call summaries and transcripts when your notes live in Gong.
