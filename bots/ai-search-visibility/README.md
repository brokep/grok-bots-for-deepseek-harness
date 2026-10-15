# AI Search Visibility
Checks whether AI assistants and Google recommend you, and who they name instead. Starts from a handful of questions your buyers actually ask.
Converted from the Grok Bot marketplace template by Adam Tanguay (@adamta): https://x.ai/bot/marketplace/bots/ai-search-visibility

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/ai-search-visibility"
```

Then start a session and pick **AI Search Visibility** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly visibility brief**: Every week, runs the whole prompt list, then reports which answers moved, who is winning, and the one thing to do about it.
- **Top prompt spot check**: Twice a week, re-runs the top five prompts and speaks up only when the user drops out of an answer or a new name shows up.

## Integrations the original bot used
- slack: Post the weekly brief in a channel your team already reads.
- notion-workspace: Keep the prompt list, the briefs, and the fix list where your team looks things up.
- linear: Turn the fix list into tracked issues for whoever owns those pages.
- hex: Chart the share of answer scoreboard over time if your team already uses Hex.
- Profound: Read AI answer visibility and citations across engines to widen the capture.
- Google Sheets: Read and write Google Sheets.
