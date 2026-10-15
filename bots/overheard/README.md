# Overheard
Watches Reddit, Hacker News, news sites, and X for third-party mentions of your name, brand, and URLs, then sends a short weekday digest when something clears the bar. Stays quiet on dead days and never posts on your behalf.
Converted from the Grok Bot marketplace template by Lenny Rachitsky (@lennysan): https://x.ai/bot/marketplace/bots/overheard

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/overheard"
```

Then start a session and pick **Overheard** in the preset selector. The bot's 2 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily mention monitor**: Paused weekday-morning mention sweep. Created after the watch-list interview. Enable only when the user says so. Digests third-party hits in chat and stays quiet on dead days.

## Integrations the original bot used
- X: Search posts and read accounts on X. Optional, improves X coverage over web search.
- Slack: Optional. Deliver the weekday digest to a Slack channel you approve.
