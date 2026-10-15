# X Brief
Turns the accounts and topics you pick on X into one short daily brief. Reads your X connection or handles you paste, and never posts on your behalf.
Converted from the Grok Bot marketplace template by Dan McAteer (@daniel_mac8): https://x.ai/bot/marketplace/bots/x-brief

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/x-brief"
```

Then start a session and pick **X Brief** in the preset selector. The bot's 6 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily X brief**: Once a day at the hour you pick, reads your watch list and sends the day's items grouped by theme with a link on every line.
- **Weekly X recap**: Every Friday, pulls the week's briefs into the themes that held, the voices worth adding, the accounts that went quiet, and what to read this weekend.

## Integrations the original bot used
- X: Read your timeline, lists, and the accounts you follow, and open posts reliably.
- slack: Post the daily brief to a channel you and your team already read.
- notion-workspace: Keep the watch list and every brief where your team looks things up.
- linear: Turn anything in the brief you want to act on into a task with the link on it.
