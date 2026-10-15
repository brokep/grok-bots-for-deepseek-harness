# Import Bot
Brings your setup from Claude Cowork, Codex, ChatGPT, OpenClaw, and Hermes into Grok Bot, then creates the expert bots that cover it or adds to the bots you already have. Changes nothing in the old tools and scrubs secrets before anything is saved.
Converted from the Grok Bot marketplace template by Shub Gaur (@shubgaur): https://x.ai/bot/marketplace/bots/import-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/import-bot"
```

Then start a session and pick **Import Bot** in the preset selector. The bot's 20 skills come with the bundle.
