---
name: outbound-voice
description: "Use this to learn the user's outbound voice from their own sent mail and booked meetings, and to draft any cold touch, follow-up, or touch arc in it. Drafts only, on every channel."
---

# outbound-voice

Part of the Sequencer agent preset.

# Outbound voice

Learn the user's outbound voice from their own mail and their own wins, then draft in it. Drafts
only, on every channel.

## When to use

- After the voice source lands during setup.
- When the user asks to refresh voice, draft cold copy, rewrite a draft, or build a touch arc.
- Before any batch of sequence drafts, so the copy matches the confirmed card.

## Train from wins

1. Scan sent outbound plus threads with a positive reply or a booked meeting. Weight recent booked
   meetings highest. Confirm booked outcomes against the calendar when one is connected.
2. Prefer real prospecting mail over internal notes. Strip signatures and quoted threads first.
3. Build the style profile and surface sample lines for Keep, Tweak, or Drop:
   - greeting and sign-off
   - length and paragraphing
   - opener pattern
   - the ask, and where it sits
   - words they use and words they never use
   - proof style, only if proof appears in the samples. Never invent a logo, a metric, a mutual
     connection, or a customer name.
4. Save the confirmed voice card to VOICE CARD in `/workspace/sequencer/state.md` and reuse it on
   every draft. Refresh when the samples age past about 30 days or when the user asks.
5. Thin scan, fewer than about 5 usable samples: say so, ask for about 3 pasted on-brand emails or
   a CSV with subject and body, and hold cold copy until there is a source.

No connected mail is not a blocker. Pasted samples produce the same card, marked as pasted.

## Draft

1. Confirm the persona, the region and channel allowlist for that row, and the trigger. If the
   trigger has no source, write `[needs source]` rather than inventing one.
2. Draft in the confirmed voice, read from VOICE CARD in `/workspace/sequencer/state.md`. Match
   the greeting, the ask, the length, and the sign-off from the card, not a house style.
3. Run humanizer as the last pass. It changes cadence, never claims.
4. Present as a draft: a mail draft where mail is connected, otherwise draft text in chat. LinkedIn
   and WhatsApp are always text in chat for the user to paste, because neither has a connector.
5. A touch arc is 2 to 4 touches, still drafts only. Each touch does a distinct job. A paraphrase of
   touch 1 is not touch 2.

## Clarifying widgets

- Which threads count as wins: Booked meetings / Positive replies / I will paste specific threads /
  All recent sent prospecting
- Include follow-ups in training: Yes / Cold openers only / Keep them as separate cards
- Thin scan: Paste about 3 emails / Upload a CSV / Connect mail now / Skip for now

## Never

- Send, schedule-send, or post on any channel.
- Invent proof, logos, metrics, mutuals, customer names, or activity.
- Train cold voice from internal chat banter alone.
- Use a house voice when the user has a confirmed card.
