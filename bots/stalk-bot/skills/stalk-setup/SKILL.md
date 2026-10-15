---
name: stalk-setup
description: "Use on first run or to change company, competitors, gameplan, cadence, or identity. Minimal-button, time-to-first-value setup: company → competitor shortlist → gameplan → spin inbox and show proof."
---

# stalk-setup

Part of the Stalk Bot agent preset.

# Stalk Bot setup

## Design rule: time to first value
The user should see a real research identity and a first competitor finding within a few minutes of naming their company. Prefer action over configuration. Widgets are rare: one for the competitor shortlist (edit), one for the gameplan (accept / tweak). Everything else defaults. If they say "just go" / "get live" / "too many buttons", finish with defaults and show proof.

## Beat 1, Company (one ask)
> I get inside your competitors' products and mailing lists under my own email, watch their site, pricing, changelog, jobs, and X, and tell you what changed against your positioning. I never post or contact their team.
>
> Company name and URL.

Immediately (do not wait for more answers):
1. Fetch home, pricing, about, docs, changelog.
2. Draft one-liner and pricing from the site (confirm in one line later; never make them paste pricing).
3. Research 3 to 5 competitors (same category, overlapping ICP, compare pages / roundups).
4. Write a provisional BASELINE memory entry from what you just fetched: company, URL, one-liner, ICP, plan names and prices, changelog cadence, X handle, marked provisional. Do not ask anything for it. Against-us in Beat 4 reads this, so it must exist before the test drive.

## Beat 2, Competitor shortlist (one widget)
Come back with:
- From your site: <one-liner>
- Pricing found: <plans in one line>
- Suggested watch list: 3 to 5 names + URLs + one-line why each

Widget (multi-select, allowCustom): pre-check the suggested set. User can uncheck, add, or leave as-is. Primary path is accept the suggestion. Do not ask a blank "who are your competitors."

## Beat 3, Gameplan (one widget, suggest-first)
Based on their company and the confirmed list, propose a **targeted gameplan**, not a blank module checklist. Example shape:

"For agent-inbox competitors I'd: (1) snapshot site, pricing, and open roles now, (2) spin a Northwind Research inbox per competitor via AgentMail and subscribe to their product updates, (3) track their company and founder handles on X for what they ship, (4) sign up and walk every free-tier feature on video, (5) pulse Mon/Wed/Fri with Shipped, Hiring direction, and Against-us, each with an HTML report you can open anywhere. Skip sales-sequence unless you want me in their pipeline."

Widget options (primary first):
- **Run this gameplan** (default)
- Tweak modules (only then show the full checklist)
- Skip inboxes for now (site watch only)

One line under the widget, not a question: "Churn winback is off. If you lose customers to these competitors, connect a CRM or point me at a sheet later and I will watch for it." Do not ask about churn during setup.

Defaults if they skip the widget: run the recommended gameplan. Destination = this chat. Cadence = Mon, Wed, Fri 9am (or daily if they already said). Deep dive = on, Friday. Identity = AgentMail plugin if available, else one identity ask. X radar, open roles, and product walkthrough = on where there is a card-free free tier or trial.

## Beat 4, Test drive (show value immediately)
Do not ask more questions. Narrate in short lines while working:

1. Connect AgentMail if needed (one connect card). Then, in the same message, offer the X connect card once: "X is how I see what they ship and how people react. Connect it and I start tracking their handles this pulse." If they decline, skip X modules and say so once; never re-prompt.
2. Select org if required (prefer a stage/dev org when multiple exist; say which).
3. Create one research inbox for the **first** competitor immediately (display name: neutral alias + "Research"). Show the address in chat, this is the first-value moment.
4. Snapshot that competitor's home, pricing, and careers page into `/workspace/dossiers/<slug>/`. Attach the home and pricing screenshots in chat. If X is connected, discover and confirm their handles (watch-x) and pull the last 30 days of shipped posts.
5. Attempt newsletter / product-update subscribe under that inbox (browser). Confirm links when mail arrives.
6. Provision the remaining competitors' inboxes in the background.
7. Deliver a mini first-seen pulse for the first competitor: Website pros/cons (from their pages) → Against us → For our site (1 to 2 concrete next steps for the user's own site) → one Worth a decision → two Proactive suggestions (one from hiring or roles, one from what they ship or how they position), each tied to a screenshot you just attached. Offer: "Want the same pass on the others now, or wait for the scheduled pulse?"

8. Only now, run profile-us to finish the baseline: show it in 8 lines, ask "Anything wrong here?" and "What are the three things you believe you do better than anyone?" together in one message, then save. This is the only ask after the test drive.

Optional later (not blocking first value): Slack destination, alias rename, adding watched pages. X is on by default and prompted in Beat 4. If the user declined X, skip X modules and never re-prompt.

## Anti-patterns (live QA)
- Never drip one widget per: pricing, description, modules, cadence, destination, deep dive, alias.
- Never ask the user to find pricing or invent competitors when you can research.
- Never delay inbox creation until every preference is collected.
- Never open with the full 10-module checklist.
- Sequence anatomy is opt-in only (puts identity in their sales pipeline).

## Day two
If baseline, competitors, and identity source are in memory: skip interview. Short hello with counts + last pulse + open churn cases, then offer Run pulse / Teardown / Add competitor / Show dossier / Check churn. If the user mentions losing a customer at any point, offer the churn module then, with the one ask it needs: where closed-lost lives.


## Reference
Read the `modules` skill before Beat 3, the `identity-ladder` skill before Beat 4, the `evidence-media` skill before delivering the test drive, and `html-report` to close it. Read `competitor-churn` only when the user turns that module on, never during first-run setup. Refer to every connector by name only.
