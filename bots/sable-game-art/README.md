# Game Art Director
Turns a game concept into a style guide, palettes, and prompt sheets for your image tool. Slices sprite sheets and checks your art for palette and grid drift.
Converted from the Grok Bot marketplace template by Danny Limanseta (@DannyLimanseta): https://x.ai/bot/marketplace/bots/sable-game-art

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/sable-game-art"
```

Then start a session and pick **Game Art Director** in the preset selector. The bot's 6 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly art review**: Once a week, checks new art against the style guide and the spec, reports what drifted with the numbers behind it, and lists what is still missing from the shot list.
- **Weekly reference sweep**: Once a week, sends four to six fresh art references in the user's genre and style, each with a source link and what is worth taking from it.

## Integrations the original bot used
- figma: Read your mood board and mockups, and keep the style guide where your artists already work.
- notion-workspace: Keep the style guide, the spec, and the shot list where your team looks things up.
- slack: Post the weekly art review to the channel your team already reads.
- linear: Turn the shot list into issues so the art backlog sits with the rest of the work.
