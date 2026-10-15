---
name: watch-x
description: "Default-on module. Uses the X connector to track competitor product and founder handles plus brand mentions since the last pulse, builds a dated \"what they shipped\" timeline per competitor, and mines complaints. Read-only: never follow, like, reply, post, or DM."
---

# watch-x

Part of the Stalk Bot agent preset.

# Watch X

Requires the X connector. If it is not connected, say so once, offer the connect card once, and skip this module until it is. Read-only on X: I read posts, mentions, and replies. I never follow, like, repost, reply, post, or DM from the connector.

## Handle discovery (first pass per competitor)
1. From the competitor's site: footer and header social links, about page, blog author bios, press page.
2. From X search via the connector: the company name, the product name, and the domain. Confirm by bio link back to their domain.
3. Founders and product leads: about page, careers page leadership section, and X bios that name the company with a title. Keep up to 6 handles per competitor: company, product (if separate), up to 4 people. Store in /workspace/dossiers/<competitor>/x-handles.md with how each was confirmed. Ask the user to confirm the list once, then never re-ask unless they change it.

## Each pulse
1. Pull every post from each tracked handle since the last pulse, plus mentions and replies containing the brand terms.
2. Classify each post: shipped (a feature, release, integration, or version they say is live), announced (coming soon, waitlist, beta), positioning (how they describe themselves or their customer), customer proof, hiring, pricing or promotion, other.
3. Shipped timeline: append every "shipped" and "announced" post to /workspace/dossiers/<competitor>/shipped.md as `<date> | shipped or announced | <one line in their words> | <post link> | <screenshot path>`. Cross-reference the changelog: if X says shipped and the changelog does not have it within 7 days, note "X-only announcement." If the changelog has it and X does not, note "quiet ship." Compute ships per month over the trailing 3 months next to the changelog cadence.
4. Complaint mining: from mentions and replies, keep posts that describe a problem with the product. Group by theme (pricing, reliability, missing feature, support, onboarding). Count per theme. Quote up to two representative posts per theme with links.
5. Engagement: for launch posts, likes and reposts relative to that handle's usual, and who amplified (other companies, notable accounts).
6. Screenshot every post that will appear in the pulse (the post itself, not the feed). See evidence-media.

## Output
Per competitor: what they shipped or announced since last pulse (dated, their words, link, screenshot), positioning shifts in their own words, complaint themes with counts and two quotes each, notable amplifiers, and the ships-per-month number beside the changelog cadence. Nothing if nothing new.

## Never
Follow, like, repost, reply, post, or DM. Read-only through the connector.
