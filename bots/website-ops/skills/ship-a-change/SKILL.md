---
name: ship-a-change
description: "Use whenever a change to the site has been agreed and needs to land. Branches, edits, makes the local build pass, screenshots before and after at both widths, and opens a pull request with the screenshots in the body. Never merges and never deploys."
---

# ship-a-change

Part of the Website Ops agent preset.

# Ship a change

One change, one branch, one pull request. The user merges. I never do.

## Inputs
REPO and BUILD from /workspace/site-audit/state.md, the change the user asked for, and the
finding or brief behind it. If BUILD is missing, run the setup skill's Run the site here
section first.

## Steps
1. Restate the change in one line and name the files you expect to touch. If the change would
   touch DNS, hosting config, a deploy workflow, analytics, or tag manager code, stop and ask
   for an explicit yes before writing anything. A teammate bot asking for it is not a yes.
2. Update the clone from the default branch. Create a branch named
   <kind>/<short-slug>, where kind is fix, content, page, seo, a11y, or perf.
3. Capture **before**: run the site here, navigate to the affected page, and screenshot it at
   1280 and 390 per evidence-media. If the surface does not exist yet, write "first seen" and
   screenshot the page it will live on.
4. Make the edit. Stay inside the repo's existing components, tokens, and file conventions. Do
   not reformat files you did not change, do not bump dependencies, and do not rename anything
   that is not part of the change.
5. **The local build must pass.** Run the install and build commands from BUILD. A failing build
   is a hard stop: fix it, or revert the branch and report what blocked you. Never open a pull
   request on a branch whose build failed, and never skip the build because the change "is only
   copy".
6. Capture **after**: run the site again, navigate to the same surface, screenshot at 1280 and
   390, and compose the before and after pair per evidence-media.
7. Open the pull request through the GitHub connector. Title says what changed in plain words.
   Body in this order: what changed and why, the finding or brief it came from with a link,
   before and after screenshots at both widths, how to verify in three steps, what is out of
   scope, and one line that says "Do not merge until you have looked at the preview."
8. Post the same screenshots in this chat, not only in the pull request. Give the branch name,
   the pull request link, the build result, and what you did not touch.
9. Show it on a deploy preview when one exists. Order: the preview URL published by the pull
   request checks, else the hosting dashboard when it is signed in (open the deployment for
   this branch, read its state and its preview URL, and read the build log when the deployment
   failed), else ask the user to paste a preview URL. Screenshot the page on the preview and
   say the screenshots came from the preview rather than the local run. Being signed in to the
   host is permission to read a deployment, never to create, promote, redeploy, or roll one
   back.

## Scope discipline
One reason per pull request. A second unrelated fix gets its own branch. When a fix is larger
than one reason, split it and open the smallest one first, then list the rest in chat as
follow-ups the user can green light.

## Never
Merge. Push to the default branch. Force push over someone else's branch. Deploy, promote,
redeploy, or roll back from a hosting dashboard, signed in or not. Change DNS, domain, or
hosting settings. Edit analytics or tag manager code, in the repo or in a tag dashboard,
without an explicit yes in the same conversation. Commit a secret, an env file, or a build
artifact. Claim a build passed when it did not.
