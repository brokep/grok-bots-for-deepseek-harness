# Product Marketer
Learns your product, brand, and market, turns competitive research into positioning principles every message is measured against, and drafts landing page, ads, and email copy that holds to them. Drafts only, and never publishes, sends, or spends.
Converted from the Grok Bot marketplace template by Josh Kim (@joshkim): https://x.ai/bot/marketplace/bots/product-marketer

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/product-marketer"
```

Then start a session and pick **Product Marketer** in the preset selector. The bot's 9 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Principles review**: Disabled by default. Mondays at 9am in the user's timezone. Re-reads the positioning principles doc and the voice profile, collects new comments and open gaps, and flags copy that drifted from the current rev with the line before and after. Reports in chat, draft only, and stays quiet when nothing changed.

## Integrations the original bot used
- Google Drive: Optional. Reads the brand, positioning, and messaging docs you already have, and holds the principles doc, the voice profile, every draft, and every brief as Markdown. Without it everything is delivered in chat.
- Google Sheets: Optional. Where the ads copy set lives as a live sheet with the Overview, RSA long format, Keywords, and Callouts tabs. Without it the same tables ship as CSV to Drive or as Markdown in chat.
- Notion: Optional. Reads the brand, product, and positioning pages you point me at, and can hold the principles doc and drafts instead of Drive.
- X: Optional and read only. Reads how you and your competitors position the category in public, for the claim map in sharpen-positioning. Never follows, likes, reposts, replies, posts, or sends a DM.
