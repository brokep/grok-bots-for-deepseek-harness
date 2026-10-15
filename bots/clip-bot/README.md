# Clip Bot
Finds the best moments in a long recording and cuts them into short captioned clips. Works from an upload or a link, with transcript and timestamps on every clip.
Converted from the Grok Bot marketplace template by This Week in AI (@ThisWeeknAI): https://x.ai/bot/marketplace/bots/clip-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/clip-bot"
```

Then start a session and pick **Clip Bot** in the preset selector. The bot's 6 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Clip queue pass**: Every weekday morning, transcribes any new recording waiting in the clip queue and comes back with the moments worth cutting.
- **Friday clip recap**: Every Friday, a short recap of what got clipped this week, which strong moments are still uncut, and the three worth cutting next.

## Integrations the original bot used
- slack: Drop the moment list and finished clips in the channel your team picks from.
- notion-workspace: Keep transcripts, moment lists, and the clip log where your team looks things up.
- linear: Turn approved moments into clip tasks your team can track to done.
- figma: Pull title cards, end cards, and caption styling so clips match your brand.
