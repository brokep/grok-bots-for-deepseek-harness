# Credit Card Max
Credit card maxing with live Grok Finance (Plaid): which card to swipe given your priorities (points, cash back, airline/hotel status), statement-credit tracking with muteable expiry nags, wrong-card recurring flags, and a monthly points-and-perks rollup — not budgeting.
Converted from the Grok Bot marketplace template by Trevin Chow (@trevin): https://x.ai/bot/marketplace/bots/credit-card-max

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/credit-card-max"
```

Then start a session and pick **Credit Card Max** in the preset selector. The bot's 2 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Monthly card rollup**: Fires on the 1st of each month to deliver a perk-maximization rollup (not a budget review).
- **Perk expiry watch**: Runs daily to nag only on T-5 and period-end for unmuted unused watched perks; silent otherwise.
- **Wrong-card recurring watch**: Runs weekly to flag recurring charges on a suboptimal card; silent when the queue is clean.
