---
name: prove-plugin-local
description: "Use when proving a Cursor/Agent Plugin loads locally — schema validate, install under ~/.cursor/plugins/local, and record what loaded."
---

# prove-plugin-local

Part of the tinkabot agent preset.

---
name: prove-plugin-local
description: >-
  Use when proving a Cursor/Agent Plugin loads locally — schema validate,
  install under ~/.cursor/plugins/local, and record what loaded.
---
# Prove a plugin locally

## Preconditions

Plugin directory has either:
- Agent Plugin: root `plugin.json` with agent-plugins `$schema`, or
- Cursor Plugin: `.cursor-plugin/plugin.json`

## Steps

1. **Schema.** Validate Agent `plugin.json` / `mcp.json` against https://agent-plugins.org/schemas/1.0.0/plugin.schema.json and `mcp.schema.json` (jsonschema or equivalent). Cursor manifests only need a kebab-case `name` (no agent `$schema`).
2. **MCP smoke.** If there is a stdio server: `node --check` (or language equivalent), then a live `initialize` + `tools/list` + one real `tools/call` against the public API when safe.
3. **Install path.** Copy into a **real directory** under `~/.cursor/plugins/local/<plugin-name>` (not a symlink whose target is outside that folder; Cursor rejects those).
4. **Loader.** Prefer running `@anysphere/cursor-plugins` `loadUserLocalPlugins({ userHomeDir })` when that package is available. Expect the plugin name, skills, rules, and mcp server ids.
5. **IDE.** Reload Window / Customize confirms components when running inside Cursor. Note org gate: Teams/Enterprise may require "Allow Local Plugin Imports".
6. **Verify note.** Short file or chat note: paths, PASS/FAIL, what loaded vs what this environment cannot prove (Customize UI, org policy).

## Done when

Manifests valid, local install present as a real directory, and either the shared loader reports the plugin or you documented why the loader/IDE step was skipped.
