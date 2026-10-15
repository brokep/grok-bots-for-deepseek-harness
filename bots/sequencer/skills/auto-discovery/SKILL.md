---
name: auto-discovery
description: "Use this when a connector lands or a fallback is accepted, and when the user asks to refresh voice, ICP, or title winners. Scans, proposes confirm cards, and is honest when the scan is thin. Nothing saves without a yes."
---

# auto-discovery

Part of the Sequencer agent preset.

# Auto discovery

After each connector lands or a fallback is accepted, infer the voice, the ICP, title winners, and
the skip rules from live data. Propose. Never save an inference the user has not confirmed. Be
honest when the scan is thin.

## When to run

- Right after mail, tracker, CRM, calendar, team chat, enrichment, or call notes connects, or after
  a paste or export is accepted in its place.
- On demand: refresh voice, re-infer ICP, refresh title winners.
- Never silently overwrite a confirmed card. Diff it and ask.

## Lanes

### Mail (the voice lane)

1. Scan sent outbound plus threads with a positive reply or a booked meeting. Weight recent booked
   meetings highest.
2. Prefer real prospecting mail and replies to prospects over internal one-liners and calendar
   noise. Strip signatures and quoted threads before analysing.
3. Propose a voice card: greeting, opener pattern, the ask, length and paragraphing, sign-off,
   words used and avoided, and proof style only where proof is actually in the samples.
4. Propose opener and CTA winners ranked by outcome when outcome labels exist, booked above
   positive reply above neutral.
5. Cross-check booked outcomes against the calendar when one is connected.

### CRM

1. Discover the real object, field, and stage names through crm-adapter. Never assume a stage label.
2. Map replies, meetings, and won deals to titles and segments.
3. Propose title winners and segment hints, with the counts behind each.
4. Propose the ownership filter, the open-opportunity stage that pauses sequencing, and any
   do-not-touch flag the CRM already carries.
5. If there is no CRM, continue on the tracker alone and say plainly what cannot be inferred.

### Tracker

1. Read the headers. Map to the sequence columns in sheet-brain, or create them.
2. Infer region and channel mix from existing rows when rows exist.
3. Never invent contacts to fill an empty sheet.

### Optional lanes

- Enrichment or web research for firmographics and triggers. Cite the source and the date, or mark
  it Unknown.
- Call notes for pain language only when the note exists. Never invent a quote.
- Team chat for internal triage context, never for cold voice training.
- Calendar for booked-meeting confirmation and review blocks.

## Confirm cards (required before save)

One card at a time, or a short stack:

1. **ICP**: industries, size bands, regions, buyer functions, editable.
2. **Voice**: sample lines with Keep, Tweak, or Drop on each line.
3. **Title winners**: ranked, with Keep, Remove, or Add.
4. **Channel map**: region to allowed channels, editable, an example and not a lock.
5. **Skip and pause rules**: owner filter, open-opportunity stage, already-touched window.

Persist only what the user confirms, and persist it to `/workspace/sequencer/state.md` as this
user's preference. Nothing about the stack or the cadence carries over from whoever built this
recipe.

## Thin-scan honesty

- Fewer than about 5 usable outbound samples: say the voice scan is thin, ask for about 3 pasted
  emails or a CSV, and do not draft cold copy from a thin card.
- CRM empty or unreadable: skip title and segment inference, ask for a seed list.
- Conflicting signals, for example a formal and a casual voice or two title clusters: surface the
  conflict in a widget. Never average two voices into one.
- A connector that fails mid-scan: switch to the paste path quietly and say what could not be read.

## Output

- Proposed cards in chat with confirm widgets.
- A short what I inferred and what I still need summary.
- Never claim discovery is complete when coverage is partial.

## Never

- Save an inference before it is confirmed.
- Invent research, contacts, outcomes, or proof.
- Send anything. This skill reads and proposes.
