---
name: import-bot-setup
description: "use this on the first turn: hello, which tools, which workflows to make sure of, then run the whole import in order"
---

# import-bot-setup

Part of the Import Bot agent preset.

# Import Bot setup

Runs on the first turn, right after the user pressed Import. Two questions, then the whole import runs without stopping for permission at each step. The button press was the yes. The platform still shows its own permission cards for the user's computer and a sign-in hand-off for accounts, and you tell the user those are coming so nothing surprises them.

## 0. Check what already exists (silently, before the hello)

One Shell call on this computer, with no machineId: `ls /workspace/migration/receipt.md /workspace/migration/state.md /workspace/migration/inventory.json /workspace/migration/pack/spawn-plan.md /workspace/migration/tools/ 2>/dev/null`.

- `receipt.md` exists: this is a return visit. Skip the two questions. "Welcome back. I can bring over what changed since <date>, show your receipt, or adjust an expert. Which?" Then resync or adjust-experts.
- `inventory.json` exists but no receipt: a run stopped partway. Say "Picking up where we left off." Read `state.md` for the answers and accounts already saved. Skip the steps whose outputs exist (archive collected, parsed, memory written, experts in `spawn-plan.md`) and continue from the first missing one. Never re-collect, re-parse, or re-create what is already there.
- `tools/` exists: fine. The scripts are copied out of the skills again on every run, one command each (see "Copying a script out of a skill").
- Nothing exists: first run, continue below.

## 1. Hello and question one

"I bring your AI setup into Grok Bot and set up the expert bots that cover it, or add to the bots you already have. About ten minutes, nothing in your old tools changes, and everything stays in your Grok Bot."

Then, as a multiselect: "Which of these do you use?"
- Codex
- Claude Cowork
- ChatGPT
- OpenClaw
- Hermes
- Something else (tell me what)

Whatever they pick, also import anything found on their computer that they did not name (Claude Code, Cursor, Gemini CLI, OpenCode). Say so in the coverage table later, never as a question now.

## 2. Question two (skippable)

"Any workflows you want to make sure come over, even ones that might be hard to see in your history? One line each is plenty. Skip if nothing comes to mind."

Write them to `/workspace/migration/state.md` under "Named workflows", in their words. They become work units with the highest priority in plan-experts, and each one must appear in the receipt by name.

## 3. Inventory, then show the plan, then go

"Grok Bot will ask you to approve a few reads of your computer. If you picked ChatGPT or Cowork, I will also hand you my browser to sign in to those accounts, because that is where their memories and conversations live. Approve and sign in as they come."

Then, in this order, without waiting between steps unless a step needs the user:

1. Inventory on the user's computer (below). This is also the local access check.
2. Existing bots. Read the user's current bots on this computer: every sibling folder under the agents root has a `profile.json` with `name` and `description` (the agents root is named in your own context, `~/agent-data/agents` on a standard box). Skip yourself and any folder with no profile. Read each bot's skills and routines folders too when they are readable, so you know what it already does. Write the list to `/workspace/migration/existing-bots.md` (name, one-line job, skills, routines) for plan-experts, and rebuild it on every run. It is working state for this import, never memory: never save another bot's name, job, or contents as a memory fact.
3. **Show the plan before doing it.** One short message from the inventory, the existing bots, and the named workflows, in plain words, in this shape:

   "Here is what I will do. Read your Cowork (14 sessions, 2 projects, 2 scheduled tasks) and Codex from your computer, and sign you in to ChatGPT for its memories and conversations. Bring what they knew about you into shared memory. Then set up your work like this: your writing projects and the <custom GPT> get a new <expert title>. Your pipeline review and deal research fit your existing <bot name>, so I will propose that and ask before sending anything to it. Your two scheduled jobs come over paused so you decide when they run. Starting now. Say stop or change anything as I go."

   Counts and names from the inventory, expertise guesses from titles and the named workflows, existing bots by name. No file names, no tool names. Then continue without waiting. If the user says "show me first", "wait", or "stop" at any point, finish the current step, stop, and show the next step in the same plain words before doing it. Stay in that mode until they say go.
4. cleanup-fix, silently, using what the inventory found. The conversations it protects are being deleted by age, so this comes before the pack.
5. collect-local.
6. collect-accounts, for ChatGPT always, for Cowork and Claude Code as the account side of the dual approach, for Codex when they use Codex Cloud. OpenClaw and Hermes have no account side.
7. parse-import, which also normalizes every conversation for transcript-toolkit.
8. write-user-memory.
9. plan-experts (existing bots first), then project-folders for any project that had a local folder, then bot-design-standard on the plan, then spawn-experts.
10. routines-roster.
11. connectors-encourage.
12. import-receipt. Afterwards, adjust-experts handles renames, moves, and merges the user asks for.

Name each step in one short line as you start it ("Reading your computer.", "Signing you in to ChatGPT.", "Planning your experts."). Never narrate tool calls, file names, commands, settings keys, or counts of anything technical. The user hears outcomes. Every code block in these skills is for you to run, never to show.

## Reaching the user's computer

Every read and copy on the user's computer uses the same tools you use here, pointed at their machine. Call ListMachines once, then pass the returned machineId to Shell, Read, and AwaitShell, and to CopyToBox and CopyFromBox for files. Without a machineId those tools run on this computer, where none of the user's files are, and an inventory here finds nothing. Their messages from the desktop app carry a "[Sent from machine <machineId>]" note, and that machine is the default. If more than one machine is connected, ask once which to import from (multiselect, all allowed) and label each in the coverage table. If none is connected, say in one line that their desktop app needs to be open, then carry on with fallback-collect-script and the accounts. An older app lists ExternalShell and AwaitExternalShell instead, and those do the same job.

## If local access is off

The first call on their machine tells you. A result starting "Local tools are turned off" means the setting is Never allow. Before anything else, ask the user to change it, in this shape:

"One setting first. Grok Bot is not allowed to read your computer right now, so I could only import from your online accounts. Open Settings, then Bot, find Execution on Local Computer, and pick Ask every time. You will approve each read as it happens. Tell me when it is done and I continue."

Wait. When they say done, run the inventory again. If the result still says off, ask once more with the exact label. If they say their team admin set it (the setting shows "Your team's admin allows at most Never allow"), say so plainly, skip to the fallback-collect-script path for what they can gather by hand, and make the account side carry the rest.

A declined card is different from the setting being off. Grok Bot never asks about the same action twice in one task, so do not retry a declined step on your own. Say in one line what it was for and what skipping it costs ("Without that read I skip your Cowork projects. Say go ahead and I will ask again."), move on to the fallback for that step, and ask again only when the user says so.

## Inventory (one Shell call with the machineId, picked by the user's operating system)

Your context lists the operating system and shell of the machine the user is messaging from. Use the matching block. For another machine, or when the context is missing, run `uname -s 2>/dev/null || echo windows` there first.

**macOS and Linux** (bash). Claude Desktop keeps its data under `~/Library/Application Support/Claude` on macOS and `~/.config/Claude` on Linux. The first line picks the right one.

```bash
if [ -d "$HOME/Library/Application Support/Claude" ]; then A="$HOME/Library/Application Support/Claude"; else A="${XDG_CONFIG_HOME:-$HOME/.config}/Claude"; fi
for d in "$A/local-agent-mode-sessions" "$A/claude-code-sessions"; do
  [ -d "$d" ] || continue
  echo "== cowork $(basename "$d")"
  echo "accounts: $(find "$d" -mindepth 2 -maxdepth 2 -type d -not -path '*/skills-plugin/*' | wc -l | tr -d ' ')"
  echo "session records: $(find "$d" -maxdepth 4 -name 'local_*.json' | wc -l | tr -d ' ')"
  echo "transcripts: $(find "$d" -name '*.jsonl' -not -name 'audit.jsonl' -not -path '*/skills-plugin/*' -not -path '*/subagents/*' | wc -l | tr -d ' ')"
  echo "global memory notes: $(find "$d" -maxdepth 4 -path '*/memory/memory/*.md' | wc -l | tr -d ' ')"
  echo "projects: $(find "$d" -maxdepth 3 -name 'spaces.json' | wc -l | tr -d ' ') registry, $(find "$d" -maxdepth 6 -path '*/spaces/*/memory/*.md' | wc -l | tr -d ' ') notes"
  echo "scheduled tasks file: $(find "$d" -maxdepth 3 -name 'scheduled-tasks.json' | wc -l | tr -d ' ')"
done
[ -d "$A/cowork_plugins" ] && echo "cowork plugins: $(ls "$A/cowork_plugins" | wc -l | tr -d ' ')"
[ -f "$HOME/.claude/CLAUDE.md" ] && echo "claude code: CLAUDE.md yes, projects $(ls "$HOME/.claude/projects" 2>/dev/null | wc -l | tr -d ' ')"
[ -f "$HOME/.claude/settings.json" ] && echo "claude settings: $(grep -o '"[a-zA-Z]*[cC]leanupPeriodDays"[^,}]*' "$HOME/.claude/settings.json" | tr '\n' ' ')"
[ -d "$HOME/.codex" ] && echo "codex: yes, memories $( [ -d "$HOME/.codex/memories" ] && echo on || echo off ), sessions $(find "$HOME/.codex/sessions" -name '*.jsonl' 2>/dev/null | wc -l | tr -d ' '), chatgpt login $( grep -q '"auth_mode": *"chatgpt"' "$HOME/.codex/auth.json" 2>/dev/null && echo yes || echo no )"
[ -d "$HOME/.openclaw" ] && echo "openclaw: yes, workspace files $(ls "$HOME/.openclaw/workspace" 2>/dev/null | wc -l | tr -d ' '), agents $(ls "$HOME/.openclaw/agents" 2>/dev/null | wc -l | tr -d ' '), skills $(find "$HOME/.openclaw/skills" -name SKILL.md 2>/dev/null | wc -l | tr -d ' ')"
[ -d "$HOME/.hermes" ] && echo "hermes: yes, state.db $( [ -f "$HOME/.hermes/state.db" ] && echo yes || echo no ), skills $(find "$HOME/.hermes/skills" -name SKILL.md 2>/dev/null | wc -l | tr -d ' ')"
for d in "$HOME/.cursor" "$HOME/.gemini" "$HOME/.local/share/opencode"; do [ -d "$d" ] && echo "also present: $d"; done
echo "os: $(uname -s)"
```

**Windows** (PowerShell. If the shell is cmd, prefix with `powershell -NoProfile -Command` and wrap the block in double quotes, or run it as a file the same way collect-local runs its script).

```powershell
$A = Join-Path $env:APPDATA "Claude"; $H = $env:USERPROFILE
foreach ($d in (Join-Path $A "local-agent-mode-sessions"), (Join-Path $A "claude-code-sessions")) {
  if (-not (Test-Path $d)) { continue }
  "== cowork " + (Split-Path $d -Leaf)
  "session records: " + (Get-ChildItem $d -Recurse -Depth 3 -Filter 'local_*.json' -File -ErrorAction SilentlyContinue).Count
  "transcripts: " + (Get-ChildItem $d -Recurse -Filter '*.jsonl' -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -ne 'audit.jsonl' -and $_.FullName -notmatch 'skills-plugin|subagents' }).Count
  "global memory notes: " + (Get-ChildItem $d -Recurse -Filter '*.md' -File -ErrorAction SilentlyContinue | Where-Object { $_.FullName -match '\\memory\\memory\\' }).Count
  "projects: " + (Get-ChildItem $d -Recurse -Depth 2 -Filter 'spaces.json' -File -ErrorAction SilentlyContinue).Count + " registry"
  "scheduled tasks file: " + (Get-ChildItem $d -Recurse -Depth 2 -Filter 'scheduled-tasks.json' -File -ErrorAction SilentlyContinue).Count
}
if (Test-Path (Join-Path $A "cowork_plugins")) { "cowork plugins: " + (Get-ChildItem (Join-Path $A "cowork_plugins") -Directory).Count }
if (Test-Path (Join-Path $H ".claude\CLAUDE.md")) { "claude code: CLAUDE.md yes" }
if (Test-Path (Join-Path $H ".claude\settings.json")) { "claude settings: " + ((Select-String -Path (Join-Path $H ".claude\settings.json") -Pattern '"[a-zA-Z]*[cC]leanupPeriodDays"[^,}]*' -AllMatches).Matches.Value -join ' ') }
if (Test-Path (Join-Path $H ".codex")) { "codex: yes, memories " + $(if (Test-Path (Join-Path $H ".codex\memories")) { "on" } else { "off" }) + ", sessions " + (Get-ChildItem (Join-Path $H ".codex\sessions") -Recurse -Filter '*.jsonl' -File -ErrorAction SilentlyContinue).Count }
if (Test-Path (Join-Path $H ".openclaw")) { "openclaw: yes, agents " + (Get-ChildItem (Join-Path $H ".openclaw\agents") -Directory -ErrorAction SilentlyContinue).Count }
if (Test-Path (Join-Path $H ".hermes")) { "hermes: yes, state.db " + $(if (Test-Path (Join-Path $H ".hermes\state.db")) { "yes" } else { "no" }) }
foreach ($d in ".cursor", ".gemini") { if (Test-Path (Join-Path $H $d)) { "also present: " + (Join-Path $H $d) } }
"os: windows"
```

If a card goes unanswered, Grok Bot will not ask about that same action again in this task. Say in one line that you are waiting on their approval, and run it again when they reply. If it is declined or no machine is connected, go to collect-local's fallbacks. If two Cowork accounts exist, import both and label them in the coverage table.

## 4. Save setup state

Run state lives in `/workspace/migration/state.md` on this computer, not in memory, so the rules you arrived with stay in your prompt. Write the setup line there: "Setup <date>: os <macOS/Windows/Linux>, machine <label>, tools <list>, named workflows <n>, local access <yes/no>." Accounts and the retention fix result are added as they happen. At the end, import-receipt writes the one Import state fact to memory.

## Copying a script out of a skill

The scripts this bot runs on its own computer live in the import-scripts skill: `import-tools.py` (the parser and transcript toolkit), the Windows collector, and the Windows ChatGPT pull. The fallback also sends the Mac and Linux collectors from collect-local. Never retype one. Your skills are files on this computer, and the agent_skills catalog in your context lists each one's SKILL.md path. Copy a script out with one Shell call on this computer, passing that path, the heading the script sits under, and where it goes. It finds the heading as a line of its own and takes the first code block after it:

```bash
python3 - "<the skill's SKILL.md path>" "<heading>" "<destination>" <<'EOF'
import re, sys
fence = "`" * 3
text = open(sys.argv[1], encoding="utf-8").read()
start = re.search("^" + re.escape(sys.argv[2]) + "$", text, re.M).end()
code = re.search(fence + r"[a-z]*\n(.*?)\n" + fence, text[start:], re.S).group(1)
open(sys.argv[3], "w", encoding="utf-8").write(code + "\n")
print(sys.argv[3], len(code.encode()), "bytes")
EOF
```

If Shell cannot see the skill file (a team bot keeps its skills off this computer), Read the skill and write the script out exactly instead.
