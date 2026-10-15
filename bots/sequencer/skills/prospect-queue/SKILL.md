---
name: prospect-queue
description: "Use this to turn the confirmed ICP into new rows on the tracker, during the dry run, on request, or from the weekday queue routine. Sourced or blank, never guessed, and never past the saved cap."
---

# prospect-queue

Part of the Sequencer agent preset.

# Prospect queue

Turn the confirmed ICP into rows on the tracker. Sourced or blank, never guessed.

## When to use

- During the Beat 4 dry run.
- When the user asks for new prospects.
- When the weekday queue routine runs.

## Steps

1. Read `/workspace/sequencer/state.md` for ICP, title winners, the owner filter, the daily cap,
   and the channel map. If ICP is not confirmed, stop and run the auto-discovery ICP card instead.
2. Count rows already queued or active for today. If the cap is filled, stay quiet and stop.
3. Find candidates from the sources the user actually has, in this order:
   - CRM views and saved lists, when a CRM is connected
   - the tracker's own seed rows and past accounts
   - an enrichment tool, when one is connected or signed in
   - web research, when nothing else is available
4. Dedupe against the tracker, recent sent mail, and CRM activity. Someone mid-thread is not a new
   prospect.
5. Research each account only as far as the evidence goes: what they do, the trigger, and one
   reason this person now. Every fact carries a source and a date, or the word Unknown. Never
   reconstruct a plausible fact.
6. Append rows with region, channel_allowlist, status queued, next_due_at, and source. Leave email,
   phone, and profile URL blank when they are not sourced. A blank is honest. A guess is a bounce.
7. Report only when rows were added: how many, from which sources, how many were dropped as
   duplicates, how many are missing an email.

## Contact data

- Use what the source actually shows. Never assemble an address from a pattern, never guess a
  direct dial, never infer a profile URL from a name.
- A row with no email is still useful. It queues a profile-only touch when the channel map allows
  one, or it waits.

## Never

- Invent a contact, an email, a phone, a title, a trigger, or a quote.
- Queue someone the owner filter excludes.
- Exceed the saved daily cap because the pipeline looks thin.
- Buy, scrape behind a login, or pull data from a source the user has not signed into or named.
