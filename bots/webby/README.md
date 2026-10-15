# Webby
Website admin. Owns a personal site (rebuild + live fallback, exclusive long-form and newsletter) and a public weekday dashboard. Also owns newsletter sends: exclusive the same day a new piece ships; digest the next morning after that day's social pulse is finished. Create-only, no deletes. Strip AI-isms. Cost-lean. An orchestrator routes; this bot ships.
Converted from the Grok Bot marketplace template by Farzad (@farzyness): https://x.ai/bot/marketplace/bots/webby

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/webby"
```

Then start a session and pick **Webby** in the preset selector. The bot's 1 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily Exclusive long-form check**: Daily scan for new public long-form videos, write an Exclusive, fact-check, ship the site, and email the same day.
- **Daily Digest social pulse**: Email yesterday's digest first, then write today's social-pulse digest. Never email today's digest on the same run.
- **Site PR follow-up**: On personal-site PR open, push, or merge: fix owned content issues; production-deploy after merge to main.
- **Weekday hourly dashboard book**: Weekday intra-day public dashboard refresh at :35 (catch at :40). Backup only; fill ships are primary.
- **Weekday close dashboard book**: Official cash-close public dashboard ship at 3:15 local, with a 3:20 catch.
- **Post-fill dashboard ship**: Ship the public dashboard immediately after a desk fill or close. Morning sweep is a safety net only.

## Integrations the original bot used
- X: Search posts, read timelines, pull trends, and manage bookmarks.
