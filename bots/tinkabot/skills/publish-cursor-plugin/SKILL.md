---
name: publish-cursor-plugin
description: "Use when publishing a Cursor/Agent Plugin: ask once if they work at the company/service — yes → Marketplace, no/unsure → cursor.directory. Trust their answer; approve gate still blocks submit."
---

# publish-cursor-plugin

Part of the tinkabot agent preset.

---
name: publish-cursor-plugin
description: >-
  Use when publishing a Cursor/Agent Plugin: ask once if they work at the
  company/service — yes → Marketplace, no/unsure → cursor.directory. Trust their
  answer; approve gate still blocks submit.
---
# Publish a Cursor plugin

Pick the destination first. Do not submit until the owner approves.

## Route

Ask once: **do you work at / own the company or service this plugin is for?**

| Answer | Destination |
| --- | --- |
| Yes (or they insist they do) | Cursor Marketplace (https://cursor.com/marketplace/publish) |
| No / unsure | cursor.directory (https://cursor.directory/plugins/new) |

Trust their answer. Do not interrogate or dig for proof. If they insist they work there, route to Marketplace — the approve gate still controls whether anything is submitted.

Default when they skip or stay unsure: **community → cursor.directory**.

Never invent API keys or paste secrets into a form or chat.

Shared preconditions (both destinations):

- Valid root `plugin.json` (Agent) or `.cursor-plugin/plugin.json` (Cursor)
- Unique lowercase kebab-case `name`
- Clear `description`; components have valid frontmatter
- `README.md` covers usage and config
- Agent Plugins: every `${VAR}` in mcp config declared under `variables`
- Relative paths only (no `..`, no absolutes)
- Proven locally via prove-plugin-local
- Public GitHub repo with the plugin on the default branch

---

## A. Community → cursor.directory

Primary path when they say no / unsure. Listing flow (from cursor/community-plugins):

1. Public GitHub repo ready (create with `gh` / CloudAgent if needed; no secrets in the tree).
2. Open https://cursor.directory/plugins/new (owner signed in via GitHub or Google; cookie import / box help if the browser needs their session).
3. Paste the GitHub repo URL — the site auto-detects Open Plugins components (rules, MCP, skills, agents, hooks, LSP).
4. Preview what was detected. Fix the repo if detection misses something, then refresh.
5. **Approve gate** (widget): submit this plugin to cursor.directory now? → Submit / Hold off.
6. Only on Submit: click **Submit**. Report the listing URL or error text. On Hold off: leave the form filled, do not submit.

After submit: security scan / verification may run. If the listing sticks, tell the owner to email marketplace-publishing@cursor.com with plugin name, repo URL, and submit date — do not spam re-submit.

Specs: https://open-plugins.com/plugin-builders/specification · template: https://github.com/cursor/plugin-template

---

## B. Official → Cursor Marketplace

When they say yes (or insist). Affiliation is self-attested; Cursor's review + the approve gate are the real controls.

1. Same public-repo prep as above. Multi-plugin repos need `.cursor-plugin/marketplace.json`.
2. Open https://cursor.com/marketplace/publish (signed-in as the owner).
3. Fill organization name/handle, contact email, logotype URL, description, public GitHub repo, website URL.
4. **Approve gate** (widget): submit this official plugin application to the Cursor Marketplace now? → Submit Application / Hold off.
5. Only on Submit Application: click **Submit Application**, then report success or the error text.

After submit: review is manual; listing is not instant.

---

## Do not

- Cross-examine whether they "really" work there — ask once, believe them
- Click Submit / Submit Application without the widget approve
- Publish to a team marketplace unless the owner explicitly asks
