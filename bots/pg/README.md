# Outbound Prospecting
Finds prospects that match your ideal customer, then drafts a first message to each one. Every name is researched on the public web, and nothing sends without your yes.
Converted from the Grok Bot marketplace template by Krista Letz (@kristaletz): https://x.ai/bot/marketplace/bots/pg

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/pg"
```

Then start a session and pick **Outbound Prospecting** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekday draft batch**: Every weekday morning, researches the next few names on the target list and leaves a first-touch draft for each one, waiting on your yes.
- **Friday prospecting recap**: Every Friday, what went out this week, what came back, which rows are waiting on you, and where the list is running thin.
- **Monday list top-up**: Every Monday, adds new companies and named people that match your ideal customer so the list never runs dry.

## Integrations the original bot used
- slack: Post the day's drafts or the Friday recap to a channel your team reads.
- notion-workspace: Keep the target list and every draft where your team looks things up.
- linear: Turn a reply or a booked meeting into a task somebody owns.
- Gmail: Every draft sits unsent in your own account until you send it.
- Google Sheets: Keep the target list somewhere you can edit directly.
- X: Read a prospect's recent posts for a real, dated hook when X is your channel.
- Salesforce: Read who you already know so the list drops open deals and customers.
