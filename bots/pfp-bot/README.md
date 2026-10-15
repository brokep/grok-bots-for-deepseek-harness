# Pfp Bot
Turns your X photo, an upload, a selfie, or a pet pic into a tiny Grokbot-style icon with capsule eyes that keeps the hair, colors, and signature look. Style and prompt by @Multi_Serio_Ai.
Asks for more photos when unsure, and never makes realistic likenesses or posts anything.
Converted from the Grok Bot marketplace template by Shub Gaur (@shubgaur): https://x.ai/bot/marketplace/bots/pfp-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/pfp-bot"
```

Then start a session and pick **Pfp Bot** in the preset selector. The bot's 8 skills come with the bundle.

## Integrations the original bot used
- X: Optional. Reads your X profile photo and handle directly, so nothing needs typing. Without it, I fetch your public profile photo from the handle you type.
