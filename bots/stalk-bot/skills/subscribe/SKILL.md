---
name: subscribe
description: "Use to get a competitor's research identity onto their newsletter, blog updates, product updates, and waitlists."
---

# subscribe

Part of the Stalk Bot agent preset.

# Subscribe

## Inputs
Competitor, research identity, optional list of specific signups.

## Steps
1. Find every subscription surface on their site: newsletter form, blog subscribe, product updates, changelog RSS or email, waitlists, webinar lists. Also check the footer and the docs site.
2. For each: submit the research identity on my browser. If a form needs a name, use the research alias. If it needs a company, use "<Company> Research".
3. Check the identity's inbox for confirmation emails on this turn and again on the next pulse (do not block waiting). If a teammate identity bot holds the inbox, send AUTH REQUEST need: code. Click confirm links when mail arrives, confirmations are allowed; never reply to marketing.
4. Record in /workspace/dossiers/<competitor>/subscriptions.md: source, date, confirmed yes/no.
5. Report one line per subscription.

## Never
Subscribe the user's personal address. Reply to a welcome email. Sign up for a paid list.
