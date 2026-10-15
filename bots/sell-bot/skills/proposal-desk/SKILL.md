---
name: proposal-desk
description: "Use for proposals, quotes, expansion deals, contracts, and won or lost."
---

# proposal-desk

Part of the Sell Bot agent preset.

# proposal-desk

From first proposal to signed.

## Proposal

From the account file (what they asked, call learnings) and Prices and terms in setup.md. A missing price or term: ask the user, and offer to save the answer under Prices and terms.
proposals/<slug>-<date>.html, self-contained and under a page: their goal in their words, what they get (plan, seats or volume, services), price and term, what is not included, next steps with dates, and who signs, with versions logged in the account file. Attach it in chat with a cover email per draft-email, attached to the draft through UploadFile when email is connected. The stage moves to proposal once it is sent.

## Expansion deals

From account-watch, call-wrap, or the user: a pipeline.csv row with stage expansion, the signal with numbers and dates, the plan or volume that fits, the price change from Prices and terms, and why now. Draft the note to their buyer and the updated quote.

## Contract back-and-forth

Questions or redlines: read the thread and any attachment (download it, or ask the user to paste the clauses). For each change: what they want in plain words, the risk to the user, never softened, and a suggested position from setup.md, then draft the reply. Track open points in the account file until both sides agree.

## Won or lost

Signed or paid: stage customer, with what they bought and what was promised in the account file. A no: stage lost (an expansion row just closes), with their reason in their words.

## Never

Send a contract, offer a discount or term outside setup.md, or put one account's price in another's proposal.
