---
name: strategy-read
description: "Use this when the monthly routine fires, or when the user asks where the market is going or whether to change course. Rolls the weekly briefs and the month's real numbers into patterns and ranks 2 to 4 marketing moves as adjust or pivot."
---

# strategy-read

Part of the Market Researcher agent preset.

# Strategy read

The monthly step up from what moved to what to do about it.

## When to use
The monthly routine, or when the user asks where the market is going or whether
to change course.

## Inputs
Every weekly brief since the last read, the swipe files, the promotion
calendars, the matrix history, the search overlap tables, the baseline, and the
ACCOUNTS entries. With fewer than two weeks of history, say so and give a first
read from whatever snapshots exist.

## Steps
1. The month's real numbers first, live UI where signed in, export otherwise,
   nothing at all where neither exists:
   - Search Console: clicks, impressions, average position this month against
     last, and the 10 queries that moved most each way.
   - GA4: sessions and conversions by channel this month against last, and the
     landing pages that gained or lost.
   - Google Ads: impression share, overlap rate, and the auction competitor set
     this month against last.
   Screenshot each view and label every figure with its source and date range.
   With nothing signed in, run the read on public evidence alone and name it as
   the weaker read.
2. **Where the market moved**, 3 to 5 lines. Each is a pattern across
   competitors, not one event, and a pattern needs two pieces of dated evidence.
   The shapes that recur: several competitors converging on one hook, offers
   moving the same direction (trials lengthening, cards appearing, freemium
   opening or closing), a channel filling up or emptying out, a category term
   being abandoned, a new domain climbing the auction list two months running.
3. **Where we are exposed**: read the baseline and the month's numbers against
   those patterns. Name the specific claim, offer, page, term, or channel that
   is now weaker, with the number and the evidence behind it. A pattern that
   cost real clicks outranks one that did not.
4. **Moves**, 2 to 4, each marked **adjust** or **pivot**, all of them
   marketing:
   - Adjust: a change inside the current positioning. A message, an offer, a
     page, a creative angle, a channel weight, a term to defend.
   - Pivot: a change to who the marketing talks to or what it claims. Only when
     the evidence is a pattern across at least two competitors or two months,
     and say plainly that it is the expensive option.
   - Every move carries the evidence, the cost to make it, the fastest test of
     it, and the signal that would say it was wrong. Where a real number exists,
     that killing signal is a number.
   - Never a product move, a roadmap item, or a feature request. If the honest
     answer is that the product itself is behind, say that in one line as
     context and keep the moves on marketing.
5. **What did not change**: one line, so a quiet month does not read as a
   crisis.

## Output
One page in chat plus the report from capture-and-report. Ranked moves with the
evidence under each. Recommendation only. The user decides and nothing here is
executed.

## Handoffs
If a move needs copy, a page change, an ad, or a report, produce the brief for
it and offer it to a teammate that does that job if one exists. Otherwise hand
it to the user. A spend, a publish, or a send is always the user's explicit yes.

## Never
Propose a pivot on one data point. Present an inference as a fact. Blend a live
number and an exported number without saying so. Recommend a budget number.
