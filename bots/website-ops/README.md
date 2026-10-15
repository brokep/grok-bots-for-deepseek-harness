# Website Ops
Ships website changes as pull requests from your site repo with before and after screenshots in chat, and runs evidence backed audits of SEO, content, speed, accessibility, CRO, and schema. Never merges, deploys, changes DNS, or edits analytics without your explicit yes.
Converted from the Grok Bot marketplace template by Josh Kim (@joshkim): https://x.ai/bot/marketplace/bots/website-ops

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/website-ops"
```

Then start a session and pick **Website Ops** in the preset selector. The bot's 8 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Weekly site audit**: Disabled by default. Monday at 8am in the user's timezone. Re-audits the saved page list for SEO, links, speed, accessibility, CRO, and schema, diffs against the previous audit, and delivers only what is new, fixed, or regressed with a self contained report. Report only, quiet when nothing changed.

## Integrations the original bot used
- GitHub: Required. Clones the website repo, opens the branch and the pull request for every change, and reads the pull request checks for a preview URL. Never merges.
- Google Drive: Optional. Reads landing page briefs and picks up images or exports that belong on a page. A paste or an upload works instead.
- Slack: Optional. A destination for the weekly audit instead of this chat, when you name a channel. Read only otherwise.
- Figma: Optional. Reads the design reference a brief points at so a page matches the intended layout. Read only, and the repo's existing components still win.
