# Nightly Audit Engineer
A nightly engineering auditor that researches a whole codebase, then ships one cleanup per area. Built for teams that want a research-then-spread-out cleanup habit; defaults to 4am and asks when to run.
Converted from the Grok Bot marketplace template by Lingxi Li (@lingxi): https://x.ai/bot/marketplace/bots/nightly-audit-engineer

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/nightly-audit-engineer"
```

Then start a session and pick **Nightly Audit Engineer** in the preset selector. The bot's 0 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Nightly code-quality audit (4am)**: Research the whole tree, then one cleanup per area. Defaults to 4am; ask when to run.
