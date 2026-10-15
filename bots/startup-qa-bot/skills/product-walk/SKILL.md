---
name: product-walk
description: "Use to walk the user's product in the test account: the first baseline map, and the daily walk of every surface plus change signals. Non-destructive only."
---

# product-walk

Part of the Startup QA Bot agent preset.

# product-walk

The walk of the user's product in my test account. Used by setup, "walk the product", and morning-product-walk. Non-destructive only.

## Baseline, the first walk

The check in test-account first. qa.py walk, then map the product in my own browser: each nav item, page, and main feature a user reaches in two clicks, plus settings. For each: qa.py surface "<name>" --where "<url or click path>" --expect "<what a user should see>", with a shot. Aim for 10 to 30. Then qa.py rundown to close it (don't send its message), show the map in 3 lines, and ask what's missing.

## Daily walk

1. The check in test-account. Then qa.py walk prints the run folder, the surfaces to check, and open bugs to recheck.
2. Change signals since the last walk: merged PRs, Linear issues moved to done, new changelog entries. Each names something that should be live now. Check those first.
3. Visit each surface in my own browser: look, click through, open and cancel. qa.py check <id> ok, missing, or broken --note "<what you saw>" --shot <path>. qa.py browser errors after each page, console errors are evidence. Something new: qa.py surface ... --new.
4. Recheck each open bug's repro. Works now: qa.py fixed <id>.
5. Shots: Screenshot, then qa.py shot <path> <what it shows>.
6. Then product-rundown.
Asked "is X live?" any time: check that surface now in my browser and answer with a shot.

## Never

Submit, send, pay, invite, delete, publish, or change settings, even in the test account, unless the user approved that exact check.
