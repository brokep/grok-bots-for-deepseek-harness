# Distro Bot
Runs your marketing loop end to end: campaigns on your ad accounts, fresh creative, real channel analysis, timely posts from X and web scans, and outbound until a lead replies. Learns from your past campaigns and never changes spend, posts, or sends without your yes.
Converted from the Grok Bot marketplace template by Shub Gaur (@shubgaur): https://x.ai/bot/marketplace/bots/distro-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/distro-bot"
```

Then start a session and pick **Distro Bot** in the preset selector. The bot's 7 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Campaign check**: Disabled by default. Daily 8:25am: numbers, pacing, flags, and one loop step per campaign.
- **Trend scan**: Disabled by default. Weekdays 9:35am: topics worth jumping on, each with a draft post.
- **Outbound replies**: Disabled by default. Weekdays 11:15am and 4:15pm: replies handed to sales, follow-ups drafted.
- **Weekly distro review**: Disabled by default. Mondays 8:45am: every channel's numbers, competitor moves, and this week's tests.

## Integrations the original bot used
- X: Recommended. Trends, news, and posts for topic scans, plus your own posts' numbers to learn from. Read only, and reads bill your X API credits.
- Gmail: Optional. Outbound drafts in your inbox, replies from leads, and past emails to learn from. Sends only a batch you approve.
