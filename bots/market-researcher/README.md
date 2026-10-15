# Market Researcher
Tracks how competitors market: their ads and creative, landing pages, offers, pricing, channel mix, search overlap, and content cadence, then delivers a weekly brief of what changed with screenshots and marketing counter-moves. Never posts, contacts anyone, signs up for anything, or spends on ads.
Converted from the Grok Bot marketplace template by Josh Kim (@joshkim): https://x.ai/bot/marketplace/bots/market-researcher

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/market-researcher"
```

Then start a session and pick **Market Researcher** in the preset selector. The bot's 10 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly marketing brief**: Disabled by default. Monday at 8am in the user's timezone, or any day and time the user picks. Checks every competitor's ads, landing pages and offers, pricing and promotions, channel mix, search overlap, and content, then delivers what moved with screenshots, Against our marketing, and 2 to 5 counter-moves. Quiet when nothing moved.
- **Monthly strategy read**: Disabled by default. The 1st of the month at 10am in the user's timezone. Rolls the month of weekly briefs and the user's own traffic, query, and auction numbers into where the market moved, where the marketing is exposed, and 2 to 4 ranked moves marked adjust or pivot. Recommendation only.

## Integrations the original bot used
- X: Recommended. Reads competitor company and product handles for post volume, engagement, themes, and promoted copy being tested in public. Read only, it never follows, likes, reposts, replies, posts, or sends a DM.
- Google Sheets: Optional. Holds the swipe file index, the promotion calendar, the search overlap table, and the messaging matrix when the user wants them outside chat, and is one place an ad or search export can live. A paste works instead.
- Google Drive: Optional. The folder where ad platform, analytics, or search console CSV exports are dropped for the runs when a platform is not signed in. Read only. A paste works instead.
- Slack: Optional. Delivers the weekly brief and the strategy read to a channel the user names instead of this chat.
