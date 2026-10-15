---
name: routine-pitch-call-review
description: "Scheduled routine: Weekday evening review of recent pitch-call transcripts with structured coaching"
---

# Post-pitch call review

Part of the Dan Lanning agent preset.

Schedule, as written by the template author: Weekday evening review of recent pitch-call transcripts with structured coaching

## What to do on each run

Standing: after the user's external partnership or sponsorship pitch calls (and notable internal strategy or leadership calls), review the transcript and coach them on delivery.

Each run:
1. Check meeting notes from the last ~24 hours (Notion meeting-notes query; confirm schema first). Cross-check Google Calendar for yesterday and today to separate real external or multi-person pitch calls from internal 1:1s or solo blocks.
2. Focus on EXTERNAL partnership, sponsorship, or discovery calls with counterparts (sports properties, venues, agencies, vendors) and high-stakes internal strategy calls. SKIP: routine internal syncs, solo focus blocks, coffee chats, standups.
3. Dedupe: track already-reviewed call page IDs in a local reviewed-calls log; never coach the same call twice.
4. For each new qualifying call: fetch the full transcript (transcript usually at the bottom of the meeting note). Produce coaching in this structure: (a) What they did well (3–5 specifics, quote real moments); (b) Where to improve (4–6 actionable, tied to actual lines); (c) Recurring patterns vs known themes; (d) "instead of X, try Y" phrasing upgrades from their actual words; (e) short pre-call checklist. Skip sales-101; every point ties to the transcript. Reference known themes (giving away leverage early, inconsistent qualification, hedging filler, not owning the close) and note whether they are improving or repeating.
5. Log each reviewed call plus top fixes so feedback compounds.
6. Deliver the coaching to the user. If nothing new qualifies, STAY QUIET — no filler.

Fill-ins for the installer:
- Meeting-notes source (e.g. Notion)
- Calendar source (e.g. Google Calendar)
- Delivery path to the user
- Local path or doc for the reviewed-calls dedupe log

Fires on:
- cron `0 18 * * 1-5`

Ask the importing user for:
- Timezone
