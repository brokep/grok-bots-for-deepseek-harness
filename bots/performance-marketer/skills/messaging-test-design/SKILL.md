---
name: messaging-test-design
description: "Use when planning a test, when the user asks how long to run one, or when reading results. Holds the one-variable and one-platform rules, the minimum clicks and minimum days, what a cheapest-click shell can and cannot measure, what invalidates a read, and how a winner is called."
---

# messaging-test-design

Part of the Performance Marketer agent preset.

# Messaging test design

A messaging test answers one question. Everything in the build exists to keep the answer readable.

## One variable, one platform
Each test changes exactly one thing across the variants: the promise, the headline theme, the
proof, or the call to action. Everything else is held constant, targeting, exclusions, final URL,
budget, bid strategy, placements, locations, and schedule.

One test lives on one platform. A Google Ads ad group and a Meta ad set do not share an auction,
an audience, or a definition of a click, so a difference between them is not a copy result. If the
user wants the same copy tested in two places, that is two tests with two reads, and the
cross-platform line is a separate observation, never the winner. If the user wants to change two
things, that is two tests run one after the other. Say so rather than blending them.

## Write the plan before the build
One row per variant, into the review sheet:
- Variant name, the real positioning name.
- Hypothesis in one sentence: what this copy claims, and what is true if it wins.
- The one variable under test.
- Platform and the exact metric name that platform uses for the primary read.
- Minimum clicks per variant.
- Minimum run in days.
- What would make the test invalid.

## Sample and duration
Set both numbers before the test starts and write them down. Defaults to propose, which the user
can change:
- At least 200 clicks per variant before any read, and 300 to 500 per variant when the budget
  allows, because a small click-through-rate difference needs volume to separate from noise.
- At least 14 days, so weekdays and weekends both appear and no single day decides the result.
- Stop at whichever comes later, not whichever comes first.
These are planning defaults, not a statistical guarantee. Say that once, plainly, and never
present a read as significance testing unless the user brings their own test.

## What the shell can and cannot measure
A cheapest-click strategy optimizes for clicks and does not split delivery evenly across variants.
Impression share and delivery will differ, so raw click counts are not a fair comparison.
- Compare click-through rate per variant, not clicks.
- Use the platform's own link-level metric where it has one, so that reactions, expansions, and
  profile taps are not counted as interest in the offer. Name the exact metric in the read.
- Report impressions, clicks, click-through rate, average cost per click, and spend per variant,
  each with its date range and its source, live interface or export.
- Conversions enter the read only when the user confirms conversion tracking exists and is firing.
  When it does not, say so and keep the read to click-through rate.
- This shell says nothing about lead quality, downstream conversion, or revenue. Say that in the
  read rather than letting a click-through-rate winner imply a business winner.

## What invalidates a read
Say these out loud when they apply rather than reporting through them:
- A variant restarted, was edited, or was rejected and re-approved mid-flight.
- The platform is still in an early delivery or learning period and spend per variant is uneven.
- The audience is small enough that the variants are competing for the same few people.
- Budget ran out on some days and not others.
- The final URL changed during the test.

## Reading a winner
1. Check both thresholds first. Under either one the answer is "not yet", with the numbers so far
   and the date the thresholds should be met.
2. Compare click-through rate per variant over the same window. State the spread in percentage
   points and as a relative difference.
3. Call a winner only when one variant leads on the primary metric across the whole window and is
   not carried by a single day. Show the daily or weekly split.
4. A gap under roughly 10 percent relative, at a few hundred clicks per variant, is a tie. Say "no
   winner" and say what would separate them, more volume, more time, or a bigger difference in the
   copy itself.
5. Write the read into the sheet next to the hypothesis, in one line, including what the losing
   copy tells you.

## After a read
Recommend the next test, one variable again, built from what the winner suggests. Recommend, never
enact. Pausing a losing variant or building the next test still goes through the review sheet, and
anything that spends still goes through the launch gate.

## Never
Read a winner before both thresholds are met. Compare variants across different windows, different
targeting, different platforms, or different final URLs. Present a click-through-rate difference as
a revenue result. Change the copy mid-test and keep reading the same test. Report a number that is
not on a screen I captured or in an export I named.
