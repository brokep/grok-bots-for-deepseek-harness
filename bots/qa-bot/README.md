# QA bot
Acts as your QA on the live deploy: runs the acceptance checklist and says pass or fail before you ship.
Converted from the Grok Bot marketplace template by Ulysses Ng (@): https://x.ai/bot/marketplace/bots/qa-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/qa-bot"
```

Then start a session and pick **QA bot** in the preset selector. The bot's 3 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Post-merge AC fail-gate**: When a PR merges in the watched product repo, verify Production SHA and re-run the BLOCK AC pack; stay quiet on unchanged PASS.

## Integrations the original bot used
- Vercel: Build and deploy web apps and agents
