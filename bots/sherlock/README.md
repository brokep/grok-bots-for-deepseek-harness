# Talent Discovery
Finds candidates for open roles that match your criteria and aren't already in your ATS.
Converted from the Grok Bot marketplace template by Tommy Hansen (@TommyHansenTA): https://x.ai/bot/marketplace/bots/sherlock

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/sherlock"
```

Then start a session and pick **Talent Discovery** in the preset selector. The bot's 9 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Daily candidate batch**: Every weekday morning, sources a small batch of new candidates for the open role, deduped against your pipeline, with evidence and a source link on every card.
- **Weekly sourcing recap**: Every Friday, a recap of who was added, what you kept and passed on, who has not replied yet, and whether the bar needs to move.

## Integrations the original bot used
- slack: Post new candidates to the hiring channel your team already reads.
- notion-workspace: Keep the role scorecard and the shortlist where your hiring team already looks.
- linear: Track the search, or each candidate, as issues if your team runs hiring in Linear.
- figma: Read a designer's shared case study or portfolio file when you are hiring design.
- Gmail: Search, read, draft, and manage email.
- Google Sheets: Read and write Google Sheets.
- Ashby: Search candidates, prep interviews, and manage pipeline tasks.
