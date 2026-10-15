---
name: cleanup-fix
description: "use this after parsing when Cowork or Claude Code was found: stop the 30-day transcript cleanup, automatically on defaults, asking when the user set a value"
---

# cleanup-fix

Part of the Import Bot agent preset.

# Cleanup fix

Claude Code and Claude Desktop delete session transcripts whose file age passes `cleanupPeriodDays` (default 30) and `desktopSessionCleanupPeriodDays`. Silent, keyed on file modification time, unrecoverable. Memory notes and projects survive it, transcripts do not. Anthropic documents both keys in `~/.claude/settings.json` (`%USERPROFILE%\.claude\settings.json` on Windows).

## Decide

First, skip entirely if `state.md` or the Import state fact says the fix was applied or declined, or if the inventory shows both values already at 3650 or higher. Nothing to do and nothing to say.

Otherwise read the retention values the inventory printed (`claude settings:` line, or `claude_code.settings` after parsing). The user hears none of the mechanics below. No file names, keys, numbers, or backups in chat.

- Nothing set, meaning defaults: apply it silently. The only mention is one line in the receipt: "I also made sure Claude stops deleting your older conversations, so nothing disappears while you switch."
- A value the user set themselves: ask once, in plain words. "Claude is set to delete your conversations after <n> days. Want me to turn that off so nothing disappears while you switch? You can undo it any time." Yes runs it. No moves on and it is never raised again.
- Cowork and Claude Code both absent: skip.

## Rules

Every command below runs on the user's machine, Shell with the machineId. Never 0 (zero deletes everything). Use 3650. Back up first, in the same command. If the file is not valid JSON, stop and leave it alone. Show the resulting file.

## macOS (one card)

```bash
f="$HOME/.claude/settings.json"; mkdir -p "$HOME/.claude"; [ -f "$f" ] && cp "$f" "$f.bak-$(date +%Y%m%d-%H%M)"; osascript -l JavaScript -e 'ObjC.import("Foundation");var p="'"$f"'";var raw=ObjC.unwrap($.NSString.stringWithContentsOfFileEncodingError(p,4,null));var o={};if(raw&&raw.trim()){o=JSON.parse(raw)};o.cleanupPeriodDays=3650;o.desktopSessionCleanupPeriodDays=3650;$.NSString.alloc.initWithUTF8String(JSON.stringify(o,null,2)+"\n").writeToFileAtomicallyEncodingError(p,true,4,null);"written"' && cat "$f" && (ls "$HOME/.claude/" | grep bak || echo "no previous file, nothing to back up")
```

## Linux (one card, uses python3, then jq, then node, whichever exists)

```bash
f="$HOME/.claude/settings.json"; mkdir -p "$HOME/.claude"; [ -f "$f" ] && cp "$f" "$f.bak-$(date +%Y%m%d-%H%M)"
if command -v python3 >/dev/null 2>&1; then python3 - "$f" <<'PY'
import json, os, sys
p = sys.argv[1]; raw = open(p).read() if os.path.exists(p) else ""
o = json.loads(raw) if raw.strip() else {}
o["cleanupPeriodDays"] = 3650; o["desktopSessionCleanupPeriodDays"] = 3650
open(p, "w").write(json.dumps(o, indent=2) + "\n"); print("written")
PY
elif command -v jq >/dev/null 2>&1; then if [ -s "$f" ]; then jq '.cleanupPeriodDays=3650 | .desktopSessionCleanupPeriodDays=3650' "$f" > "$f.new" || { rm -f "$f.new"; echo "settings.json is not valid JSON, left alone"; false; }; else printf '{"cleanupPeriodDays": 3650, "desktopSessionCleanupPeriodDays": 3650}\n' > "$f.new"; fi && mv "$f.new" "$f" && echo written
elif command -v node >/dev/null 2>&1; then node -e 'const fs=require("fs");const p=process.argv[1];const raw=fs.existsSync(p)?fs.readFileSync(p,"utf8"):"";const o=raw.trim()?JSON.parse(raw):{};o.cleanupPeriodDays=3650;o.desktopSessionCleanupPeriodDays=3650;fs.writeFileSync(p,JSON.stringify(o,null,2)+"\n");console.log("written")' "$f"
else echo "no JSON tool on this computer"; false; fi && cat "$f"
```

If none of the three tools exist, do the merge here: Shell `cat "$f"` on their machine, edit the JSON on this computer, then CopyFromBox the merged file back (same machineId) to `~/.claude/settings.json` after the backup card. Four cards, so say so first.

## Windows (one card, PowerShell)

```powershell
$f = Join-Path $env:USERPROFILE ".claude\settings.json"; New-Item -ItemType Directory -Force -Path (Split-Path $f) | Out-Null
if (Test-Path $f) { Copy-Item $f ($f + ".bak-" + (Get-Date -Format "yyyyMMdd-HHmm")) }
try {
  $raw = if (Test-Path $f) { Get-Content -Raw $f } else { "" }
  $o = if ($raw.Trim()) { $raw | ConvertFrom-Json } else { New-Object PSObject }
  $o | Add-Member -NotePropertyName cleanupPeriodDays -NotePropertyValue 3650 -Force
  $o | Add-Member -NotePropertyName desktopSessionCleanupPeriodDays -NotePropertyValue 3650 -Force
  [System.IO.File]::WriteAllText($f, ($o | ConvertTo-Json -Depth 20) + "`n"); "written"; Get-Content $f
} catch { "settings.json is not valid JSON, left alone: " + $_.Exception.Message }
```

## After

If the command stops because the file is not valid, leave it alone and say nothing in chat. Put one plain line in the receipt: "Claude's auto-delete setting could not be changed automatically. Ask me if you want the steps." Do not hand-edit the file. Add one line to `state.md`: "Retention fix <applied, declined, or failed> <date>." The Import state fact picks it up at the end.
