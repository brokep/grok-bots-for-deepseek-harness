# Stalk Bot
Signs up for your competitors' newsletters and products under its own research email, walks their onboarding on video, and watches their site, pricing, changelog, jobs, and X. Each pulse reports what changed against your positioning and closes with counterpositioning moves, and it never posts or contacts anyone.
Converted from the Grok Bot marketplace template by Shub Gaur (@shubgaur): https://x.ai/bot/marketplace/bots/stalk-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/stalk-bot"
```

Then start a session and pick **Stalk Bot** in the preset selector. The bot's 19 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Competitor pulse**: Disabled by default. Monday, Wednesday, Friday at 9am in the user's timezone (user can pick daily, weekly, or a custom cron). Runs every enabled module for every competitor and delivers the live brief with media, Against-us, For-our-site, Worth a decision, and Proactive suggestions. Quiet when nothing changed.
- **Weekly deep dive**: Disabled by default. Friday 10am, one competitor in rotation. Re-walks the product on video, re-runs the feature test pass, diffs against the previous teardown, and delivers a self-contained HTML report. Report only.
- **Competitor churn watch**: Disabled by default and only useful once a churn source is named. Weekdays at 10am in the user's timezone. Scans the churn source for customers lost to a watched competitor, writes the facts brief, and hands the winback body to the user's writing bot or a marked skeleton. Never sends. Quiet when there are no new cases.

## Integrations the original bot used
- AgentMail: Preferred. Research inboxes for newsletters, trials, and sales sequences. Create inboxes and read mail via the plugin MCP.
- X: Needed for the X radar and complaint mining modules. Read-only: posts, mentions, replies for competitor and founder handles.
- Gmail: Fallback only. Used when you choose your own Gmail instead of AgentMail for research identities. Puts newsletters and trials on your address.
- Slack: Optional. Deliver the pulse to a channel you name instead of this chat.
- Salesforce: Optional, churn module only. Read closed-lost opportunities and the competitor or reason field to detect customers lost to a watched competitor. Read only. A sheet or a paste works instead.
- Google Sheets: Optional, churn module only. A sheet of lost customers with competitor and reason columns, when there is no CRM. Read only.
