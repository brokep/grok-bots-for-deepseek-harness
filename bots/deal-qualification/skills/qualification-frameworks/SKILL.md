---
name: qualification-frameworks
description: "Defines what \"met\" means for each criterion of MEDDPICC, MEDDIC, BANT, SPICED, or the team's own framework, so every audit scores the same way."
---

# qualification-frameworks

Part of the Deal Inspector agent preset.

# qualification-frameworks

## When to use

`stage-gate-audit` reads this before scoring. The owner may also ask to change or explain a criterion.

## The team's framework wins

If memory holds a custom framework (set in `getting-started`), score against it and use the definitions below only as a reference for how strict "met" should be.

## MEDDPICC (default)

- Metrics: the customer stated a measurable outcome they want (a number, a date, a cost). "Faster" is not a metric; "cut release time from two weeks to three days" is.
- Economic buyer: the person who can approve the spend is named, and either attended a call or was confirmed by name by someone who knows.
- Decision criteria: the customer said how they will judge options (security review, integration, price, a pilot result).
- Decision process: the steps and owners from evaluation to signature were described, with a timeframe.
- Paper process: procurement, legal, and security steps were named, or the customer confirmed there are none.
- Identified pain: the customer described the problem in their own words and its cost to them. Our description of their problem does not count.
- Champion: a named person who has said, on a call, that they want this and will work internally for it. Enthusiasm is not championship; action is.
- Competition: the alternatives they are considering, including "do nothing" and internal build, were named.

## MEDDIC

MEDDPICC without paper process and competition.

## BANT

Budget (a number or a confirmed allocation), Authority (the decision maker named and reached), Need (pain in their words), Timeline (a date or an event that forces one).

## SPICED

Situation (their current setup, stated), Pain (in their words), Impact (the cost or upside quantified by them), Critical event (a date that forces a decision), Decision (process and people).

## Scoring rules

- Met requires a customer quote. Partial requires a quote plus a named gap. Anything else is Missing.
- A criterion met on a call 90 or more days ago is Partial until re-confirmed.
- Never count what a rep said to the customer as evidence of the criterion.
