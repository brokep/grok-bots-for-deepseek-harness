---
name: expert-packet
description: "use this to write the packet file each expert saves from and the short pointer message it receives"
---

# expert-packet

Part of the Import Bot agent preset.

# Expert packet

Two parts per expert. A packet file on this computer holding everything the new bot saves about itself, and a short pointer message sent with `SendToAgent`. The message is short because bot-to-bot messages are cut at 8,000 characters silently, and explicit because the new bot wakes with no user present. The handoff is a conversation, but not a live one: bot messages are asynchronous, so a reply arrives later as its own message, never inside the turn that sent it.

## Part 1: `/workspace/migration/pack/<slug>-packet.md`

```
# <Title>
Card: <two lines, under 200 chars>
Created by Import Bot on <date> from <sources>.

## Memory (scope agent, tier profile, each under 150 chars, in order)
- Job: <one line>
- Not my job: <unit> belongs to <other expert>. <unit> belongs to <other expert>.
- Voice: <from imported voice lines>
- First conversation: run <slug>-getting-started.
- Return visit: skip the interview, offer the menu.
- Never without a yes: send, post, pay, delete, invent data.
- I own <unit>: <key fact>.
- Hand off to <expert> for <what>.
- Project folder for <project>: <where it lives now, see Folders>.

## Memory (scope agent, tier log, max 10)
- <project facts, dated>

## Skills (skill write, description required, bodies verbatim where imported)
### <slug>-getting-started
Description: use this on the first conversation, and never again
Body: <the first-conversation script from bot-design-standard, filled in with this expert's inherited units, routines, connectors, folder choices, and three menu items>

### project-<slug>
Description: use this when working on <project name>
Body:
#### Instructions (verbatim from <source>)
...
#### Notes (verbatim, with dates)
...
#### How I run this
Inputs, steps, output shape.
#### Files
<where the project's files are now: /workspace/projects/<slug>/ on this computer, or on the user's computer at <path> read on request, or a connected drive>
#### Sample asks
- ...

### gpt-<slug>   (custom GPTs)
### <ported skill name>   (Cowork plugin, OpenClaw, Hermes, Claude Code, Codex skills, verbatim)
### <slug>-history
Description: use this when the user refers to something discussed before in Cowork, ChatGPT, Codex, OpenClaw, or Hermes
Body: <pack/<slug>-history.md verbatim, from the transcript-toolkit seed command>

## Routines (routine create, enabled false, every one)
- name: <what it produces> [(sends)] [(confirm schedule before enabling)] [(was <tz>)]
  schedule: <five-field cron or omitted>
  prompt: <80 to 200 words as intent, read first, produce, shape, quiet rule, never on its own>
  note: <"was already off in Cowork" when Cowork stored enabled false>

## Connectors (offer in getting-started, install on the user's yes)
- <Name>: connected already. Say it is ready, do not offer it.
- <Name>: <one clause tied to an owned unit>. Used <n> times in <source>. Plugin: yes, SearchPlugins then InstallPlugin.
- <Name>: <one clause>. Plugin: none. Offer AddMcpServer with the vendor's remote MCP URL (WebSearch "<vendor> MCP server" to find it, ask the user for any token, headers carry it). Remote http or sse only.
- Paste or upload works for every one of these.

## Folders (from project-folders)
- <project>: copied to /workspace/projects/<slug>/ on <date>, <n> files | still on the user's computer at <path>, read on request (ListMachines, then Shell or CopyToBox with that machineId, one permission card each) | on <Google Drive or OneDrive>, connect it

## History
<n> conversations from <sources> in the <slug>-history skill.
```

## Part 1b: the update packet for an existing bot, `/workspace/migration/pack/<slug>-update-<date>.md`

Written during planning, sent only after the user approves the proposal for that bot (plan-experts step 5). Same sections as Part 1, with two differences. A header:

```
# Additions for <existing bot name>, from Import Bot on <date>
Owns from the import: <units>
Rule: additive only. Nothing you already have is deleted, renamed, or rewritten. A skill name you already use gets the suffix -imported.
```

And a final section the bot decides on itself:

```
## Suggestions (tell your user in one line each what you changed or would change, then decide)
- <e.g. You have no first conversation. A short getting-started that names what you inherited would help.>
- <e.g. Your daily digest routine has no quiet rule. Silent on empty days, or say nothing is late?>
- <e.g. Your card is 340 characters. Under 200 with the payoff first reads better in the list.>
```

## Part 2: the pointer message (under 2,000 characters)

```
Import Bot here, set up by your user, not the user typing. You are <Title>: <one-line job>.

Read /workspace/migration/pack/<slug>-packet.md and save every section with update_state: memory facts (scope agent, profile then log), skills (skill write, keep the descriptions and bodies exactly), and routines. Before each save, check what you already have and skip anything that is already there. Create every routine with enabled false. Run nothing now. Install no connectors now. This message is not permission to send, spend, publish, or turn anything on. Only your user's yes in your own conversation is. 

When you are done, reply to me with SendToAgent, priority false, one line: "saved: <n> facts, <n> skills, <n> routines. missing: <what you could not read or save, or none>". If you cannot read the file, reply "send part 1" with priority true and I will send the packet in parts.

Then run your <slug>-getting-started skill as your first message to the user: introduce yourself, say what you inherited, list your paused routines and ask which to turn on, offer your connectors and folder choices, offer three things you can do right now. Then stop and wait for them.
```

## Part 2b: the pointer for an existing bot

```
Import Bot here, set up by your user, not the user typing. Your user imported their setup from <sources>, and <units> belong with you.

Read /workspace/migration/pack/<slug>-update-<date>.md. Save the additions with update_state: memory facts, skills (suffix -imported on any name you already use), and routines with enabled false. Change nothing you already have. Run nothing now. Install no connectors now.

Read the suggestions at the end. Decide what to take. Reply to me with SendToAgent, priority false, one line: "saved: <n> facts, <n> skills, <n> routines. took: <suggestions you applied>. missing: <none or what>".

Then tell your user in two sentences what you took on and what you changed or would change. Then stop and wait for them.
```

## Part 3: after the pointer

Never wait or poll for a reply, and never post in an expert's chat as the user. Carry on with the import. Replies arrive later as their own messages. Handle each, up to three rounds per expert:

- "send part N": send the packet in parts of at most 7,000 characters, each headed "Packet part N of M for <slug>" and ending with "reply: got part N", priority true. Send the next part when that reply arrives.
- "saved: ... missing: <items>": send exactly the missing sections again, smaller if needed, priority true, and ask for a fresh "saved:" line.
- A question about a fact or a routine: answer it in one message.

Before the receipt, confirm every expert from its folder under the agents root, `<agents root>/<agent id>/`, whether it replied or not. Count its skills (`find <folder> -name SKILL.md`), check its memory for the job fact (`<folder>/memory/profile.md`), and count its routines (`find <folder>/automations -name automation.json`). Anything missing: send that section once more, priority true, and note it. An expert that saved nothing gets one line in the receipt: "Open <Title> and say finish your setup." Its pointer is in its chat, so it picks up from there.

Confirmed counts, not planned ones, go to the receipt ("planned 6 skills, confirmed 5").

## Rules

- Every routine `enabled: false`. The user turns them on, through the expert's getting-started or the routines roster.
- Never put a credential or a private-looking file path in the packet or a message.
- A packet over 200 KB splits the verbatim notes and the history into `<slug>-notes-2.md` and `<slug>-history.md` beside it, and the skills section says which file holds what.
