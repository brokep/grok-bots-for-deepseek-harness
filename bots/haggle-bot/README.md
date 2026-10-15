# Haggle Bot
Inventories your SaaS spend from Ramp and bills, finds evidence-backed savings (unused seats, duplicates, cheaper alternatives), and drafts vendor counters for your review. Never spends, signs, or sends without you.
Converted from the Grok Bot marketplace template by Daniel Gartshein (@): https://x.ai/bot/marketplace/bots/haggle-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/haggle-bot"
```

Then start a session and pick **Haggle Bot** in the preset selector. The bot's 6 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Renewal window watch**: Disabled by default. Weekly scan of the vendor database for contracts renewing inside the priority window (default 120 days) that have no Focus tag or thesis yet.
- **Monthly inventory refresh**: Disabled by default. Monthly re-pull of Ramp cards and bills, diffed against the vendor database, with new vendors, spend changes, and dropped vendors flagged for review.

## Integrations the original bot used
- Ramp: Live card and bill spend. Primary source for the vendor inventory.
- Google Sheets: The vendor database and savings tabs live here.
- Gmail: Draft vendor RFQs and counters. Never sends without your go.
- Slack: Optional. Source for vendor owners and usage, and colleague DMs for data. Never posts without your go.
- Notion: Optional. Source for vendor owners, purpose, and usage notes.
- Google Drive: Optional. Contracts, order forms, and quotes for commitment evidence.
- Granola: Optional. Vendor call notes for sentiment and commitments.
