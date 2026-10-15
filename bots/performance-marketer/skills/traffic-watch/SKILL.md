---
name: traffic-watch
description: "Use at 24 hours and 72 hours after a campaign is enabled, on the spend checkpoint date, when the daily routine fires, or when the user asks how it is doing. Reads spend and per variant metrics from the signed-in interface with screenshots, and pauses on the stop word or the cap."
---

# traffic-watch

Part of the Performance Marketer agent preset.

# Traffic watch

Once something is live, the job is a short honest read and a fast stop.

## When to use
At 24 hours and at 72 hours after a campaign is enabled, when the daily routine fires, on the
spend checkpoint date, and whenever the user asks how it is doing.

## Quiet by default
If nothing is enabled, say nothing. No digest, no "still paused" note, no summary of the last
test. The one exception is the spend checkpoint date, which is reported even when the answer is
that the campaign was already paused.

## The read
1. Open the campaign in the signed-in platform interface. If the session is dead, follow the
   session expiry path in connect-accounts: say it, ask once for a fresh sign in, offer the export
   path in the same message, and do not retry anything. If the user sends an export instead, use
   it and put its export date on every number.
2. Screenshot the campaign row with the status and spend columns, and the variant table with
   impressions, clicks, click-through rate, average cost per click, and cost. Those screenshots
   are the numbers. The text repeats them, it does not replace them.
3. Name the metric exactly as the platform names it, and use the link-level click metric where the
   platform has one, so that interactions with the post rather than the offer are not counted.
   Never rename a platform's metric into another platform's word for it.
4. Report in this order and nothing more:
   - Source: live interface or export, with the date.
   - Status and spend: what is live, spend since enable, spend against the daily budget, spend
     against the total cap, and days left at the current rate.
   - Per variant: impressions, clicks, click-through rate, average cost per click, cost. The same
     window for every variant.
   - Against the plan: clicks per variant versus the minimum, days elapsed versus the minimum, and
     whether a read is possible yet. At 24 hours it usually is not, and saying so is the correct
     answer.
   - Anything broken: rejected or limited ads, limited by budget, a final URL that stopped
     loading, zero impressions on a variant, a policy notice, an uneven delivery split. Each with
     its screenshot.
   - One line of what I would do next, as a recommendation, never as an action taken.
5. At 72 hours add the first directional read per messaging-test-design, labeled directional and
   not a winner unless both thresholds are already met.

## Spend checkpoint
On the checkpoint date, compare spend to the total cap. Under the cap, report the number and the
projected date it would be reached. At or over the cap, pause the campaign immediately, screenshot
the paused state, and report it in the same turn.

## Stop word
Any stop word from the user, the one agreed at the launch gate or an unmistakable stop, pause, or
kill in plain language, pauses every live campaign in this test on that turn, on every platform it
runs on. Pause first, report second, with the screenshot of the paused status. Never ask for
confirmation before pausing.

## Never
Enable, re-enable, raise a budget, change a bid strategy, edit copy, or change targeting during a
watch. Report a number I did not see on a screen this run or read in an export I named. Fill a gap
in the data with an estimate. Stay quiet about a rejection, a broken URL, or a dead session
because the rest of the run looks fine.
