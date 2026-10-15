---
name: ad-and-creative-analysis
description: "Use this when you need to know what a competitor is advertising and how their creative is working: hooks, offers, CTAs, formats, fatigue from run dates, the channel mix across networks, and the swipe file of ad screenshots organized by theme."
---

# ad-and-creative-analysis

Part of the Market Researcher agent preset.

# Ad and creative analysis

What a competitor pays to say is the least filtered thing they publish. This
skill turns their live ads into a swipe file and a read on their creative
strategy.

## When to use
Every weekly brief, on demand when the user asks what a competitor is running,
and for the Beat 4 first proof.

## Sources, in order
1. **Signed-in Google Ads** (only when signed in per connect-accounts, read
   only): auction insights for the account and the top campaigns. Capture the
   competitor domain list with impression share, overlap rate, position above
   rate, and top of page rate, and the date range. Screenshot the table. Diff
   against last run: who entered, who left, whose overlap grew.
2. **Public ad libraries**, no sign in needed: the Google Ads Transparency
   Center by advertiser name or domain, the Meta Ad Library by page name, and
   the LinkedIn ad library by company page. Screenshot the result page once for
   the count, then each creative.
3. **Export fallback** when neither is available, validated per
   connect-accounts. Never fill the gap with an estimate.

## Capture, per creative
Network, format (search text, static image, video, carousel), the **hook** (the
first line or first three seconds, in their exact words), the **offer** (free
trial, demo, discount, guarantee, tool, report, none), the **CTA** wording, the
proof used (number, logo, quote), first and last seen dates, and the landing
destination including the campaign parameters in the URL.

## The swipe file
Every creative screenshot goes to `<competitor>/swipe/<theme>/` under the
working root, filename `<first-seen-date>-<network>-<nn>.png`, where theme is
the message theme it belongs to in their words (for example "speed",
"migration", "priced per outcome"). Keep a `swipe/index.md` with one row per
creative: theme, hook, offer, CTA, network, first seen, last seen, landing page,
screenshot path. The swipe file is cumulative, it is never cleared, and it is
the artifact the user actually reuses. When it is attached in chat, attach a
grid composed by theme rather than 30 loose images.

## Creative fatigue, from dates alone
1. Run length per creative is last seen minus first seen. Sort by it.
2. A creative that has run longer than the competitor's median is a winner they
   are not tired of. A burst of new creatives inside two weeks with old ones
   going dark is a refresh, and it usually follows a message change.
3. Count new, still running, and retired since the last brief. Report the three
   numbers together, because only the shape of all three means anything.
4. Say what the dates support and nothing more. A long run is evidence a
   creative works for them. It is not evidence of spend, and spend is not public
   for commercial advertisers.

## Channel mix
1. Which networks carry live creatives, and how many in each. That ratio is the
   mix as far as anything public can show it.
2. Cross-check the tags on the competitor's own pages: a Meta pixel, a LinkedIn
   insight tag, a Google Ads conversion tag, a TikTok pixel, and any affiliate or
   partner script. A tag with no visible library creatives means they run there
   and the library does not cover that format, which is worth a line.
3. Note where they are absent. A competitor with no search ads on the category
   terms is making a choice, and it is usually the user's opening.
4. Write the mix to `<competitor>/channel-mix.md` with the date, and diff it
   every brief. A network appearing or disappearing is a bigger signal than a
   creative swap.

## Output
New creatives with screenshots and dates, retired ones, the hook and offer
rollup by theme, the three fatigue numbers, the channel mix and its diff,
auction movement when Google Ads is signed in, and one line on who the ad set is
talking to. Nothing if nothing changed.

## Never
Click a competitor ad. Fill a form on their landing page. Estimate a
competitor's spend, budget, or CPC. Change anything in a signed-in account.
Report a creative without its screenshot and its first-seen date.
