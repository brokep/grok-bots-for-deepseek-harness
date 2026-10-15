# figma bro
Turns a Figma frame into a build spec, and audits your components, tokens, and motion. Builds screens from a brief too, and works from a pasted link when Figma isn't connected.
Converted from the Grok Bot marketplace template by John Bai (@johnbai): https://x.ai/bot/marketplace/bots/figma-bro

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/figma-bro"
```

Then start a session and pick **figma bro** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly library check**: Every Monday morning, checks the component library and token set for new duplicates, detached instances, and hardcoded values, and reports only what drifted since last week.
- **Ready for dev sweep**: Every Friday afternoon, lists the frames marked ready for dev that still have no spec, and offers to write the next one.

## Integrations the original bot used
- figma: Read your file directly: the layer tree, the components, the variables, the prototype, and the exact values.
- notion-workspace: Park specs and audits where your team already looks things up.
- linear: Turn handoff open questions and audit fixes into issues you approve first.
- slack: Drop a spec or a handoff note into the channel your engineers already read.
