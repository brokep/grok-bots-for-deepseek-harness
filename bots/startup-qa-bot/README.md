# Startup QA Bot
Walks your product every weekday in its own test account and tells you what shipped, what got unshipped, what broke (with repro steps and screenshots), and which calls need you. Reads its own verification emails or takes pasted codes, and never touches real data.
Converted from the Grok Bot marketplace template by Shub Gaur (@shubgaur): https://x.ai/bot/marketplace/bots/startup-qa-bot

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/startup-qa-bot"
```

Then start a session and pick **Startup QA Bot** in the preset selector. The bot's 5 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Morning product walk**: Disabled by default. Weekday mornings, ready by 9: walks your product in its test account and sends what shipped, what got unshipped, what broke, and the calls to make.

## Integrations the original bot used
- AgentMail: Recommended. An inbox only I use for the test account, so I sign up and read its verification emails myself. I only create that inbox and read it, never send. Without it, you paste me the codes.
- GitHub: Optional. Merged pull requests tell me what should be live before I walk. Read-only. Without it, I use your changelog page or just walk.
- Linear: Optional. Issues moved to done tell me what should have shipped. Read-only, and I never file or change issues.
