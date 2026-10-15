# Stills & Clips Desk
Pulls stills, thumbnails, and short clips out of your footage, sized for where they go. Cleans up screenshots for docs too, and writes the caption and alt text.
Converted from the Grok Bot marketplace template by Matt Palmer (@mattyp): https://x.ai/bot/marketplace/bots/image-gen-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/image-gen-bot"
```

Then start a session and pick **Stills & Clips Desk** in the preset selector. The bot's 6 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly pull queue**: Every week, works through the stills and clips waiting in the pull queue and posts each finished file here for review.

## Integrations the original bot used
- slack: Drop a pulled still or clip in the channel where your team gives feedback.
- notion-workspace: Keep the size sheet and the cleaned-up docs screenshots where your team looks things up.
- figma: Read the real logo file, hex codes, and font for anything that gets an overlay.
- linear: Pick up asset requests filed as issues and feed them into the weekly pull queue.
