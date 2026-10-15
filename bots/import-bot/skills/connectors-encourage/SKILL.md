---
name: connectors-encourage
description: "use this to map every connector the user relied on to a Grok Bot plugin, assign it to the expert that needs it, and make the case to connect"
---

# connectors-encourage

Part of the Import Bot agent preset.

# Connectors encourage

Every connector the user relied on elsewhere should be connected here, on the expert that needs it. This skill builds the list and makes the case, one clause each.

## Inputs

- Names on the Mac: `cowork.mcp_servers`, `claude_code.mcp_servers`, `codex.mcp_servers`, `openclaw.channels`, Hermes config lines.
- Usage: `cowork.accounts[].connectors_seen`, per project `spaces[].connectors_seen` with counts, `connectors_seen_outside_projects`.
- Account side: ChatGPT connectors mentioned in memories or projects, Claude project docs.
- Cowork plugins are skill bundles, already ported. Not connectors.

## What is already connected

Ask this computer first (`GetMcpServerStatus`) and note every plugin or server already connected for this user. Those are marked "connected" in `connectors.md` and in every expert packet. The expert says "Gmail is ready" and never offers it again. Only what is missing is offered.

## Map by common name

| Seen | Grok Bot |
|---|---|
| gmail, google-mail | Gmail |
| google-calendar, gcal | Google Calendar |
| google-drive, gdrive | Google Drive |
| google-sheets, sheets | Google Sheets |
| google-docs, docs | Google Drive (documents live there, there is no separate Docs plugin) |
| onedrive, sharepoint | OneDrive, when SearchPlugins finds it |
| slack | Slack |
| notion | Notion |
| github | GitHub |
| linear | Linear |
| salesforce, sfdc | Salesforce |
| gong | Gong |
| figma | Figma |
| granola | Granola |
| hex | Hex |
| databricks | Databricks SQL |
| x, twitter | X |
| telegram, whatsapp, discord, imessage (OpenClaw channels) | Slack for the same job, offered as the replacement |

Never quote a plugin id.

## Output, `/workspace/migration/pack/connectors.md`

| Connector | Used where | Times seen | Expert that needs it | Why, in one clause | Path |
|---|---|---|---|---|---|

"Path" is plugin, MCP (with the URL found), or paste.

Then two short lists:

- **Connect these first.** The connectors with the most usage, one clause each on what the expert does with it. "Salesforce, so <the pipeline expert> can pull the stale-deal list itself instead of you exporting a CSV."
- **Connect these too.** Tools the user clearly uses (named in memory, in project instructions, in their setup answers) that Grok Bot offers and no old tool had wired up. "You mention Notion in four project instructions. Connect it to <the expert> and it can read those pages directly."

Each expert installs its own when the user says yes in its first conversation (SearchPlugins then InstallPlugin, or AddMcpServer for the MCP path). Import Bot installs nothing for itself except Gmail, Google Drive, or OneDrive when the user wants it to fetch an export link or their fallback zip. Paste and upload always work in the meantime, and the receipt says so once.
