# EBR & Value Deck Builder
Builds an executive business review or value deck for a named account from your CRM, call history, and usage data, on your brand, and hands you an editable file. Never invents a number, and nothing goes to the customer without your yes.
Converted from the Grok Bot marketplace template by Krista Letz (@kristaletz): https://x.ai/bot/marketplace/bots/ebr-value-deck-builder

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/ebr-value-deck-builder"
```

Then start a session and pick **EBR & Value Deck Builder** in the preset selector. The bot's 5 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Renewal deck reminder**: On the 1st of each month, list the owner's accounts with a renewal inside 120 days that have no review deck this quarter, and offer to build each one.

## Integrations the original bot used
- Salesforce: Account, contract, contacts, and history the deck is built from. Connect the one CRM you use.
- HubSpot: CRM alternative to Salesforce.
- Attio: CRM alternative to Salesforce.
- Gong: What the customer said they wanted, in their words, for the goals and outcomes slides.
- Mixpanel: Adoption and usage trends for the account's domain.
- Google Drive: Upload the finished deck next to the account's other files.
- OneDrive: Upload destination for Microsoft 365 users.
