# Proto Bot
Turns your daily ideas into live, shareable prototypes in your real app, built as draft pull requests with click-path screenshots and a short video, plus Figma mocks, images, and memes on the side. Never merges, publishes, or shares without your yes.
Converted from the Grok Bot marketplace template by Shub Gaur (@shubgaur): https://x.ai/bot/marketplace/bots/proto-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/proto-bot"
```

Then start a session and pick **Proto Bot** in the preset selector. The bot's 9 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Prototype rundown**: Disabled by default. Weekday mornings at 9: packets for builds that finished, results of media jobs, and briefs for queued ideas, waiting for your yes.
- **Craft scan**: Disabled by default. Mondays at 10: new models, techniques, and guides for the crafts you name, with links.

## Integrations the original bot used
- Figma: Optional. Reads your files for references and design reviews, and draws mocks, screens, and decks when a cloud agent can't.
- Slack: Optional. Reads a thread you point at so a prototype starts from the real discussion. Posts only a draft you approve.
- X: Optional. Searches posts and threads for craft research. Web search works without it.
