---
name: outstanding-asks-review
description: "Scan Slack, Gmail, and Notion for open asks that still need the user, then deliver a prioritized digest."
---

# Outstanding asks review

Part of the WTD agent preset.

---
name: Outstanding asks review
description: >-
  Scan Slack, Gmail, and Notion for open asks that still need the user, then
  deliver a prioritized digest.
---
# Outstanding asks review

## Goal
Produce a short, prioritized digest of outstanding asks across Slack, Gmail, and Notion so the user can clear blockers without digging through every channel.

## Scope defaults
- Lookback: last 7 days for a weekday morning digest (use last 14 days after OOO or when the user asks for catch-up).
- Channels: Slack (mentions, DMs, threads), Gmail (unread/important needs-reply), Notion (open tasks assigned to the user, hospitality plan pages, recent meeting action items).
- Prefer VIP hospitality and field / revenue marketing items when ranking.

## Steps
1. Confirm identity (Slack profile / Notion self) if not already known.
2. Slack (read-only): search mentions and DMs for open asks; open promising threads to check whether the user already replied or the ask was closed.
3. Gmail (read-only): search unread/important and ask-like threads; skip promotions/newsletters.
4. Notion (read-only): search and query task DBs / hospitality pages / recent meeting notes for open items assigned to the user.
5. Deduplicate and rank: High = waiting on user / time-sensitive / VIP; Medium = clear ask, softer deadline; Low = FYI or likely already handled.
6. Deliver a tight digest in chat: channel, who, one-line ask, urgency, link when available. Cap at ~15 items unless the user wants more.
7. Offer to draft replies or knock out the top items next — do not send anything without confirmation.

## Standing use
When run on a schedule, stay quiet if there is nothing new or actionable. Only ping when there are real outstanding asks.
