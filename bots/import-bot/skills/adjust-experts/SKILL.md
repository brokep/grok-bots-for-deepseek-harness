---
name: adjust-experts
description: "use this when the user wants to rename, move a project, merge, split, or add to the experts after they were created"
---

# adjust-experts

Part of the Import Bot agent preset.

# Adjust experts

The user shapes the experts afterwards through this bot. Every adjustment is one message from the user and a short confirmation back.

## Rename

"Call <old> <new>." Check the new name against bot-design-standard (says the job, four words or fewer). If it hides the job, rename anyway and tell the expert to say its job in its first line. `UpdateAgent` with the new name. Tell the expert with `SendToAgent`: "Your user renamed you to <new>. Update your job fact and introduce yourself with the new name."

## Move a unit

"Move <project or task> to <expert>." Write `pack/<slug>-update-<date>.md` for the receiving expert with that unit's playbook, memory facts, routine, and connectors, and a short pointer message as in expert-packet Part 2 (with the same reply protocol). Tell the giving expert: "Your user moved <unit> to <expert>. Delete its skill project-<slug>, its routine <name>, and its memory facts with update_state, then reply saved:." Update `pack/expert-plan.md` and `spawn-plan.md`.

## Merge two experts

"Merge <A> into <B>." Move every unit of A into B as above, then tell A: "Your user merged you into <B>. Tell them so in one line and stop." Grok Bot has no delete tool for bots, so say: "<A> is empty now. To remove it, right-click it in the sidebar and choose Delete." Re-run bot-design-standard on B's anti-jobs, since one of them just vanished.

## Split an expert

"Split <A>, put <units> in a new one." Plan the new expert with plan-experts step 4, create it with spawn-experts, move the units, fix anti-jobs on both.

## Send a parked proposal

"Send the pipeline work to <bot>" or "make a new expert for it": the parked units from the receipt go out as an update packet to that bot (with or without the suggestions, as they say) or become a new expert through spawn-experts. Update the receipt's "waiting for your call" table.

## Add a missed workflow

"You missed <thing>." Treat it as a user-named workflow: find evidence with the transcript-toolkit search, assign an expertise, add it to the owning expert as a playbook or routine through an update packet, or create a new expert if nothing fits. Add it to the receipt under "added afterwards".

## Strike a memory fact

"Strike <n>" or "forget that I <fact>": `update_state` memory forget with the exact text, scope user. Confirm in one line.

## Turn a routine on or off

Relay to the owning expert per routines-roster.

## Re-seed history

"Give <expert> more history" or "less": re-run the transcript-toolkit seed with different limits, send the new `<slug>-history.md` as an update packet replacing the history skill.

## Always

Update `pack/expert-plan.md` after any change, so a resync routes new items to the right expert. Confirm in one line, no recap of what was not changed.
