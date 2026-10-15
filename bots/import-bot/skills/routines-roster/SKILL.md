---
name: routines-roster
description: "use this after spawning to lay out every routine across all experts, paused, and turn them on when the user picks"
---

# routines-roster

Part of the Import Bot agent preset.

# Routines roster

After the experts are up, lay out every routine across all of them so the user sees the whole rhythm at once and can decide what to turn on. They arrive paused. Each expert also lists its own in its first conversation, so this is the overview, not the only place.

## Table

| Routine | Bot | Produces | When (plain words) | Quiet rule | Start with it |
|---|---|---|---|---|---|

- "Produces" is the output, in one clause. Never "runs the pipeline review". Instead "the Friday stale-deal table for the RVP".
- "When" comes from the cron in plain words. For a routine marked "(confirm schedule before enabling)", write "schedule needs your confirmation".
- "Quiet rule" is "silent on empty days" or "says nothing is late".
- "Start with it" gets a yes for at most three routines: the ones with the most session evidence, or the ones the user named in setup.

Under the table, one line each:
- "These were on in Cowork: <names>." and "These were already off: <names>."
- "Anything marked (sends) messages someone when it runs. Turn those on last."
- "Say turn on <name>, or pick in each bot's first chat. I will tell the bot."

## Turning one on from here

The routine lives on the expert, and a request relayed by this bot is not the user's yes to that expert. On "turn on <name>": tell the user "Open <expert> and say turn on <name>, it switches it on there." Also `SendToAgent` the owning expert a heads-up: "Your user said in Import Bot's chat they want <name> on. Ask them in your own conversation and enable it only on their yes there." Never ask an expert to enable anything on this bot's word alone.

## Routines that did not map

A scheduled task with no clear owner went to the expert closest to its topic. If none fit, it went to the expert with the most routines, named as is, and the roster marks it "check the owner". Never drop one.
