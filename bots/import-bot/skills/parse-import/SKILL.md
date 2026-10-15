---
name: parse-import
description: "use this to turn the archive and account pulls into inventory.json and sources.md with secrets scrubbed"
---

# parse-import

Part of the Import Bot agent preset.

# Parse import

Turns the archive and the account pulls into `inventory.json` and `sources.md`, and every conversation into the one shape transcript-toolkit searches. Secrets are scrubbed before anything is read into the conversation.

## Steps

1. Copy `import-tools.py` out of the import-scripts skill to `/workspace/migration/tools/import-tools.py` with the command in import-bot-setup ("Copying a script out of a skill").
2. Run `python3 /workspace/migration/tools/import-tools.py parse /workspace/migration/import.tgz /workspace/migration` (or the archive under `/workspace/uploads/`). Account pulls already under `/workspace/migration/raw/accounts/` are picked up in the same run, and it normalizes every conversation at the end. Re-run any time more arrives (an export zip, a late sign-in). It is idempotent.
3. Read `sources.md`. Paste the table as the coverage table, one line above it: what was found, what was not. Leave out the technical footer lines. If anything was skipped, say it in plain words ("anything that looked like a password or key was removed before I read it").
4. Read `inventory.json`. Do not paste it. Use it.
5. Delete the archive: `rm -f /workspace/migration/import.tgz /workspace/uploads/*.zip /workspace/uploads/*.tgz`.
6. Run the cleanup-fix skill if Cowork or Claude Code was found.

## Reading the inventory

- `cowork.accounts[]`: `global_instructions` (their CLAUDE.md), `global_memory_notes[]`, `spaces[]` (projects with instructions, folders, memory notes, per-project `connectors_seen` and `session_count`), `scheduled_tasks[]` (schedule, timezone, prompt, `space_id`, `enabled` as Cowork stored it), `sessions[]` (title, dates, `space_id`, `connectors_seen`, sample user turns, `agent_type`), `oldest_session` vs `oldest_transcript` for the 30-day check, `connectors_seen_outside_projects`.
- `cowork.plugins[]`: installed plugins and their skill files.
- `claude_code`: CLAUDE.md, skills, rules, commands, agents, per-repo memory, MCP names, retention settings.
- `codex`: AGENTS.md, memories (if on), skills, MCP names, session count, sample turns.
- `openclaw`: `bootstrap` (SOUL, IDENTITY, USER, AGENTS, MEMORY), `memory_notes`, `skills`, `channels`, `agents[]` with session counts and sample turns.
- `hermes`: MEMORY.md, USER.md, skills, config lines, `sessions[]` (title, date, model, cwd).
- `accounts.chatgpt`: `memories`, `custom_instructions`, `projects`, `gpts`, `conversations[]` (title, dates, turns, sample turns, source export or live).
- `accounts.claude`: `memory_text`, `export_memory` (conversations_memory and per-project memories), `projects[]` (name, description, prompt_template, docs), `conversations[]`.

Every source has `found`. Say plainly what was absent. Never invent a project, memory, or workflow.

## Unknown shapes

Unknown keys are kept under `raw`. When a scheduled task has no `schedule` or a project has no `name`, look in `raw`, then in the session titles, then ask the user in one line. Note any schema surprise at the bottom of `sources.md` under "Schema notes".
