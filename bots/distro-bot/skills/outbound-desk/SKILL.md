---
name: outbound-desk
description: "Use for lead lists, outbound drafts and sends, replies, and hand-offs to sales."
---

# outbound-desk

Part of the Distro Bot agent preset.

# outbound-desk

Outbound until a lead replies, then the lead goes to sales.

## Leads

From a list or sheet the user gives, a lead tool through SearchPlugins, or people engaging with the user's topics in public. distro.py lead import <csv> --source <where>, or lead add, dedupes and skips do-not-contact and broken addresses. Draft only for leads that fit the audience in distro.py status.

## Sequence

First touch: why them, the problem in one line, one proof, one ask, and a plain opt-out line, under 90 words in the user's voice. Each follow-up adds something new. distro.py lead due lists who is due, spaced by the script, up to steps touches.
Drafts go in the user's inbox (distro.py lead drafted <email>). Send only a batch the user approves, read back as count and recipients: send each, then distro.py lead sent <email>, which stops at send_cap. No inbox: copy-ready text, logged as sent when the user says so.

## Replies (Outbound replies, or when asked)

Read the inbox for replies from leads in distro.py leads (auto-replies don't count). Interested or asking: distro.py lead reply <email> --said "<their words>" stops the sequence and prints the hand-off. Send it to the sales teammate with SendToAgent, priority true, then distro.py lead handed <email> --to sales. No sales teammate: show it to the user with a suggested reply, then --to user. A no, opt-out, or bounce: distro.py lead stop <email> --why <no|optout|bounce>.

## Numbers

distro.py lead stats: reply, opt-out, and bounce rates by source and touch, for the weekly review and the playbook.
