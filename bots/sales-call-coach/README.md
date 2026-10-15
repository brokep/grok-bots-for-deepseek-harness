# Sales Call Coach
Scores your sales calls and tells you what to fix before the next one. Works from a pasted transcript or an uploaded recording.
Converted from the Grok Bot marketplace template by Daniel Brill (@danielbrill_): https://x.ai/bot/marketplace/bots/sales-call-coach

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/sales-call-coach"
```

Then start a session and pick **Sales Call Coach** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly coaching recap**: Once a week, reads the calls you logged and sends the counts that moved, the two weakest dimensions with quotes, and the one habit to work on next.
- **Objection drill**: On the mornings you pick, runs one short live drill on the objection that keeps costing you, using wording from your own calls.

## Integrations the original bot used
- notion-workspace: Keep your coaching log, scorecards, and pre-call plans where you already work.
- slack: Send a scorecard or a follow-up draft to yourself or your manager, only when you say so.
- linear: File the product gaps buyers name on your calls as issues, only when you say so.
- Gong: Pull your call recordings and transcripts straight from Gong instead of pasting them.
- Google Calendar: See the calls coming up so a pre-call plan is ready before you dial in.
