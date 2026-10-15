# Video Editor
Edits short vertical talking-head videos from your raw footage: picks the best takes, captions what you actually said, and adds B-roll, motion graphics, and music. Sends an edit plan for your yes before cutting, checks every cut for sync and glitches, and never posts.
Converted from the Grok Bot marketplace template by Ethan Ng (@Ethan_Ng_13): https://x.ai/bot/marketplace/bots/video-editor

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/video-editor"
```

Then start a session and pick **Video Editor** in the preset selector. The bot's 5 skills come with the bundle.

## Integrations the original bot used
- Remotion: Optional. Remotion's own skills for animations, captions, and rendering, used for the graphics in each edit.
- Google Drive: Optional. Pull raw footage from Drive and share preview links of finished cuts.
