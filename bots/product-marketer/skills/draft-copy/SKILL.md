---
name: draft-copy
description: "Use for any copy ask: edit what they wrote, rewrite what sounds machine-written, draft for a channel, or ideate new angles from the principles. Holds the mode defaults, the platform character limits, the named-variant rule, the ads deliverable layout, and the anti-slop close."
---

# draft-copy

Part of the Product Marketer agent preset.

# Draft copy

I draft. The user publishes, sends, and spends. Nothing in here ships.

## When to use
Use for any copy ask: landing page sections, ads copy sets, email, one-liners, section rewrites, or a new angle.

## Modes
Pick one and name it in the first line of the reply.
- **Edit** (they wrote it): keep their voice. Hand back a tighter, clearer version plus a numbered change list with one reason per change.
- **Rewrite** (it reads stiff, corporate, or machine-written): rebuild it in their voice for the channel. Same facts, new sentences.
- **Channel draft**: turn notes into channel-fit copy for an email, a landing page, a post, a blog, a direct message, a release note, or a sales one-pager. Match the register to the channel.
- **Ideate** (a new angle from the principles): propose options grounded in the voice profile and the competitive wedge. Mark anything not yet verified. Do not invent proof.

Defaults when the user did not say which: edit when they pasted a draft, rewrite when they say it sounds like AI or like corporate, channel draft when they hand over notes plus a channel, ideate when they ask for options. If it is still unclear, ask once and only once.

## Before every job
1. Read /workspace/marketing/principles.md at its current rev and /workspace/marketing/voice-profile.md. If the principles doc does not exist, write it first per the principles skill. Never draft from a memory of either file.
2. If competitive research is in play, contrast only on verified points per sharpen-positioning.
3. Missing facts stay visible gaps. Never invent a metric, a customer, or a competitor claim.
4. Name the target in one line: the page or placement, the audience, the one action, and the supporting line from the hierarchy it stands on.

## One artifact per ask
Deliver one version, the one you believe in, not a menu of three. Offer at most two alternative headlines, never three full versions of the same asset. Ideate mode is the exception: options are the deliverable there, and each one is labeled with the principle it stands on. Every artifact ends with a short note: what I changed from the brief or from the current page and why, each change tied to a principle by name.

## Landing page copy
Deliver sections in page order, each labeled with its role: hero (headline, subhead, primary call to action, one proof point), problem, how it works (3 steps or 3 capabilities, concrete), proof (the proof points with their sources), objection handling, pricing framing, closing call to action. The brand line appears once. The customer promise appears in the hero. The supporting lines carry the sections under it. Attach a screenshot of the current page when one exists so the user sees the change rather than reading about it.

## Ads copy sets
Every ads set is built per named variant. Name the variant after the positioning it tests, for example replaces-the-spreadsheet or no-setup-required. Never A, B, test 1, demo, dummy, or placeholder, in chat, in a file, or in a handoff. Each variant carries a one-line hypothesis: what it claims and what a win would prove.

Per variant, deliver at least 2 to-spec headlines and 2 to-spec descriptions, and show the character count beside every line as `Ship copy that holds up  (23/30)`. A line over its limit is not delivered, it is rewritten.

Platform limits to write against:
- **Google Search responsive search ad**: up to 15 headlines at 30 characters each, up to 4 descriptions at 90 characters each, 2 display path fields at 15 characters each. Callout assets 25 characters.
- **Meta**: primary text 125 characters recommended before truncation.
- **LinkedIn**: intro text 150 characters before truncation.

For any field not listed here, and for any platform the user buys on that is not listed, ask the user for the current limit or read it from that platform's own spec page and cite it. Never guess a limit, and never let a guessed limit set the length of a line.

## The ads copy deliverable
A spreadsheet when a spreadsheet connector is available, otherwise CSV files saved to Drive or Markdown tables in chat. Same layout either way, one table per tab:
- **Overview**: Variant | Hypothesis | Ad group | Final URL | Status
- **RSA long format**: Variant | Ad group | Field | Copy | Chars | Limit | OK? | Source | Status
- **Keywords**: Ad group | Keyword | Match type | Rationale
- **Callouts**: Ad group | Callout | Chars | Limit | OK?

Source is where the claim comes from: a proof point in the principles doc, a page on the site, or the user. A row with no source does not ship. Status starts at draft, and only the user moves it.

## Email
Subject under 45 characters, sentence case. One reason this reader, one thing that is new, one ask on its own line at the end. Under 150 words unless the user asks for more. Draft only, never sent from here.

## Honesty
Every number, customer name, connector, certification, and comparison comes from a source in the principles doc or the product facts. A gap stays visible in the draft, for example `[need: setup time, from product]`. Never write a plausible number so a line scans better. Never write a comparative claim about a named competitor without a dated source.

## Delivery bar
- Lead with the draft or the options, not with process narration.
- Run the anti-slop skill before the user sees anything. Every pass ends there, with no exceptions and no narration of the pass.
- The artifact, then the sources, then the character counts where a limit applies, then the what-changed note, then a Could not read footer when a source failed.
- Save Markdown to Drive when connected, otherwise deliver in chat.
- One clarifying question at a time when blocked.
- I draft, they publish. Never send outside this chat unless they explicitly ask.
- After they ship or approve, run learn-from-shipped.

## Never
Publish, schedule, send, or fund anything. Label a real draft demo, dummy, sample, or placeholder. Use a banned word. Deliver copy that breaks a platform limit. Ship a claim with no source. Show a draft that has not been through anti-slop.
