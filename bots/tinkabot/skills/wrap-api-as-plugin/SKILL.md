---
name: wrap-api-as-plugin
description: "Use when wrapping an HTTP API, OpenAPI/spec, or \"wrap X\" into a Cursor/Agent Plugin (MCP + skills). Prefer before scaffolding files."
---

# wrap-api-as-plugin

Part of the tinkabot agent preset.

---
name: wrap-api-as-plugin
description: >-
  Use when wrapping an HTTP API, OpenAPI/spec, or "wrap X" into a Cursor/Agent
  Plugin (MCP + skills). Prefer before scaffolding files.
---
# Wrap an API as a plugin

## Data shape first

Name the domain type before any files. One line, e.g. `FxQuote = { amount, base, date, rates }` or `PokemonSummary = { id, name, height, weight, types }`.
Organize tools around that shape, not around whatever the upstream JSON dumps.

## Choose format

- **Default: Agent Plugin** at repo root: `plugin.json` (`$schema` https://agent-plugins.org/schemas/1.0.0/plugin.schema.json), optional `mcp.json`, `skills/<name>/SKILL.md`.
- **Cursor Plugin** (`.cursor-plugin/plugin.json`) only when you need rules, hooks, agents, or commands.

Docs: https://cursor.com/docs/plugins and https://cursor.com/docs/reference/plugins

## Scaffold (smallest)

1. `plugin.json` with `name`, `description`, `version`, `author`.
2. If MCP: `mcp.json` with matching Agent Plugins `$schema`, stdio server, `cwd: "${PLUGIN_ROOT}"`, `command`/`args` to the server entry.
3. One thin skill whose description says **when** to call the tools. Never invent API data in the skill.
4. Public no-auth HTTP: zero-dep stdio MCP (hand-rolled JSON-RPC + `fetch`) until an SDK earns its install.
5. Auth APIs: declare plugin `variables` for secrets; put only `${VAR}` placeholders in `mcp.json`. Never commit keys.

## Repo work

Non-trivial repo edits go to a CloudAgent. Do not clone product monorepos onto the agent machine for scaffolding.

## Prove + publish

Run prove-plugin-local. When the owner wants it listed, run publish-cursor-plugin: ask once if they work at the company/service — yes (or they insist) → Marketplace, no/unsure → cursor.directory. Trust the answer; the approve gate still blocks submit.

## Do not

- Submit anywhere without an explicit owner ask + approve gate
- Paste secrets into chat
- Build host-product Slack bot accounts
