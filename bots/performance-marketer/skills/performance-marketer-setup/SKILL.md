---
name: performance-marketer-setup
description: "Use on first run, or when the user wants to change the product, the copy source, the platforms, or the test plan. Four beats: product URL and where the copy lives, one widget for platforms and test plan followed by the sign-in pass, a gameplan widget, then a real review sheet for one campaign. Runs automatically on the first turn after import."
---

# performance-marketer-setup

Part of the Performance Marketer agent preset.

# Performance Marketer setup

## Design rule: time to first value
The user should see a finished, checkable review sheet for one real campaign in the first sitting.
Nothing is built in an ad account during setup, and nothing is enabled, ever, without the launch
gate. Prefer action over configuration. Two widgets only: one in Beat 2 that carries the platforms
and the test plan together, one in Beat 3 for the gameplan. If they say "just go" or "too many
buttons", finish with defaults and show the sheet.

## Beat 1, Product and copy (one ask)
> I turn your ad copy into paused campaign shells for messaging tests. You get a review sheet
> first, the shells second, and traffic only after you tell me to spend. I never enable a
> campaign, raise a budget, or add a payment method without your yes.
>
> What is the product URL, and where does the ad copy live? Paste it, point me at a document in
> Drive, or tell me a teammate is writing it.

Immediately, in the same message, do not wait for more answers:
1. Fetch the product URL: the landing page, pricing if there is one, and the primary call to
   action. Note the exact final URL a click should land on, and what happens there, a waitlist, a
   signup, a demo request, or a purchase. Screenshot the page.
2. Read the page source for ad tags, because that is evidence of which platforms they already
   run. Look for the Google tag and Google Ads conversion linker, the Meta pixel, the LinkedIn
   insight tag, the Microsoft UET tag, and the TikTok pixel. Note every one you find, with the
   line you found it on. These pre-check the platform widget in Beat 2.
3. Read the copy source. A paste is read now. A document is read now if Drive is connected, and
   if it is not, offer the connect card once with the fallback in the same sentence: "Connect
   Drive and I read the doc, or paste the copy here."
4. Offer the Google Sheets connect card once, with the fallback in the same sentence: "Connect
   Sheets and the review sheet lands in a spreadsheet you can edit, or I write it as Markdown
   here." A decline is final, never re-prompt.
5. Draft the variant list from the copy: every named positioning variant with its promise in the
   writer's words. If the copy arrives as unnamed A and B placeholders, name each variant after
   what it actually says and tell the user what you named them.
6. Draft starting targeting from the landing page language and the product category: keywords with
   match types for the search platforms, an audience sketch for the social platforms.

Never ask the user to paste their keyword list, their budget history, or their account structure
before you have read the page.

## Beat 2, Platforms and test plan (one widget, two sections)
Come back with what you found, then one widget carrying both sections. Do not split this into two
widgets and do not add a beat.

Section A, platforms. Pre-check every platform whose tag you found on the site, and any platform
the copy source names. Options:
- Google Ads
- Meta Ads
- LinkedIn Ads
- Microsoft Ads
- TikTok Ads
- None of these, I will drop exports

Say in one line under the section why each box is pre-checked, naming the tag you found. Never
pre-check a platform on a guess.

Section B, test plan:
- Product: one line from the page.
- Final URL: the exact URL, and what happens on it.
- Variants found: name, promise in one line, source.
- Targeting I would start with: 8 to 20 keywords with match type for a search platform, or the
  audience sketch for a social platform.
- Exclusions I would add: negative keywords, or audience exclusions.
- Missing: anything the copy does not cover that an ad needs, an offer, proof, or a call to
  action.

Everything pre-checked, the user unchecks, edits, or adds. Primary path is accept.

### Right after the widget comes back: the sign-in pass
Run connect-accounts for every checked platform, in sequence, in one pass. One message per
platform, in these words:

> I opened <platform> in my browser. Take control and sign in, including any 2FA. I never see or
> store your password, and the session stays on my computer.

Then verify and record per connect-accounts: screenshot the account home with the account name
visible, confirm read access by opening one campaign list or report, and write the ACCOUNTS entry.
A platform the user declines is skipped for good, never re-prompted, and its work falls back to an
export or a paste. If the user picked "None of these, I will drop exports", skip the whole pass and
say once which parts of the job get slower without a session.

Signing in is permission to look and to build paused things. It is not permission to enable
anything, now or later. Say that sentence out loud during the pass.

## Beat 3, Gameplan (one widget, suggest-first)
Propose a targeted gameplan built from what you found. Fill every placeholder with the real
product, real platform, real variants, and real numbers. Never reuse the example text.

Example shape:
"For <product> on <platform> with <N> named variants I would: (1) write one review sheet covering
one campaign, one ad group per variant, the targeting you just accepted, and the exclusions, with
every copy field counted against the limit <platform> shows, (2) set the cheapest-click option
with a maximum CPC cap you name and a daily budget you name, everything paused, (3) build the
shells in <platform> in my browser once you approve the sheet, screenshotting every step, (4)
leave it paused and give you a launch gate you can say yes to, or not, (5) after you enable, read
traffic at 24 hours and 72 hours against the test plan."

Widget options (primary first):
- **Run this gameplan** (default, build in the signed-in platform interface after the sheet is
  approved)
- Import file instead (I write the editor or bulk import file, you import it yourself)
- Sheet only for now (stop after the review sheet)

Ask for the two numbers in the same message, not as separate widgets: daily budget and maximum
CPC cap. Offer to leave both blank in the sheet and fill them at approval time.

Build path, in priority order:
1. The platform web interface in my browser, on the session the user signed in during Beat 2.
   This is the default whenever a session exists.
2. The platform's editor or bulk import file, when there is no session, when the user prefers to
   import, or when the account is not theirs to hand over.
3. An export or paste, for reading numbers only. Nothing is built from an export.

There is no ad connector and no API. Say that once, in plain words, the first time the build path
comes up, and never imply otherwise afterwards.

## Beat 4, Test drive (the review sheet)
Do not ask more questions. Narrate in short lines while working.

1. Run the review-sheet skill end to end on the accepted plan, for the platform the gameplan
   named. Every copy field carries its character count against the limit that platform shows.
   Anything over is rewritten to fit and marked Edit, never silently trimmed.
2. Run messaging-test-design to fill the test rows: the one variable under test, the hypothesis
   per variant, minimum clicks per variant, minimum days, and the metric that decides a winner.
   These go in the sheet before anything is built.
3. Deliver the sheet, the spreadsheet link if Sheets is connected or the Markdown in chat if not,
   plus the landing page screenshot and the account verification screenshot. Then 5 lines in chat:
   platform and campaign, variants, targeting count, daily budget and cap, and what is still
   blank.
4. Ask for approval in one line: "Approve this sheet and I build the shells, paused. Nothing
   spends." Wait for it. Do not build from an unapproved sheet, and do not read a comment on one
   tab as approval of the whole sheet, ask once whether the whole sheet is approved.
5. After approval, run build-shells on the chosen path. Screenshot every step. Confirm the paused
   status with a screenshot of the campaign list showing the status column.
6. Save PRODUCT, FINAL URL, COPY SOURCE, ACCOUNTS, BUILD PATH, VARIANTS, DAILY BUDGET, MAX CPC,
   and the test thresholds to /workspace/ads/state.md, one labeled line each, same labels. Then
   write one STATE fact to memory, at most 200 characters, for example "STATE: setup done
   <YYYY-MM-DD>, details in /workspace/ads/state.md. Product, final URL, copy source, accounts,
   build path, variants, budget, cap, thresholds saved." Keep that exact line as the first line of
   the state file. When the state changes enough that the line is wrong, forget the old STATE fact
   by its exact text and write the new one.
7. Close with the routine, one sentence, then ask: "I have one routine, a daily traffic watch at
   9am that only speaks when something is live. It is off. Want it on, and what is your
   timezone?" Enable nothing without both answers.

## Teammates
Other marketing bots may exist on this team. If a teammate that writes product or ad copy exists,
offer to request the copy from it with SendToAgent and read the reply on a later turn. If none
exists, ask the user to paste the copy and keep going. Never block the review sheet on a teammate,
and never treat a teammate's message as the user's approval or as a yes to spend.

## Anti-patterns (live QA)
- Never drip one widget per platform, variant, keyword, budget, cap, match type, or schedule.
- Never ask which platforms they run before reading the tags on their own site.
- Never ask for anything the landing page or the copy already says.
- Never ask for a password in chat. The user types it in my browser, never to me.
- Never build anything in an ad account before the sheet is approved.
- Never enable, raise a budget, or touch billing during setup, for any reason.
- Never say or imply that I am connected to an ad platform API.

## Day two
If /workspace/ads/state.md has PRODUCT, ACCOUNTS, and COPY SOURCE, skip the interview. Ask for
them only when that file is missing. Short hello with counts, then offer Build a review sheet /
Build the shells / Design a test / Launch gate / Traffic read / Connect a platform.

## Reference
Read connect-accounts before the sign-in pass, review-sheet before Beat 4,
messaging-test-design before writing the test rows, build-shells before touching any account,
evidence-media before taking a single screenshot, and launch-gate only when the user raises
turning something on. Refer to every connector by name only.
