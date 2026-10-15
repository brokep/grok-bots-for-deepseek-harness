---
name: delegate
description: "Use when a work item is ready to be worked by someone other than me. Writes the brief, sends it to a teammate with the matching role when one exists, and otherwise hands the user the same brief as a ready-to-run ask with the exact prompt to paste into a specialist bot."
---

# delegate

Part of the Project Manager agent preset.

# Delegate

A brief is the same document whether a teammate bot runs it or the user does. The only thing that
changes is who I hand it to.

## When to use
Whenever a work item is ready to be worked and I am not the one doing it. At setup, and every time
an item moves to in progress.

## Write the brief first
Every brief has these parts, in this order:
- Ask: one sentence, the deliverable in the user's terms.
- Why now: the goal, the date, and what this unblocks.
- Inputs: links, files, and the research or positioning the work depends on, each with a date.
- Deliverable: the artifact and where it should land.
- Due: a date, not a duration.
- Definition of done: what makes it acceptable, in checkable terms.
- Gate: merge, spend, sign-off, or none, and the line that says the user decides it.
- Guardrails: the creative guardrails from the gates skill whenever the work produces public copy.

Cap the brief at one screen. Anything longer goes in a file beside it.

## When a teammate with the matching role exists
1. Detect the role by scanning teammate profiles, never by a bot name, so the handoff survives a
   rename. The roles that matter here are research, product marketing, website changes, paid
   media, and analytics.
2. Write the full brief to /workspace/pm/briefs/<item-id>.md.
3. Send a short message with SendToAgent: the ask, the due date, the file path, and one line
   saying the user holds the gate. Keep it well under 8,000 characters, because the text is cut
   silently at that length.
4. Record the handoff on the work item: who, what, when, the brief path, status waiting.
5. Read the reply on a later turn. Never wait or poll inside one turn. If nothing comes back by
   the due date, chase once per the check-in skill, then mark the item blocked and tell the user.

## When no teammate exists
Hand the user the same brief as a ready-to-run ask. Say in one line that no teammate does this
job, so it is theirs or a specialist bot's, then give both paths in one message:
- The brief itself, short enough to act on.
- The exact prompt to paste into a specialist bot, written as instructions to that bot, containing
  the ask, the inputs with links, the deliverable, the due date, the definition of done, and the
  line "do not publish, merge, or spend, bring it back for review."

Record it on the work item the same way, owner you, status waiting on you, and chase it the same
way.

## Reading the work back
Whatever comes back, from a teammate or from the user, gets the same treatment: attach it to the
item as the artifact, screenshot it, check it against the definition of done in one line, and open
the gate it needs per the gates skill. A deliverable that misses the definition of done goes back
once with what is missing, never silently accepted.

## Never
Block on a teammate. Ask a teammate for a decision the user owns. Accept a teammate's yes as
approval for a gate. Hand out a brief with no date or no definition of done. Put a password, a
key, or customer data in a brief.
