# Customer Proof Desk
Turns call notes and transcripts into case studies, testimonials, and proof points. Quotes stay word for word from what you paste, and nothing publishes without your yes.
Converted from the Grok Bot marketplace template by Anoop Baliga (@akbaliga96): https://x.ai/bot/marketplace/bots/customer-stories

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/customer-stories"
```

Then start a session and pick **Customer Proof Desk** in the preset selector. The bot's 11 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly proof roundup**: Every Monday morning, what new proof came in, which customers are ready for a case study, which approvals are still sitting, and which claims have nothing behind them.
- **Monthly proof refresh**: Once a month, the quotes and numbers that have aged out, the customers worth a fresh call, and the claims with the thinnest proof behind them.

## Integrations the original bot used
- notion-workspace: Keep the proof bank, the case studies, and the drafts where your team already looks.
- slack: Watch the channel where customer wins get posted, and drop the Monday roundup there.
- linear: Track ready-to-write customers and pending approvals as tasks your team can see.
- figma: Lay a finished case study into a page design instead of handing over raw text.
- hex: Check a customer's numbers against your own data before you publish them.
- Gmail: Search, read, draft, and manage email.
- Granola: Pull customer call notes straight from your meetings.
