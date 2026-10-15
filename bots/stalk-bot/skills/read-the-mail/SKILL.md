---
name: read-the-mail
description: "Use for the newsletter pulse and sequence anatomy modules. Reads new mail at each competitor's research identity since the last pulse, classifies it, extracts positioning and offers."
---

# read-the-mail

Part of the Stalk Bot agent preset.

# Read the mail

## Inputs
Competitor, research identity, last pulse timestamp. If a teammate identity bot holds the inbox, send AUTH REQUEST need forward-thread with details "all messages since <timestamp>, summaries with subject, sender, date, and any offer or launch" and read the AUTH RESULT on a later turn. Otherwise list messages myself.

## Steps
1. Pull every message since the last pulse.
2. Classify: newsletter, product update, sales sequence (from a named person, asks for a meeting or reply), transactional (confirmations, receipts), event, other.
3. For newsletters and product updates: extract the headline, the main announcement, positioning phrases (how they describe themselves and their customer), any pricing or promotion, any competitor named (including us). Append to /workspace/dossiers/<competitor>/newsletters.md with date and subject.
4. For sales sequence: append to /workspace/dossiers/<competitor>/sequence.md as day N since signup, sender, subject, the ask, the proof used, CTA. Never reply to competitor marketing or sales emails. Confirm links for subscriptions are fine. If the user explicitly instructs a specific reply in chat, send exactly that and record it in sequence.md.
5. Note frequency: issues per week.

## Output
Per competitor: new issues with one-line summaries and links, positioning phrases that are new since last pulse, promotions, sequence progress ("day 6 of their nurture, third email asks for a demo"). Nothing if no new mail.
