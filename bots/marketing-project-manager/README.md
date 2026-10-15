# Project Manager
Turns a campaign or launch goal into a dated plan across research, positioning, landing pages, ads, and analytics, then tracks every work item, chases status with screenshots, and runs the merge and spend gates. Never merges, publishes, or spends, and never approves on your behalf.
Converted from the Grok Bot marketplace template by Josh Kim (@joshkim): https://x.ai/bot/marketplace/bots/marketing-project-manager

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/marketing-project-manager"
```

Then start a session and pick **Project Manager** in the preset selector. The bot's 7 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekday status check-in**: Disabled by default. Weekdays at 9am in the user's timezone (the user can pick a different time or cadence). Runs one status pass across the workstreams, attaches a screenshot for every artifact it names, chases anything past its date once, and lists the gates waiting on the user. Quiet when nothing moved.
- **Friday week ahead**: Disabled by default. Fridays at 4pm in the user's timezone. Lists what is due in the next 7 days, what the user has to decide to keep the date, and what is already late, read from the plan and the work items. Quiet when nothing is due and nothing is late.

## Integrations the original bot used
- Linear: Optional. Read and write the work items for this campaign when the team already tracks work there. A plain list in this chat works instead.
- Notion: Optional. The plan page, the positioning document, and the ad copy review document when the team keeps them there. A file under /workspace/pm/ works instead.
- Slack: Optional. Deliver the status pass to a channel you name instead of this chat, and read the project channel for what moved. Never a destination for a gate, which is always asked in this conversation.
- Google Drive: Optional. Where briefs, positioning documents, ad copy review documents, and the exports behind the ads and analytics workstreams live. Read and write, no secrets.
- Google Calendar: Optional. Reads the launch date, the review meetings, and the days the user is away, so the schedule and the gate dates are real. Read only.
