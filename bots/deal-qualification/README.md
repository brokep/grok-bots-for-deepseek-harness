# Deal Inspector
Checks every deal that moved stage against your qualification criteria using the actual call transcripts. Quotes the evidence, flags what is missing, recommends promote or close, and proposes the CRM updates for your approval.
Converted from the Grok Bot marketplace template by Jon Grigull (@): https://x.ai/bot/marketplace/bots/deal-qualification

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/deal-qualification"
```

Then start a session and pick **Deal Inspector** in the preset selector. The bot's 4 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Friday stage audit**: Every Friday afternoon, audit each of the owner's opportunities that was created or moved stage this week against the qualification framework and stage the CRM updates.

## Integrations the original bot used
- Gong: Call transcripts, the evidence behind every criterion. Granola works too.
- Granola: Transcript source for meetings your recorder did not capture.
- Salesforce: Opportunities, stage history, and the qualification fields the audit fills. Connect the one CRM you use.
- HubSpot: CRM alternative to Salesforce.
- Attio: CRM alternative to Salesforce.
- Slack: Deliver the weekly audit as a DM.
- Gmail: Checks whether we did what we promised on the last call.
- Notion: Keep audits and the framework definitions where your team already looks.
- Google Sheets: Export the scorecards when your team tracks them in a sheet.
