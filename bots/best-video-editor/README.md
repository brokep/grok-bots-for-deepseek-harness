# Video Edit Desk
Turns uploaded footage into cut clips, burned-in captions, and platform-sized exports. Works from your notes and never overwrites the original.
Converted from the Grok Bot marketplace template by X Freeze (@xfreeze): https://x.ai/bot/marketplace/bots/best-video-editor

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/best-video-editor"
```

Then start a session and pick **Video Edit Desk** in the preset selector. The bot's 6 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly cut queue**: Once a week, finishes the cuts the user parked, attaches them here, and asks the one question each stuck job needs.

## Integrations the original bot used
- slack: Drop a cut you approved in the channel that reviews it.
- notion-workspace: Keep the shot notes and the cut log where your team looks.
- linear: Pick up edit requests filed as issues and put the finished cut back on the issue.
- figma: Pull a title card, lower third, or thumbnail frame out of your brand file.
