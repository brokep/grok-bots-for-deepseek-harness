---
name: spend-watch
description: "Use when setting, changing, or running the spend and performance thresholds the user chose. Holds the rule model, the quiet floor, the budget pacing math, the fire path, the ping format, and the rearm rule. Produces a ping and a draft, never a change to an account."
---

# spend-watch

Part of the Marketing Analyst agent preset.

# Spend watch

A rule produces a check line and a ping. It never produces a change to an account.

## The model
A rule is five things: a **scope**, a **metric**, a **direction**, a **limit** in the user's own
units, and a **window**. Each rule also carries a **severity**.

- Scope: account, campaign, or ad set. One named entity or all of them.
- Metric: spend, CPA, ROAS, conversions, CTR, CPC, CPM, or frequency where the export has it.
- Direction: above or below.
- Limit: the number the user chose. Never a number this bot picked.
- Window: today, last 3 days, last 7 days, or month to date.
- Severity: urgent, watch, or note. Urgent pings on its own, watch and note batch into the next
  check.

Store one row per rule in /workspace/analytics/thresholds.md:

`<scope> | <name> | <metric> | <direction> | <limit> | <window> | <severity>`

## Quiet floor
A rule does not fire on an entity with fewer than 100 clicks, fewer than 5 conversions, or under
50 in the user's currency of spend in that window. The floor exists because a two click campaign
produces a headline CPA that means nothing. The user can change all three numbers. A suppressed
crossing is still written to the check file as suppressed, with the counts that suppressed it, so
nothing goes silently missing.

## Pacing math (only when a monthly budget or daily plan is on file)
- Daily plan is the monthly budget divided by the days in the month, unless the user saved a
  different daily plan.
- Month to date pace is spend month to date divided by days elapsed.
- Projected month is the month to date pace times the days in the month.
- Days of budget left is the budget remaining divided by the trailing 7 day daily rate.
- Report pacing as three numbers together: spent so far, projected, and the budget. Never report
  a percent without the two numbers under it.
- Without a budget on file, skip pacing and say it is skipped for that reason.

## Fire path
1. Read thresholds.md and ledger.csv. Re-read them every run, never rely on remembered values.
2. Run ingest-exports. The signed-in platforms are read live first, which is what makes a today
   or last 3 days window meaningful. If a platform's session has expired or its newest export is
   older than the window a rule needs, the rule does not fire. Say which platform and how stale
   the data is in one line, offer the sign in, and move on rather than firing on an old read.
3. Evaluate each rule in its window, after the quiet floor.
4. Write every crossing and every suppression to /workspace/analytics/checks/<date>.md with the
   numbers behind it, then append fired rules to /workspace/analytics/alerts.md.
5. Ping the user, one line per fired rule, in this format:

   `<scope name> | <rule name> | <metric> <direction> <limit>: <the number with its units> over
   <window> | live <platform> or export <file>, read <date> | <severity>`

6. Under each urgent ping add one line of diagnosis with the number behind it, and one question
   about what to do. Never an instruction, never an action.
7. Never fire the same rule twice for the same crossing. A rule rearms only after the entity comes
   back inside the limit for a full window, or the user says to rearm it.
8. Cap 5 pings per run. More becomes one line: "N more crossings, say show them."

## Never
Pause, enable, or edit a campaign, an ad set, a keyword, a bid, or a budget, inside a platform or
anywhere else, even when the signed-in account has admin access. Post an alert anywhere without a
saved destination and an explicit yes. Fire from a stale read without saying how stale. Fire from
a guess when a platform is signed out or an export is missing. Invent a cause for a crossing.
