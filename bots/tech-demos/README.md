# Tech Demos
Weekday X-bookmark scout that picks one new library to demo, asks for approval, then plans and builds it in a sticky monorepo with a Cursor cloud agent. For anyone who wants a daily public-tech playground, not a changelog digest.
Converted from the Grok Bot marketplace template by Matt Palmer (@mattyp): https://x.ai/bot/marketplace/bots/tech-demos

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/tech-demos"
```

Then start a session and pick **Tech Demos** in the preset selector. The bot's 1 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily X tech scout**: Weekdays at 9:00 AM. Lands paused on import.

## Integrations the original bot used
- X: Search posts, read timelines, pull trends, and manage bookmarks.
