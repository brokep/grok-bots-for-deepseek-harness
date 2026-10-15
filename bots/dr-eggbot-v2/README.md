# dr eggbot
Designs high-quality Grok Bots. Asks a few preference questions, then creates them with CreateAgent. Coding bots get the poteto-mode bar (one job, unslopped, verified). Non-coding bots get the same tightness: one job, one voice, explicit anti-jobs, no leftover tools. Casual, a little mad-scientist, short lowercase. Bias to act once the job is clear. Does not default to shareable templates.
Converted from the Grok Bot marketplace template by Lauren Tan (@poteto): https://x.ai/bot/marketplace/bots/dr-eggbot-v2

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/dr-eggbot-v2"
```

Then start a session and pick **dr eggbot** in the preset selector. The bot's 4 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **transcript-healthcheck**: Cron 44 8 * * 1-5 (weekdays 8:44 local). Scans recent bot transcripts for user friction; proposes skills/bots/routines; stays quiet when nothing is worth proposing.
- **routine-healthcheck**: Cron 49 8 * * 1 (Mondays 8:49 local). Audits fleet routines for token waste; reports fixes; stays quiet when nothing is worth proposing.

## Integrations the original bot used
- pstack: if you want to go fast, go deep first. pstack helps you write less, but higher quality code. rigorous agent workflows you can parallelize with confidence.
