---
name: principles
description: "Use to write or revise the positioning principles doc, the one artifact every piece of copy is measured against. Holds the six sections, the proof-point rule, the banned-word list, the writing bar, versioning, and the in-place revision loop."
---

# principles

Part of the Product Marketer agent preset.

# Principles

The positioning principles are the one artifact everything else is measured against. One doc, versioned, re-read before every draft and every review. The voice profile at /workspace/marketing/voice-profile.md is its companion and is read alongside it.

## When to use
Use to write the doc the first time, to revise it after feedback, after a positioning sharpen, or when the product, pricing, or ICP changes.

## The doc
Path /workspace/marketing/principles.md. A copy goes to Drive when it is connected, otherwise it lives in the workspace and is pasted into chat on request. Sections, in this order, and no others unless the user asks:

1. **Position**: one sentence. Who it is for, what it does, what it replaces, why it wins. No adjective survives without a proof point behind it.
2. **ICP**: the buyer and the user, their job, the moment they go looking, and who this is explicitly not for.
3. **Product Story**: what the product actually does, in concrete observations, in the order a buyer needs them. Each observation carries a source. Proof points live here: up to 7, each with a number or a named example, a source, and a date.
4. **Messaging**: the hierarchy, always in this order. Brand line, then customer promise, then 3 to 5 supporting lines. Each supporting line names the proof point it stands on.
5. **How It Shows Up**: what the hierarchy looks like on the home page, on the pricing page, in a search ad, in a social ad, and in an email. One or two lines each, not full copy.
6. **Voice and Creative Rules**: the tone rules from the voice profile, the banned words, punctuation and capitalization, headline case, and the contrast rule. Contrast sparingly, and never against a named competitor without a dated source in this doc.

Skip Route Strategy and Strategic Test sections unless the user asks for them.

## The banned-word list
Start from the words the user's own samples never use, then add the house list: revolutionary, game-changing, seamless, robust, powerful, supercharge, unlock, empower, streamline, world-class, cutting-edge, best-in-class, effortless, next-generation, leverage as a verb. Add anything the user bans. The list is enforced by copy-review and by the anti-slop pass on every draft.

## Writing bar
Calm, economical, specific, adult. Not blunt telegrams, not AI-sloppy framework dumps. Short prose that breathes. Concrete product observations over brand adjectives. Vary sentence length. No exclamation points, no emojis unless the user's samples use them. No em dash and no en dash. No semicolons. Every rev is written against this bar and against the voice profile, and the anti-slop skill holds the full shape list.

## Versioning
Every rev carries a header line: `rev N, YYYY-MM-DD, changed: <one line>`. Before writing a new rev, copy the current file to /workspace/marketing/revs/principles-rev<N>-<date>.md. Never overwrite without keeping the old rev.

## Revisions from feedback
When the user leaves comments or feedback on the doc, update that same doc in place. Do not open a new doc, do not fork a variant. Work the comments in order, mark each resolved or still open, and ping in one line when the next rev is ready. After the rev, list which drafted copy was written against the old rev and is now stale, and offer to refresh it.

## Unknowns
A section you cannot fill from a source stays in the doc with the gap marked, for example `[need: churn number, from the user]`. Never write a plausible line in place of a fact. Count the open gaps at the top of the doc so the user can see what is still missing.

## Output
The doc written, a 6-line summary in chat (Position, ICP in one line, the brand line, the customer promise, the count of proof points, the count of open gaps), and the rev and date saved to memory.

## Never
Invent a proof point, a customer, or a number. Delete a rule the user set. Ship a rev with no date and no changed line. Keep two competing positioning docs.
