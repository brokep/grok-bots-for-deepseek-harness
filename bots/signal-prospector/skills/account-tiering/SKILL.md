---
name: account-tiering
description: "Scores and tiers accounts inside each motion using weighted signal dimensions the owner can see and tune, so the weekly list is defensible."
---

# account-tiering

Part of the Signal Prospector agent preset.

# account-tiering

## When to use

After `signal-scan`, or when the owner asks to tier or prioritize a set of accounts.

## Dimensions and default weights

Score each account 0 to 3 on every dimension, multiply by the weight, sum. Weights live in memory as "Tiering weights"; the defaults are:

- Product traction (weight 3): signups, activation, usage trend on corporate domains.
- Hiring and initiatives (weight 3): job posts in our category, public programs that match the POV, an initiative the account announced in its own posts.
- Leadership (weight 2): a new or vocal leader in the buying center.
- Pipeline history (weight 2): prior conversations, past trials, a lost deal whose reason has aged out.
- Champion (weight 2): a known power user or advocate at Director level or above.
- Fit (weight 1): size, industry, geography match to the ICP.
- Customer lookalike (weight 1): resembles a current customer in industry and size.

Expansion and renewal use the same dimensions but read traction as growth or decline against the contract, and treat a champion who went quiet as a negative.

## Tiers

Within each motion: Tier 1 is the top 20% by score with at least one strength-3 signal in the window, Tier 2 the next 30%, Tier 3 the rest. An account with a strong signal and poor fit stays out of Tier 1; say why.

## Output

One table per motion: Rank, Account, Tier, Score, Top signals (two, with sources), Why now (one line), Suggested persona. Under the table, the weights used and a plain-text offer to adjust them.

## Rules

- Exclude accounts with open opportunities or active contracts from the net-new list unless the owner asked for them.
- Show the score math when asked. No black boxes.
- Deprioritize IT services and consulting firms unless they show adoption or a public initiative that fits.
- Read-only.
