# Apple Search Ads Review
Reviews your Apple Search Ads spend against your cost per install target. Drafts the keyword, bid, and budget changes, and never touches your account.
Converted from the Grok Bot marketplace template by Chris Everett (@): https://x.ai/bot/marketplace/bots/apple-search-ads-review

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/apple-search-ads-review"
```

Then start a session and pick **Apple Search Ads Review** in the preset selector. The bot's 7 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly ad review**: Every week on the user's chosen morning, a read on last week's Apple Search Ads spend against target, with the changes worth making first.
- **Daily spend check**: Each weekday morning, checks for a new export and speaks up only about groups over target or spending with nothing to show.

## Integrations the original bot used
- slack: Post a review you approved to the channel your growth team already reads.
- notion-workspace: Keep the targets sheet and every review where your team looks things up.
- hex: Pull spend and install numbers straight from your warehouse when they are modeled there.
- Databricks SQL: Query your Apple Search Ads reports straight from the warehouse instead of an export.
- linear: Turn an approved change list into tasks for whoever holds ad account access.
- Gmail: Search, read, draft, and manage email.
- Google Sheets: Read and write Google Sheets.
