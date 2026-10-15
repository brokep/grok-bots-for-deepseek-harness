# Ad Spend Watch
Watches your ad spend and performance and flags what's breaking before it burns budget. Works from a pasted export, and never pauses a campaign without your yes.
Converted from the Grok Bot marketplace template by Miguel Cruz (@cruzmiguel000): https://x.ai/bot/marketplace/bots/fuse

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/fuse"
```

Then start a session and pick **Ad Spend Watch** in the preset selector. The bot's 9 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily spend and performance check**: Every weekday morning, checks the newest ad numbers against your thresholds and flags what broke, with the one change to make on each urgent line.
- **Midday burn check**: Every weekday around midday, catches a spend spike the same day it happens, but only when a live source is connected.
- **Weekly budget pace check**: Every Monday morning, where month-to-date ad spend lands against your plan and which accounts are going to overshoot.

## Integrations the original bot used
- slack: Post an alert or a fix list in the channel your team actually watches.
- notion-workspace: Keep the threshold set, the checks, and the alert log where your team can find them.
- linear: File the fix when a breach belongs to engineering, like a dead pixel or a broken checkout.
- hex: Read spend straight from your warehouse when the numbers already live in a query.
- datadog: Check whether the site or checkout was down or slow when conversions dropped.
- sentry: Check whether checkout errors spiked at the hour your conversions stopped.
- figma: Pull up the creative behind a campaign whose click-through rate is sliding.
- Gmail: Read the daily report the ad platform emails you.
- Google Sheets: Read a spend sheet you already keep.
