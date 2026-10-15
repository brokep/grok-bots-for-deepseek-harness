# tinkabot
Wraps an API into a Cursor/Agent Plugin (MCP + skills). Data shape first, smallest scaffold that works, prove locally, then ask once for affiliation and publish to Marketplace or cursor.directory.
Converted from the Grok Bot marketplace template by Lauren Tan (@poteto): https://x.ai/bot/marketplace/bots/tinkabot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/tinkabot"
```

Then start a session and pick **tinkabot** in the preset selector. The bot's 3 skills come with the bundle.

## Integrations the original bot used
- pstack: if you want to go fast, go deep first. pstack helps you write less, but higher quality code. rigorous agent workflows you can parallelize with confidence.
