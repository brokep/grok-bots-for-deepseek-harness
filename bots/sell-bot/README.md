# Sell Bot
Works your whole customer journey: outreach in your voice, booked calls with prep and follow-ups, proposals and contracts, then activation, support and billing answers, and expansion. Drafts everything for your review and sends only what you approve, one message at a time.
Converted from the Grok Bot marketplace template by Shub Gaur (@shubgaur): https://x.ai/bot/marketplace/bots/sell-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/sell-bot"
```

Then start a session and pick **Sell Bot** in the preset selector. The bot's 11 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Morning prep**: Disabled by default. Weekdays 7am: prep pages for today's watched calls.
- **Confirm notes**: Disabled by default. Hourly on weekdays: confirm-note drafts for calls about an hour out.
- **Evening wrap-up**: Disabled by default. Weekdays 5:45pm: wrap-ups and the digest for today's calls.
- **Daily follow-through**: Disabled by default. Weekdays 7:50am: check-ins, wow moments, and due series emails.
- **Daily account watch**: Disabled by default. Weekdays 8:56am: credit runway, expansion, watched accounts, and X.
- **Daily prospect follow-up**: Disabled by default. Weekdays 9:40am: prospect replies, follow-ups, leads, and invites.
- **Weekly pipeline review**: Disabled by default. Mondays 9am: stalled deals, overdue touches, and nudges.
- **Monday impact read**: Disabled by default. Mondays 9:20am: how accounts with calls moved against everyone else.
- **Launch heads-ups**: Disabled by default. Weekdays 10:10am and 3:10pm: launches matched to customers who asked.
- **Friday writing review**: Disabled by default. Fridays 3:30pm: drafts against what you sent, and voice rules.

## Integrations the original bot used
- Gmail: Recommended. Drafts every email, reads replies and support email, and compares sent mail with drafts. Sends only when you say send.
- Google Calendar: Required for the call routines. Finds watched calls, and books calls after your yes.
- Granola: Optional. Call notes for learnings and follow-ups. Pasted notes work too.
- Google Sheets: Optional. Lead lists, usage or credit exports, and your roster sheet.
- Slack: Optional. Reads launch channels for heads-ups. Read only.
- X: Optional. Finds handles and reads posts. Never follows, posts, or sends DMs. Reads bill your X API credits.
