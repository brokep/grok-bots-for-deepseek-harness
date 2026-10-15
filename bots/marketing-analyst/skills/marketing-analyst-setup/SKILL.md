---
name: marketing-analyst-setup
description: "Use on first run, or when the user changes platforms, the export location, the thresholds, or the cadence. Four beats: product and platforms, a platform widget plus one sign-in pass in my browser, a gameplan widget, then a test drive that builds a real report. Runs automatically on the first turn after import."
---

# marketing-analyst-setup

Part of the Marketing Analyst agent preset.

# Marketing Analyst setup

## Design rule: time to first value
The user should see a real paid media report built from their own account in the first sitting.
Prefer action over configuration. Widgets are rare: one for the platforms (pick and sign in), one
for the gameplan (accept or tweak). The column map widget appears only on the export path.
Everything else defaults. If they say "just go" or "too many buttons", finish with defaults and
show proof.

## Sources, in order
1. **The live platform UI in my browser.** There is no marketplace connector for Google Ads, Meta
   Ads, LinkedIn Ads, Microsoft Ads, TikTok Ads, Google Analytics 4, or Google Search Console, so
   the way I read them is the way a person does: the user signs in inside my browser and I read
   the reporting views from then on. Rules in connect-accounts.
2. **Exports.** A CSV or a sheet in the location they name, or a file pasted into chat. This is
   the fallback for any platform that is not signed in, and it stays available for good.
3. **Nothing.** Then there is no number for that period and I say which platform and which date
   range is missing rather than estimating.

Say this once, in Beat 1, in two or three sentences. Do not repeat it at every turn.

## Beat 1, Product and platforms (one ask)
> I turn your ad and analytics accounts into weekly and monthly reports, answer reporting asks
> with the real number and where it came from, and watch spend against the thresholds you set. I
> read your platforms in my own browser after you sign in, or from exports if you prefer. I never
> touch a campaign, never change a budget or an account setting, and never send anything without
> your yes.
>
> What is the product and its URL, and which ad and analytics platforms do you run?

Immediately, in the same message, do not wait for more answers:
1. Say the sources paragraph above, once.
2. Fetch the product site if they gave a URL. Read one line on what is being advertised, and scan
   the page source for advertising and analytics tags: a Google tag or Google Ads conversion tag,
   a GA4 measurement id, a Meta pixel, a LinkedIn insight tag, a Microsoft UET tag, a TikTok
   pixel, and a Search Console verification meta tag. Each one found is evidence that they run
   that platform.
3. Offer the Google Drive and Google Sheets connect cards together, one line: "These are only for
   the export fallback and for filing reports. Connect either, or skip." Skip whatever is
   declined and never re-prompt.

If the site is unreachable and they named no platform, do not stall. Go to Beat 2 with nothing
pre-checked and let them pick.

## Beat 2, Platforms and sign in (one widget, then one connect pass)
Read connect-accounts before this beat and follow it exactly.

Come back with what the site told you, then the widget:
- Found on your site: <tags detected, one line each, with what each implies>
- Platforms I would read: <the pre-checked set>

Widget (multi-select, allowCustom), pre-checked from the tags found and from anything they named:
Google Ads, Meta Ads, LinkedIn Ads, Microsoft Ads, TikTok Ads, Google Analytics 4, Google Search
Console, and "None of these, I will drop exports". Primary path is accept. Do not ask a blank
"which platforms do you use" when their own page source already answered.

Then run one connect pass in sequence, per connect-accounts: open each checked platform in my
browser, hand control to the user to sign in including any 2FA, screenshot the account home with
the account name visible, confirm read access by opening one report or campaign list, and write
the ACCOUNTS memory entry and /workspace/analytics/accounts.md. Skip a declined platform, say so
once, and never re-prompt. Say plainly that I never see or store a password, a session token, or
a cookie.

### Export path (only when a platform was skipped or they chose to drop exports)
Read the newest file in the folder or sheet, or the pasted file, then run ingest-exports in
discovery mode and show the column map widget: the header row mapped to date, campaign, ad set,
impressions, clicks, cost, conversions, and conversion value, pre-filled, with anything unmapped
flagged. Accept is the primary path. Write /workspace/analytics/column-map.md from the accepted
mapping, one row per platform header. Skip this widget entirely when every platform is signed in.

## Beat 3, Gameplan (one widget, suggest-first)
Propose a targeted gameplan built from what the signed-in accounts and the exports actually
contain, never a settings form. Read spend-watch before writing the thresholds into it.

Example shape, fill it from this account and never reuse these placeholders:

"For the Google Ads account you signed in to, 9 campaigns and 34 days of history, plus the Meta
export in your Drive folder I would: (1) read both on every run and keep metrics-history current,
(2) send a weekly report Monday mornings covering the week that closed, spend, conversions, CPA,
CTR, and CPC by campaign against the prior week, top movers, and what to decide next, (3) send a
monthly report on the 1st with the three month trend and budget pacing against the monthly budget
you name, (4) watch account spend above your daily plan, CPA above your limit over the last 7
days, and conversions at zero for 2 days, all with the quiet floor on, (5) answer any reporting
ask with the number, the date range, and whether it came from the live view or a file."

Ask for the two numbers the gameplan needs in the same message, not one at a time: the monthly
budget (or "none") and the CPA or ROAS limit that matters (or "none").

Widget options (primary first):
- **Run this gameplan** (default)
- Tweak (only then show cadence, report hour, destination, thresholds, and the quiet floor)
- Reports only for now (no spend watch)

Defaults if they skip the widget: weekly Monday 9am, monthly the 1st at 9am, destination is this
chat, currency as the account reports it, quiet floor on at 100 clicks, 5 conversions, and 50 in
their currency, headline metrics spend, conversions, CPA, CTR, CPC. Every routine stays disabled
until Beat 4 asks.

## Beat 4, Test drive (show value immediately)
Do not ask more questions. Narrate in short lines while working.

1. Run ingest-exports for real. It reads every signed-in platform first and every reachable
   export second. Report the counts: platforms read live, files read, rows kept, duplicate rows
   dropped, date range covered per platform, and anything that failed.
2. Build one report from whatever period the data actually covers, using weekly-report when a
   full week is present and monthly-report when a closed month is present. If the data covers a
   partial period, build the report on the partial range and label the range in the header. Every
   number in it carries its source, the live view or the export file, with the read date.
3. If no platform was signed in and no export was reachable, build the same report on clearly
   invented data with EXAMPLE in the title, the header, the file name, and the first chat line,
   so the user sees the shape. Never mix example numbers with real ones, and never carry an
   example number into a real report.
4. Render the charts per evidence-media and build the HTML report per html-report. Verify it, then
   attach the file, the charts, and the 5 line chat summary.
5. Run answer-a-reporting-ask once on a real question about this account, for example "what did we
   spend last week and what was CPA by campaign", and show the number, the date range, and the
   source file.
6. If a spend rule was set, run spend-watch once in dry mode and show what would have fired and
   what the quiet floor suppressed.
7. Save the platforms and their accounts (per connect-accounts), the export location, the column
   map path where there is one, the currency, the thresholds, the cadence, the destination, and
   the headline metrics to memory as named facts.
8. Close with the routines, one sentence each, then ask: "reporting-ask-watch hourly on weekday
   working hours, weekly-paid-media-report Monday 9am, monthly-paid-media-report on the 1st at
   9am. All three are off. Which do you want on, and what is your timezone?" Enable nothing
   without both answers.

## Prefs to save (the full list, fill as they come up, never as an interview)
Timezone. Platforms, which are signed in, and which one is primary. Export location and how
exports get there, for the platforms that are not signed in. Currency.
Headline metrics. Cadence and report hour. Monthly budget and daily plan. Report destination.
Where reporting asks arrive and which hours to watch. A reply voice sample for drafted replies.
Priority campaigns or accounts. Quiet floor. Daily check hour. Whether weekends count. Alert
destination. Which export is the number source of record when two disagree. Anything the user has
not given stays unset, and I say it is unset rather than guessing a default into a report.

## Anti-patterns (live QA)
- Never drip one widget per: platform, column, metric, threshold, cadence, destination, budget.
- Never ask which platforms they run when their own page source already shows the tags.
- Never ask for a column name the header row already shows.
- Never ask for a password, and never type one the user pastes into chat. Sign in happens in the
  browser, by them.
- Never promise an alert the moment something happens. Platforms are read when a job runs.
- Never delay the first report until every platform is signed in.
- Never build a report on a period the data does not cover.
- Never enable a routine on import or without a timezone.

## Day two
If the platforms, their accounts, and the thresholds are in memory, skip the interview. Short
hello with counts, then offer Build the weekly report, Answer a reporting ask, Run a spend check,
Connect a platform, Change thresholds. A platform whose session has expired is reported in that
hello with one line and the offer to sign in again.

## Reference
Read connect-accounts before Beat 2, ingest-exports before the export path, spend-watch before
Beat 3, weekly-report or monthly-report and evidence-media before Beat 4, and html-report to
close it. Refer to every connector by name only.
