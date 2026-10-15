# Competitor Watch
Tracks competitor pricing, product, and hiring pages and briefs you on real changes. Starts from a list of URLs you paste.
Converted from the Grok Bot marketplace template by Shimecki (@scheemunai): https://x.ai/bot/marketplace/bots/competitor-watching

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/competitor-watching"
```

Then start a session and pick **Competitor Watch** in the preset selector. The bot's 5 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly competitor brief**: Every Monday morning, diffs the pages on the watch list against the last snapshot and delivers a brief of what changed with a source link on every line.
- **Daily launch check**: Each weekday morning, checks changelog, release note, and blog pages across the watch list and speaks up only when a competitor ships something.

## Integrations the original bot used
- slack: Post the weekly brief to a channel you choose.
- notion-workspace: Keep the watch list and every brief where your team reads.
- linear: Turn a competitor move into an issue in your product backlog.
