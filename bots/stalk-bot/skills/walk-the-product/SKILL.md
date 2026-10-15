---
name: walk-the-product
description: "Default-on module. Sign up, walk onboarding on video, then aggressively test every feature you can reach with test data, recording a clip and screenshots per feature. Ends with a self-contained HTML teardown report. Handles web, open-source, and downloadable products with explicit fallbacks."
---

# walk-the-product

Part of the Stalk Bot agent preset.

# Walk the product

## Inputs
Competitor, product URL, research identity, whether the teammate identity bot exists.

## Decide the path
1. Web product with email signup: browser path.
2. Open source or self-hostable: try the hosted web version in my browser first. If none, clone and run on my computer.
3. Desktop or mobile app: if there is a web version, browser path. If Linux build or install is possible, try it. Otherwise public materials only (docs, videos, screenshots on their site) and say so.

## Browser path
1. Get the identity signed up: if a teammate identity bot exists, send AUTH REQUEST need signup and wait for AUTH RESULT on a later turn. Otherwise run the signup myself with the research identity, catch the code from the inbox, and store any password via secret-request with only label "<competitor> research password" and name "STALK_<COMPETITOR_SLUG>_PASSWORD" (env var; never invent connector/field args).
2. Start a recording per the evidence-media skill (browser recording, ffmpeg screen capture, or stitched slideshow as fallback). Log in. From the first screen, screenshot every step. For each step record: what it asks, required fields, defaults, skippable or not, time spent.
3. Note the moment of first value (first useful output or completed core action). Record steps-to-value and minutes-to-value.
4. Feature test pass (aggressive, this is where the value is). Build a feature list from the navigation, the pricing page, the docs index, and the changelog. Then for EVERY feature reachable on the free tier or trial, do all of the following, recording a clip and screenshots per feature:
   - Exercise the happy path end to end with obviously fake test data (Test Co, the research identity's address, lorem content). Get to a real output, not just the entry screen.
   - Try the empty state, the maximum (paste a long input, add the 11th item, upload a large file), an invalid input, and cancel midway. Note what breaks, what is validated, what silently fails.
   - Find every plan gate: what is greyed out, what shows an upgrade prompt, what limit is stated. Screenshot the gate.
   - Integrations: open the integrations page, count them, try to connect one that needs no external account (webhook, CSV import, public API key page). Note auth type and whether it works on the free tier.
   - Collaboration: invite the research identity's own second alias if inviting is free, check what a second seat sees.
   - Export and API: try every export (CSV, PDF, JSON), open the API docs from inside the product, note whether an API key can be created on this tier.
   - Settings, billing, and account deletion: read every settings page, screenshot billing and plan pages from inside, find the delete-account path but do not run it.
   - Speed and reliability: time the three slowest actions, note any error toasts, and screenshot them.
   - Docs and help: open in-app help, count help articles for the feature, note whether AI help or chat support exists.
   Per feature write: name in their words, what it does, steps to a real result, what worked, what broke, plan gate, integrations touched, time, and "vs us" in one line from the baseline. Aim for 8 to 20 features per product; if fewer than 6 are reachable on the free tier, say so as a finding.
5. Find the settings, integrations, and billing pages. Record plan names and gates as seen from inside.
6. Log out. Do not change account settings that email the user.

## Clone and run path
1. Find the repo. Read the README for install steps. Clone to /workspace/stalk/<competitor>/.
2. Follow the documented install. Prefer Docker if offered. Time-box 20 minutes. Record the terminal and browser during install as the onboarding video for self-hosted products.
3. If it runs: open it in my browser and continue with the browser path from step 2.
4. If install or build fails: capture the exact error, tell the user "I could not run <competitor> locally: <error in one line>. I evaluated the public docs and screenshots instead. If you want the full walkthrough, the hosted version needs <what>." Then continue with public materials. Never claim a walk happened.

## Hard stops (record as findings, not failures)
Card required to start trial. Phone or ID verification. Terms forbidding automated or competitive use (stop this module for the competitor and name the clause). SSO-only signup.

## Output
Write /workspace/dossiers/<competitor>/teardown.md: path taken, signup friction, onboarding steps table (step, asks, required, skippable, screenshot), steps and minutes to first value, feature test results (one block per feature as above), plan gates seen, upsell moments, empty states and errors worth noting, integrations count and auth types, exports available, three things they do better than us, three things we do better, open questions. Then run html-report to build the teardown report with the onboarding video, every feature clip, and every screenshot embedded. Attach the HTML report, the onboarding video, up to 3 feature clips, and up to 8 key screenshots. Then say in chat: 5 lines, the counts (features tested, screenshots, videos), and "full teardown in the report."

## Standing rules (from memory)
Free tier or trial without a card only. Stop at any payment field, phone verification, or ID request and record it as a finding ("requires card to start trial") rather than a failure. Screenshot every onboarding step and every main surface. Note required fields, steps to first value, time to first value, upsell prompts, empty states, default settings. Enter only obviously fake test data (Test Co, test@ the research identity), never the user's real customers, docs, or code. If the product is open source or downloadable: try the web version in my browser first, then clone or install on my computer, then run and walk it the same way. If clone, install, or build fails on my machine, tell the user exactly what failed and what I could and could not evaluate, then continue with public materials. Never pretend a walkthrough happened.
