# Performance Marketer
Turns approved ad copy into paused campaign shells for messaging tests in the ad platforms the user signs in to, with a review sheet they approve first and a screenshot per step. Never enables a campaign, raises a budget, adds a payment method, or spends without an explicit yes.
Converted from the Grok Bot marketplace template by Josh Kim (@joshkim): https://x.ai/bot/marketplace/bots/performance-marketer

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/performance-marketer"
```

Then start a session and pick **Performance Marketer** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Traffic watch**: Disabled by default. Daily at 9am in the user's timezone. Reads every enabled campaign in the signed-in platform against its test plan and its spend cap, attaches the screenshots behind the numbers, pauses at the total cap, and says nothing at all when no campaign is enabled.

## Integrations the original bot used
- Google Sheets: Recommended. The review sheet lives here so you can edit it, set Keep, Edit, or Cut per row, and approve it. Without it the same sheet is written as Markdown in chat.
- Google Drive: Optional. Reads the ad copy and positioning documents a teammate or you put in Drive. A paste in chat works just as well.
- Slack: Optional. Deliver the traffic read to a channel you name instead of this chat. Read and post only to what you name, and nothing is enabled from there.
