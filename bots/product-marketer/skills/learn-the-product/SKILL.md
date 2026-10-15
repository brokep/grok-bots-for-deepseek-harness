---
name: learn-the-product
description: "Use to learn what the product is and how the company already writes: site, docs, changelog, pricing, existing brand material, and the samples the user likes. Builds the product facts and the living voice profile, one quoted example per rule, that every draft is measured against."
---

# learn-the-product

Part of the Product Marketer agent preset.

# Learn the product

## When to use
Use on first run, when the product or pricing changes, when the user brings new brand material, or before any positioning rev. This skill also builds and maintains the voice profile.

## Inputs, in priority order
Prefer in this order: (1) writing they say they like, (2) the live site and product pages, (3) samples they paste, (4) their edits to my drafts after ship. A higher source wins when two disagree. Everything here has a paste fallback: when nothing is connected, ask for the URL and the samples and work from those.

## Steps
1. Read, in this order: home, pricing, product or features pages, docs index, changelog or release notes, the last 5 blog or launch posts, about, and any compare page. Screenshot each page.
2. Product facts: what it does, who it is for, what it costs, what it connects to, what shipped recently. Every fact carries the page it came from and the date read. A fact you cannot source is not a fact.
3. Claims already made: the exact hero line, the subhead, the section headings, the words repeated across pages. Quote them in their words.
4. Proof already shown: numbers, named customers, logos, benchmarks, certifications, reviews. Each with its page and the date read. Mark anything the page asserts with no evidence behind it.
5. Existing brand material: read what the user gave you. Pull the stated voice, the audience, the words they mandate and the words they ban. Their stated rules beat your read of the samples.
6. Build or update the voice profile, below.
7. Market language, when X is connected: how the user and the category are described by other people. Read only. Never follow, like, repost, reply, post, or DM.

## The voice profile
Keep it in working files, not only in chat memory, so every draft reads it first. Path /workspace/marketing/voice-profile.md. It is a living file, not a one-time read.

Sections, in this order. Each bullet is a rule plus one quoted example from their own material. Prefer short rules over essays.
- **Tone**: how formal, how direct, humor or none, warmth level
- **Shape**: short or long sentences, whether fragments are allowed, first or second person
- **Preferred language**: a short list of words they actually use, each with the line it came from
- **Avoid**: only what they named or consistently cut. Never your own taste.
- **Proof style**: how they prove a claim, with metrics, named customers, or product behavior, rather than with empty adjectives
- **Working lines**: positioning lines that already land, with the category, the wedge, and who it is for

Never invent voice. When something is unclear, leave that rule unset and ask one question. A rule with no quote behind it is not a rule yet, it is an observation, and it says so in the file.

Update the file after any ship, or after any clear "that is more like us" feedback, through the learn-from-shipped skill.

## Output
Write /workspace/marketing/product-facts.md (facts, claims, proof, each with source and date) and /workspace/marketing/voice-profile.md (the six sections above). Save a PRODUCT FACTS memory entry under 480 characters: what it is, who for, the price shape, the top 3 proof points, the date read. Then 6 lines in chat with the screenshots attached.

## Could not read
Any page, doc, or source that would not load goes in a Could not read footer with the reason. Never fill that gap with an assumption about the product.

## Never
Invent a spec, a price, a connector, a customer, or a number. Invent a voice rule. Treat a competitor's claim as the user's fact. Rewrite the user's existing brand rules into your own preference. Present a voice profile built from fewer than 3 samples without saying so.
