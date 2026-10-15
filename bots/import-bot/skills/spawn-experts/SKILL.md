---
name: spawn-experts
description: "use this to create every planned expert, hand each its packet, and give it its history skill"
---

# spawn-experts

Part of the Import Bot agent preset.

# Spawn experts

Creates every expert in the plan and hands each its packet. History travels as a skill on the expert.

## Before creating anything

Two kinds of owner in the plan. A new expert is created once the user tapped Set them up under the plan table (plan-experts step 5). That tap is the yes for creating each one and messaging it its packet. An existing bot (found in setup step 2, or one this bot created in an earlier run per `/workspace/migration/pack/spawn-plan.md`) only ever receives a proposal: the update packet (expert-packet Part 1b) and the existing-bot pointer (Part 2b) are sent after the user's yes for that bot, never before. "Yes but skip the improvements" sends the packet without its Suggestions section. "No" parks the units. "Make a new expert instead" adds a new expert to the plan for those units. Ask this computer which connectors are already connected (`GetMcpServerStatus`) and mark them "connected" in every packet, so no bot offers a connection the user already has.

## For each expert, in plan order

0. **Differentiation.** Across all planned experts, no two share a skill name, a routine name, or a cron. Two playbooks that read nearly the same mean one expert too many. Merge before going on.
1. **Packet.** Write `/workspace/migration/pack/<slug>-packet.md` per the expert-packet skill. Run the pre-spawn check from bot-design-standard. Fix the noes.
2. **History seed.** Pick the 12 most recent sessions tied to this expert's units from `pack/sessions/index.json`: Cowork sessions by project or title, ChatGPT and Claude conversations by title and content, Hermes and OpenClaw sessions by skill or agent, Codex and Claude Code by repo. Run the transcript-toolkit seed command. The `<slug>-history.md` goes into the packet as the `<slug>-history` skill.
3. **Create.** `CreateAgent` with the title and the card.
4. **Pointer.** `SendToAgent` the Part 2 message from expert-packet with `priority: true`, so the expert wakes now and saves its packet. Do not wait for its reply. Go on to the next expert.
5. **Log.** Append to `/workspace/migration/pack/spawn-plan.md`: title, agent id, packet path, history sessions count, timestamp.
6. **Replies.** Each expert's reply arrives later as its own message. Handle it per expert-packet Part 3, and keep going with routines-roster and connectors-encourage meanwhile. Before the receipt, confirm every expert from its files (expert-packet Part 3). Confirmed counts go in the receipt.

## Tell the user

One line per owner as it lands. New: "<Title> is up. It takes care of <units> and knows your <n> past conversations about this." Existing, after the yes: "Sent to <Name>. It will tell you what it took on and what it changed." Then: "Open any of them and say hi. New ones introduce themselves, show you their paused routines, and ask which to turn on." Parked units get one line: "<units> are waiting for your call. Say send them to <Name> or make a new expert any time."

## If the plan has one expert and the user has many projects

Still one expert. The projects are playbook skills on it. Say why in one line.

## If two experts would be identical

Merge before spawning. Two bots that match the same situation both fail at it.
