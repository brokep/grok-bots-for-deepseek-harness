---
name: collect-local
description: "use this to pack the allowed files on the user's computer (macOS, Linux, or Windows) and copy the archive here, with fallbacks"
---

# collect-local

Part of the Import Bot agent preset.

# Collect local

Gets the allowed files from the user's computer onto this one. macOS, Linux, or Windows. Two or three cards. Nothing in the old tools changes. Redaction happens here, after the copy.

## What is packed

For you: instructions, memory notes, project registries, scheduled tasks, session records, transcripts from the last 90 days, session databases (Hermes, OpenClaw), plugin skills, and connector names. Not packed: files the user attached, files the tools produced, audit keys, and the config files that can hold credentials (those are reduced to connector names on their computer first, with stock tools).

For the user, one line before the read: "I am copying your instructions, memories, projects, scheduled tasks, and recent conversations. I skip your attached files, anything the tools produced, and anything that looks like a password or key." Nothing more technical than that.

## Already collected?

If `/workspace/migration/raw/` exists from a run less than 24 hours old and this is not a resync, skip the pack and copy and go to parse-import. Say nothing about it.

## Which computer

Your context lists the user's operating system. macOS and Linux run a bash command directly. Windows runs a PowerShell script that you first place in the user's temp folder. All of it runs on the user's machine: pass the machineId from ListMachines, as import-bot-setup describes.

## macOS (one Shell call with the machineId)

```bash
A="$HOME/Library/Application Support/Claude"; T="${GB_OUT:-${TMPDIR:-/tmp}}/grokbot-import"; mkdir -p "$T"; OUT="$T/grokbot-import.tgz"; N="$T/connector-names.txt"; E="$T/collect-errors.txt"; : > "$N"; : > "$E"
for f in "$A/claude_desktop_config.json" "$HOME/.claude.json"; do [ -f "$f" ] && { echo "## $f"; osascript -l JavaScript -e 'ObjC.import("Foundation");var o=JSON.parse(ObjC.unwrap($.NSString.stringWithContentsOfFileEncodingError("'"$f"'",4,null))||"{}");var k=Object.keys(o.mcpServers||{});for(var p in (o.projects||{})){k=k.concat(Object.keys(o.projects[p].mcpServers||{}).map(function(x){return x+" (project "+p+")"}))};k.join("\n")' 2>>"$E"; } >> "$N"; done
[ -f "$HOME/.openclaw/openclaw.json" ] && { echo "## $HOME/.openclaw/openclaw.json"; osascript -l JavaScript -e 'ObjC.import("Foundation");var o=JSON.parse(ObjC.unwrap($.NSString.stringWithContentsOfFileEncodingError("'"$HOME/.openclaw/openclaw.json"'",4,null))||"{}");var k=[];["channels","connectors","plugins","mcpServers","tools"].forEach(function(s){var v=o[s];if(v&&typeof v==="object"){k=k.concat(Array.isArray(v)?v.map(function(x){return x&&(x.name||x.id)||String(x)}):Object.keys(v))}});k.join("\n")' 2>>"$E"; } >> "$N"
[ -f "$HOME/.codex/config.toml" ] && { echo "## $HOME/.codex/config.toml"; grep -oE '^[[:space:]]*\[mcp_servers\.[^].]+' "$HOME/.codex/config.toml" | sed 's/.*\[mcp_servers\.//'; } >> "$N"
[ -f "$HOME/.claude/settings.json" ] && { echo "## $HOME/.claude/settings.json"; grep -oE '"[a-zA-Z]*[cC]leanupPeriodDays"[^,}]*' "$HOME/.claude/settings.json"; } >> "$N"
[ -f "$HOME/.hermes/config.yaml" ] && { echo "## $HOME/.hermes/config.yaml"; grep -viE 'key|token|secret|password' "$HOME/.hermes/config.yaml" | grep -E '^[a-zA-Z_]+:|^\s+-\s' | head -60; } >> "$N"
for d in "$HOME/.cursor" "$HOME/.gemini" "$HOME/.local/share/opencode"; do [ -d "$d" ] && echo "## also-present $d" >> "$N"; done
( printf '%s\0' "$N"
  for r in "$A/local-agent-mode-sessions" "$A/claude-code-sessions"; do [ -d "$r" ] && find "$r" -type f \( -name '*.md' -o -name '*.json' -o -name 'audit.jsonl' \) -not -path '*/uploads/*' -not -path '*/outputs/*' -not -path '*/skills-plugin/*' -not -path '*/rpm/*' -not -path '*/debug/*' -not -path '*/backups/*' -not -name '*.audit-key' -not -name 'host-creds-*' -not -name '.claude.json' -not -path '*/ccd-session-secrets/*' -size -5M -print0 2>>"$E"; done
  [ "${GB_TRANSCRIPTS:-1}" = 1 ] && for r in "$A/local-agent-mode-sessions" "$A/claude-code-sessions"; do [ -d "$r" ] && find "$r" -type f -name '*.jsonl' -not -name 'audit.jsonl' -not -path '*/uploads/*' -not -path '*/outputs/*' -not -path '*/skills-plugin/*' -not -path '*/subagents/*' -mtime -90 -size -5M -print0 2>>"$E"; done
  [ -d "$A/cowork_plugins" ] && find "$A/cowork_plugins" -type f \( -name '*.md' -o -name '*.json' -o -name '*.yaml' \) -size -5M -print0 2>>"$E"
  for f in "$HOME/.claude/CLAUDE.md" "$HOME/.codex/AGENTS.md" "$HOME/.codex/AGENTS.override.md" "$HOME/.hermes/memories/MEMORY.md" "$HOME/.hermes/memories/USER.md"; do [ -f "$f" ] && printf '%s\0' "$f"; done
  for d in "$HOME/.claude/skills" "$HOME/.claude/rules" "$HOME/.claude/commands" "$HOME/.claude/agents" "$HOME/.codex/memories" "$HOME/.codex/skills" "$HOME/.agents/skills" "$HOME/.hermes/skills" "$HOME/.openclaw/skills" "$HOME/.openclaw/workspace" "$HOME/Claude/Scheduled" "$HOME/Documents/Claude/Scheduled"; do [ -d "$d" ] && find "$d" -type f \( -name '*.md' -o -name '*.json' -o -name '*.yaml' \) -not -path '*/.git/*' -not -path '*/credentials/*' -size -5M -print0 2>>"$E"; done
  [ -d "$HOME/.claude/projects" ] && find "$HOME/.claude/projects" -type f -path '*/memory/*' -name '*.md' -size -5M -print0 2>>"$E"
  [ "${GB_TRANSCRIPTS:-1}" = 1 ] && for d in "$HOME/.claude/projects" "$HOME/.codex/sessions" "$HOME/.openclaw/agents"; do [ -d "$d" ] && find "$d" -type f -name '*.jsonl' -not -path '*/subagents/*' -mtime -90 -size -5M -print0 2>>"$E"; done
  [ "${GB_TRANSCRIPTS:-1}" = 1 ] && for f in "$HOME/.hermes/state.db" $(find "$HOME/.openclaw/agents" -type f -name '*.sqlite' 2>/dev/null); do [ -f "$f" ] && [ "$(stat -f%z "$f")" -lt 104857600 ] && printf '%s\0' "$f"; done
  printf '%s\0' "$E"
) | COPYFILE_DISABLE=1 tar --null -T - -czf "$OUT" 2>>"$E"; echo "archive: $OUT"; ls -lh "$OUT" | awk '{print "size: " $5}'; echo "files: $(tar -tzf "$OUT" | grep -v '/$' | wc -l | tr -d ' ')"; echo "errors: $(grep -v "Removing leading" "$E" | grep -c .)"
```

## Linux (one Shell call with the machineId)

```bash
A="${XDG_CONFIG_HOME:-$HOME/.config}/Claude"; T="${GB_OUT:-${TMPDIR:-/tmp}}/grokbot-import"; mkdir -p "$T"; OUT="$T/grokbot-import.tgz"; N="$T/connector-names.txt"; E="$T/collect-errors.txt"; : > "$N"; : > "$E"
jkeys() { if command -v python3 >/dev/null 2>&1; then python3 -c 'import json,sys;o=json.load(open(sys.argv[1]));k=list((o.get("mcpServers") or {}).keys());[k.extend(x+" (project "+p+")" for x in (v.get("mcpServers") or {})) for p,v in (o.get("projects") or {}).items()];print("\n".join(k))' "$1" 2>>"$E"; elif command -v jq >/dev/null 2>&1; then jq -r '(.mcpServers // {} | keys[]), ((.projects // {}) | to_entries[] | .key as $p | (.value.mcpServers // {} | keys[]) | . + " (project " + $p + ")")' "$1" 2>>"$E"; else grep -oE '"[A-Za-z0-9_.-]+"[[:space:]]*:[[:space:]]*\{' "$1" | sed -E 's/"([^"]+)".*/\1/' | grep -vE '^(mcpServers|projects|env|args|headers)$'; fi; }
for f in "$A/claude_desktop_config.json" "$HOME/.claude.json"; do [ -f "$f" ] && { echo "## $f"; jkeys "$f"; } >> "$N"; done
[ -f "$HOME/.openclaw/openclaw.json" ] && { echo "## $HOME/.openclaw/openclaw.json"; if command -v python3 >/dev/null 2>&1; then python3 -c 'import json,sys;o=json.load(open(sys.argv[1]));k=[]
for s in ("channels","connectors","plugins","mcpServers","tools"):
    v=o.get(s)
    if isinstance(v,dict): k+=list(v.keys())
    elif isinstance(v,list): k+=[(x.get("name") or x.get("id") or str(x)) if isinstance(x,dict) else str(x) for x in v]
print("\n".join(k))' "$HOME/.openclaw/openclaw.json" 2>>"$E"; else grep -oE '"(channels|connectors|plugins)"' "$HOME/.openclaw/openclaw.json" | head -3; fi; } >> "$N"
[ -f "$HOME/.codex/config.toml" ] && { echo "## $HOME/.codex/config.toml"; grep -oE '^[[:space:]]*\[mcp_servers\.[^].]+' "$HOME/.codex/config.toml" | sed 's/.*\[mcp_servers\.//'; } >> "$N"
[ -f "$HOME/.claude/settings.json" ] && { echo "## $HOME/.claude/settings.json"; grep -oE '"[a-zA-Z]*[cC]leanupPeriodDays"[^,}]*' "$HOME/.claude/settings.json"; } >> "$N"
[ -f "$HOME/.hermes/config.yaml" ] && { echo "## $HOME/.hermes/config.yaml"; grep -viE 'key|token|secret|password' "$HOME/.hermes/config.yaml" | grep -E '^[a-zA-Z_]+:|^\s+-\s' | head -60; } >> "$N"
for d in "$HOME/.cursor" "$HOME/.gemini" "$HOME/.local/share/opencode"; do [ -d "$d" ] && echo "## also-present $d" >> "$N"; done
( printf '%s\0' "$N"
  for r in "$A/local-agent-mode-sessions" "$A/claude-code-sessions"; do [ -d "$r" ] && find "$r" -type f \( -name '*.md' -o -name '*.json' -o -name 'audit.jsonl' \) -not -path '*/uploads/*' -not -path '*/outputs/*' -not -path '*/skills-plugin/*' -not -path '*/rpm/*' -not -path '*/debug/*' -not -path '*/backups/*' -not -name '*.audit-key' -not -name 'host-creds-*' -not -name '.claude.json' -not -path '*/ccd-session-secrets/*' -size -5M -print0 2>>"$E"; done
  [ "${GB_TRANSCRIPTS:-1}" = 1 ] && for r in "$A/local-agent-mode-sessions" "$A/claude-code-sessions"; do [ -d "$r" ] && find "$r" -type f -name '*.jsonl' -not -name 'audit.jsonl' -not -path '*/uploads/*' -not -path '*/outputs/*' -not -path '*/skills-plugin/*' -not -path '*/subagents/*' -mtime -90 -size -5M -print0 2>>"$E"; done
  [ -d "$A/cowork_plugins" ] && find "$A/cowork_plugins" -type f \( -name '*.md' -o -name '*.json' -o -name '*.yaml' \) -size -5M -print0 2>>"$E"
  for f in "$HOME/.claude/CLAUDE.md" "$HOME/.codex/AGENTS.md" "$HOME/.codex/AGENTS.override.md" "$HOME/.hermes/memories/MEMORY.md" "$HOME/.hermes/memories/USER.md"; do [ -f "$f" ] && printf '%s\0' "$f"; done
  for d in "$HOME/.claude/skills" "$HOME/.claude/rules" "$HOME/.claude/commands" "$HOME/.claude/agents" "$HOME/.codex/memories" "$HOME/.codex/skills" "$HOME/.agents/skills" "$HOME/.hermes/skills" "$HOME/.openclaw/skills" "$HOME/.openclaw/workspace" "$HOME/Claude/Scheduled" "$HOME/Documents/Claude/Scheduled"; do [ -d "$d" ] && find "$d" -type f \( -name '*.md' -o -name '*.json' -o -name '*.yaml' \) -not -path '*/.git/*' -not -path '*/credentials/*' -size -5M -print0 2>>"$E"; done
  [ -d "$HOME/.claude/projects" ] && find "$HOME/.claude/projects" -type f -path '*/memory/*' -name '*.md' -size -5M -print0 2>>"$E"
  [ "${GB_TRANSCRIPTS:-1}" = 1 ] && for d in "$HOME/.claude/projects" "$HOME/.codex/sessions" "$HOME/.openclaw/agents"; do [ -d "$d" ] && find "$d" -type f -name '*.jsonl' -not -path '*/subagents/*' -mtime -90 -size -5M -print0 2>>"$E"; done
  [ "${GB_TRANSCRIPTS:-1}" = 1 ] && for f in "$HOME/.hermes/state.db" $(find "$HOME/.openclaw/agents" -type f -name '*.sqlite' 2>/dev/null); do [ -f "$f" ] && [ "$(stat -c%s "$f")" -lt 104857600 ] && printf '%s\0' "$f"; done
  printf '%s\0' "$E"
) | tar --null -T - -czf "$OUT" 2>>"$E"; echo "archive: $OUT"; ls -lh "$OUT" | awk '{print "size: " $5}'; echo "files: $(tar -tzf "$OUT" | grep -v '/$' | wc -l | tr -d ' ')"; echo "errors: $(grep -v "Removing leading" "$E" | grep -c .)"
```

## Windows (three steps)

1. Copy `collect-windows.ps1` out of the import-scripts skill to `/workspace/migration/tools/collect-windows.ps1` on this computer with the command in import-bot-setup ("Copying a script out of a skill").
2. CopyFromBox it to the user's temp folder, with the machineId: destination `%TEMP%\collect-windows.ps1` (ask the shell for `$env:TEMP` first if you need the absolute path). Skip this when `Test-Path "$env:TEMP\collect-windows.ps1"` is already true from an earlier run today.
3. Shell with the machineId: `powershell -NoProfile -ExecutionPolicy Bypass -File "%TEMP%\collect-windows.ps1"` (in PowerShell use `$env:TEMP`). To skip transcripts: `$env:GB_TRANSCRIPTS="0"; powershell -NoProfile -ExecutionPolicy Bypass -File "$env:TEMP\collect-windows.ps1"`.

## Reading the output

Every collector prints `archive:`, `size:`, `files:`, `errors:`. If the call returns while tar is still running, use AwaitShell with the same machineId until `files:` prints. Never copy a partial archive.

- `files:` 1 or 0: nothing local. Move on to accounts or the interview.
- `size:` over 200M: re-run with transcripts off (`GB_TRANSCRIPTS=0 ` prefix on bash, `$env:GB_TRANSCRIPTS="0"` on Windows). Transcripts and databases are skipped, everything else stays.
- `errors:` above 0: read `collect-errors.txt` inside the archive after the copy. A permission denied on the Documents folder means the OS blocked it. Note it in the coverage table as "Documents folder was locked by your computer" and move on.

## Card: copy

CopyToBox, with the machineId, from the absolute path on the `archive:` line to `/workspace/migration/import.tgz`.

## Fallbacks

**Local access declined or unavailable.** Run the fallback-collect-script skill: the user runs the same collector themselves, sent as a file, and that skill covers getting the archive onto this computer. The parser removes attachments, outputs, keys, and credential configs on arrival.

**Nothing found anywhere.** Say so once, then the account pulls carry the import, and the interview-fallback skill fills whatever is left.
