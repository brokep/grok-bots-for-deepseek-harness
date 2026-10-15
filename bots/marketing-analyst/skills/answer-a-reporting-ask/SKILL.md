---
name: answer-a-reporting-ask
description: "Use when someone asks a paid media question in chat or by email. Turns the question into a query over the live platform views and the exports, and answers with the number, the date range, where it came from, and a chart or table. Drafts the email reply and never sends it."
---

# answer-a-reporting-ask

Part of the Marketing Analyst agent preset.

# Answer a reporting ask

A reporting ask is any question whose answer is a number the platforms or the exports already
hold. The answer is the number, the date range, where it came from, and a chart or table.
Nothing else.

## When to use
When the user asks a paid media question in chat, and when reporting-ask-watch finds one in the
mailbox the user named.

## Steps
1. Restate the ask as a query in one line: metric, scope (account, platform, campaign, ad set),
   and date range. Where the ask is vague, take the narrowest reasonable reading and say which
   reading you took, rather than asking a clarifying question first. "How did last week go"
   becomes spend, conversions, CPA, CTR, and CPC for the account, last full week, against the
   week before.
2. Run ingest-exports so the answer is built on current data. It reads the signed-in platforms
   live first, then the exports. For a question about today or yesterday, the live view is the
   only source that can answer it, so sign in first if the platform is stale.
3. Check coverage before computing. If neither a live view nor an export covers the range, do not
   answer. Name the platform, say whether a sign in or an export would close it, give the exact
   date range needed, and offer a two line holding reply the user can send: what is known, and
   when the number will exist.
4. Query metrics-history.csv, or the ledger when the range does not line up with a stored period.
   Use the formulas in ingest-exports and nothing else.
5. Build the evidence: a table when the answer is more than one row, a chart when the answer is a
   trend or a comparison, plus the screenshot of the platform view when the number came from a
   live read, per evidence-media. Attach it, never describe it.
6. Answer in this shape:
   - The number, in the user's currency, with its unit.
   - The date range it covers.
   - The source, `live <platform> <view> <read date>` or `export <file> <ingest date>`, and mixed
     with the split when the range used both.
   - The table or chart.
   - One line of what it means, with a second number behind it.
   - A Could not read line when part of the range, a platform, or a session was missing.
7. Log the ask in /workspace/analytics/asks.md: date, who asked, where, the ask in their words,
   the answer given, the source, and the draft status.

## When the ask arrives by email
Draft the reply, do not send it. Match the reply voice sample saved in memory when there is one,
otherwise plain and short. Put the number in the first sentence. Save the draft in the mail
drafts folder when Gmail is connected, show it in full in chat, and end with one line: "Draft
only. Say send and I send it, or copy it out."

## Never
Guess a number to be helpful. Answer from a previous report instead of the source. Round in a
way that changes the decision. Quote a metric the platform or the export does not contain. Give
a number without saying where it came from. Send, reply, or post without an explicit yes in that
conversation.
