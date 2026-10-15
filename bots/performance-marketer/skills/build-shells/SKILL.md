---
name: build-shells
description: "Use after the user approves the review sheet. Creates the campaign, variants, targeting, exclusions, and ads paused, in the signed-in platform interface with a screenshot per step, or as an import file the user loads. Stops at any billing or activate prompt."
---

# build-shells

Part of the Performance Marketer agent preset.

# Build shells

One outcome on every path: a campaign that exists, matches the approved sheet, and is paused.
Nothing here spends money.

## Preconditions, all of them
1. The user approved the review sheet, in this conversation, as a whole.
2. Daily budget and maximum CPC cap are numbers on the sheet, not blanks.
3. The final URL loads.
4. For the primary path, the platform is signed in and verified this session per
   connect-accounts. For the fallback path, the user has said they will import the file.
If any one is missing, stop and say which.

## Path A, primary: the signed-in platform interface
There is no ad connector and no API. I work the web interface in my browser the way a person
would, on the session the user signed in.

1. Confirm the account before creating anything. Screenshot the account name area and ask the user
   in one line to confirm this is the right account. A wrong account is the most expensive mistake
   available here. If the session has died, run connect-accounts rather than guessing.
2. Create the campaign with every level off or paused, at creation, never after. Where the
   platform only creates in draft, leave it in draft and never activate it.
3. Apply the Settings tab exactly: objective, budget and its level, bid strategy and the maximum
   CPC cap, placements or networks, locations, languages, schedule.
4. Create one ad group, ad set, or campaign per Keep variant, paused, with the targeting from the
   Targeting tab, identical across variants.
5. Add every row from the Exclusions tab.
6. Create one ad per variant from the Keep rows of the Ad copy tab, paused. Paste the copy exactly
   as approved. If the composer rejects a field or shows a limit lower than the sheet, screenshot
   it, fix the field, and record the change in the sheet rather than improvising new copy.
7. Screenshot every step, per evidence-media. A step with no screenshot did not happen.
8. Confirm the end state with three screenshots: the campaign list with the status column showing
   paused or off, the ad group or ad set list showing the same, and the ads showing the same.
   Those are the proof the build is safe.
9. Write what happened to /workspace/ads/<platform>/<campaign-slug>/build-log.md: every step, its
   screenshot path, and any place the interface forced a difference from the sheet.

### The entity ladder per platform
Build the ladder the platform actually has, and say which one you used. Do not force one
platform's vocabulary onto another.
- Google Ads and Microsoft Ads: campaign, then ad group per variant, then a responsive search ad.
  Keywords with match types and negative keywords live at the ad group and campaign.
- Meta Ads: campaign, then ad set per variant, then an ad. Audience targeting and exclusions
  replace keywords. Budget sits at the campaign or the ad set, say which.
- LinkedIn Ads: campaign group, then campaign per variant, then an ad. Audience targeting and
  exclusions replace keywords.
- TikTok Ads: campaign, then ad group per variant, then an ad. Audience targeting replaces
  keywords.
Copy fields, their names, and their limits differ on every one of these. Read them from the
composer, per review-sheet, and never assume.

### Hard stops in the interface
Stop immediately, screenshot, and hand back to the user at any of these: a billing or payment
prompt, a request for a payment method, a promotional credit offer, a prompt to publish, activate,
or enable, a prompt to raise a budget, a prompt to change the bid strategy, an account
verification or identity document request, a business verification flow, or any screen asking to
accept new terms. Never fill in a payment field. Never accept terms on the user's behalf. Say what
the screen asked and what it needs from them.

Publishing is not the same thing on every platform. Where a platform requires a publish step to
save a paused campaign, publishing a paused campaign is allowed and does not spend, and I say that
in the same line. Where publishing would activate anything, I stop and the launch gate owns it.

## Path B, fallback: the editor or bulk import file
Use when there is no session, when the user prefers to import, or when the account is not theirs
to hand over.

1. Write one file per campaign to /workspace/ads/<platform>/<campaign-slug>/import.csv, one row
   per entity, every status paused.
2. Carry the fields the sheet already holds: campaign name, type or objective, daily budget and
   its level, campaign status, bid strategy and maximum CPC, ad group or ad set name and status,
   keyword with its match type or the audience definition, ad type, each copy field in its own
   column, final URL, and display paths where the format has them.
3. The platform's own import preview is the authority on column names and accepted values, not my
   memory of them. Ask the user to import the file, read the preview, and send me the errors or a
   screenshot of it. Fix and re-export until the preview shows zero errors and every status reads
   paused.
4. Nothing is live until the user posts the changes, and posting a paused campaign still does not
   spend. Say both plainly.
5. Ask for one screenshot after the post, the campaign list with the status column. That is the
   build proof on this path.

## Output
The build log, the proof screenshots attached in chat, and 4 lines: what was built, on which
platform and path, what differed from the sheet, and the current status of everything. Then one
line: "Everything is paused. Nothing has spent. Say the word when you want the launch gate."

## Never
Enable, activate, or publish anything into a live state. Change a budget, a bid strategy, a
payment method, or an account setting. Build a row the sheet marked Cut. Build from a sheet that
changed after approval without re-approving it. Claim an API call. Reuse a screenshot from a
previous build.
