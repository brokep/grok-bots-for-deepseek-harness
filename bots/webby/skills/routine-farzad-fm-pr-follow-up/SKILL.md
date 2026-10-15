---
name: routine-farzad-fm-pr-follow-up
description: "Scheduled routine: On personal-site PR open, push, or merge: fix owned content issues; production-deploy after merge to main."
---

# Site PR follow-up

Part of the Webby agent preset.

Schedule, as written by the template author: On personal-site PR open, push, or merge: fix owned content issues; production-deploy after merge to main.

## What to do on each run

Site follow-up for a GitHub PR event on the personal-site repo (pr-opened, pr-pushed, or pr-merged).

If the PR is new and relevant to the live site (content, Exclusive, Digest, layout, deploy-blocking YAML), handle the site follow-up: review what changed, fix Exclusive/Digest/frontmatter issues you own. Create-only on content you own. No catastrophic deletes. No production DNS.

On pr-merged to main: production-deploy the personal site so the homepage picks up new Exclusive/Digest. The host is not Git-connected; a merge alone does not update the home screen. Never print the token. Ping the orchestrator with SHA + deploy id.

Do not double-ping the owner for the same PR within an hour. Stay quiet on noise (docs-only, already-handled, duplicate wake).

Fires on:
- GitHub pr-opened, pr-pushed, pr-merged

Ask the importing user for:
- GitHub repository
