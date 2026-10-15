# Signal Prospector
Finds the accounts and people in your CRM and product data that just showed intent, ranks them, and drafts the first touch. Runs on a schedule, explains every signal, and nothing sends without your yes.
Converted from the Grok Bot marketplace template by Krista Letz (@kristaletz): https://x.ai/bot/marketplace/bots/signal-prospector

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/signal-prospector"
```

Then start a session and pick **Signal Prospector** in the preset selector. The bot's 5 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Monday signal digest**: Every Monday morning, scan the week's signals across the owner's book, rank the accounts and contacts, and stage first-touch drafts for review.

## Integrations the original bot used
- Salesforce: Leads, contacts, campaign responses, activities, and ownership. Connect the one CRM you use.
- HubSpot: CRM alternative to Salesforce; form fills and email engagement count as signals.
- Attio: CRM alternative to Salesforce; lists and notes carry the signals.
- Mixpanel: Product signups, activation, and usage spikes by company domain.
- X: Public posts from the account and its leaders, for a dated hook the signal scan can cite.
- Hunter: Finds and verifies business emails for ranked contacts who are not in the CRM yet.
- Clay: Enrichment for titles, seniority, and company facts when you already run Clay.
- Gmail: Saves first-touch drafts and learns the owner's voice. Use Outlook instead on Microsoft 365.
- Slack: Deliver the signal digest as a DM.
