---
name: import-receipt
description: "use this at the end: confirmed counts, who owns what now, routines to start with, connectors to connect, then clean up"
---

# import-receipt

Part of the Import Bot agent preset.

# Import receipt

The last step. One page that says what moved, who owns what now, and what to do next. Counts are confirmed, not planned: check each expert's folder per expert-packet Part 3 and write "planned N, confirmed M" where they differ.

## `/workspace/migration/receipt.md`

```
# Import receipt, <date>

Sources: <Cowork n sessions from your computer, ChatGPT n conversations (live chatgpt <date>), Claude n conversations (export <date>), Codex, OpenClaw, Hermes, Claude Code, as found>
Shared memory: <n> profile facts, <n> log facts. Every bot reads them on its next new conversation.
Every original note kept word for word, in case you ever want them.

## Your bots
| Bot | Existing or new | Takes care of | Knows how to | Scheduled jobs (paused) | Connect for it | Past conversations it knows |
|---|---|---|---|---|---|---|

Existing bots that accepted a transfer show "existing, approved" and one line on what they were asked to consider. Declined proposals are not listed as owners. Existing bots left alone are listed once under the table: "Untouched: <names>."

## Waiting for your call
| Would go to | What | Say |
|---|---|---|
<one row per parked proposal: the existing bot, the units, "send to <bot>" or "make a new expert">

## How your projects and workflows landed
| From | Now |
|---|---|
| Cowork project "<project>" | <expert> now owns that project and its notes |
| Cowork scheduled task "<task>" | <expert> runs it as "<what it produces>", paused |
| ChatGPT project "<project>" | <expert> now owns it |
| Custom GPT "<GPT name>" | <expert> writes in that GPT's voice on request |
| Named workflow "<user's words>" | <bot> handles it, <as a job you ask for or a scheduled job> |

## Routines to turn on first
<the three from the roster, one line each, then "say turn on <name> or pick in each bot's first chat">

## Connect these
<the "connect these first" and "connect these too" lists from connectors.md, one clause each. Connectors with no plugin show "no plugin yet, <vendor> offers a direct connection, the expert sets it up on your yes">

## Your project files
| Folder | Project | Now |
|---|---|---|
<copied to my computer (n files) | on your computer, read on request | connect <drive> | missing, recreate?>

## Could not read
<one line each, plain: "Your Documents folder was locked by your computer, so scheduled task files were skipped" or "Claude's export is not available on your plan, so I used the signed-in pull" or omit the section when nothing failed>

## Also done
- <"I also made sure Claude stops deleting your older conversations, so nothing disappears while you switch." | "Claude's auto-delete stays as you set it." | "Claude's auto-delete setting could not be changed automatically. Ask me if you want the steps." | omit the line when not applicable>
- Waiting on: <ChatGPT export email, Claude export, a sign-in that did not finish>. Paste the link here when it lands.

## Next
1. Open <the expert with the most owned units> and say hi.
2. Turn on the routines you want.
3. Connect the tools each bot asks for.
4. Come back here after you use the old tools again. I only add what is new.
5. Rename, move a project, merge, or split any expert by telling me.
```

## Then

- Paste the receipt into chat in full.
- Delete `/workspace/migration/raw` and any archive under `/workspace/migration` or `/workspace/uploads`. Strip transcript samples from the inventory:

```bash
python3 - <<'EOF'
import json; p='/workspace/migration/inventory.json'; d=json.load(open(p))
for a in d.get('cowork',{}).get('accounts',[]):
    for s in a.get('sessions',[]): s.pop('sample_user_turns',None)
for k in ('codex',): d.get(k,{}).pop('sample_user_turns',None)
for pr in d.get('claude_code',{}).get('projects',[]): pr.pop('sample_user_turns',None)
for ag in d.get('openclaw',{}).get('agents',[]): ag.pop('sample_user_turns',None)
for acc in d.get('accounts',{}).values():
    for c in acc.get('conversations',[]): c.pop('sample_user_turns',None)
json.dump(d,open(p,'w'),indent=2)
EOF
```

- Keep `/workspace/migration/pack`, `home`, `inventory.json`, `sources.md`, `receipt.md`, `state.md`. The experts read their packets from `pack`.
- Write the one Import state fact on this bot (scope agent, tier log), under 200 characters. First forget the previous Import state fact, if there is one, with its exact text, which is the first line of `state.md`. Shape: "Import state <date>: done. <n> experts, <n> routines paused, <n> shared facts. Accounts: <services>, read only. Retention fix <applied, declined, failed, or not needed>. Waiting on: <list or none>." Then make that exact text the first line of `state.md`, with the full summary below it.
