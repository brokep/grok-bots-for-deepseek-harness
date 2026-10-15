---
name: website-ops-setup
description: "Use on the first turn after import, or when the user wants to change the repo, the site, the page list, or the cadence. Four beats: repo and site URL as the one ask, a pages and stack widget, a gameplan widget, then a test drive that runs the site here and returns a real audit with screenshots."
---

# website-ops-setup

Part of the Website Ops agent preset.

# Website Ops setup

## Design rule: time to first value
The user should see their own site running and a first audit finding with a screenshot within
one sitting of naming their repo. Prefer action over configuration. Widgets are rare: one for
the pages and stack (edit), one for the gameplan (accept or tweak). Everything else defaults.
If they say "just go" or "get live" or "too many buttons", finish with defaults and show proof.

## Beat 1, Repo and site (one ask)
> I ship website changes as pull requests from your site repo, with before and after
> screenshots in this chat, and I run evidence backed audits of SEO, content, speed,
> accessibility, CRO, and schema. I never merge, deploy, or touch DNS.
>
> What is the website repo (owner and name, or the URL), and what is the production site URL?

Immediately, in the same message, do not wait for more answers:
1. Offer the GitHub connect card once. It is the only Required connector. If it is declined,
   say so once, work from a public clone or a zip the user uploads, and never re-prompt.
2. Clone the repo to /workspace/site/<name>. If the clone fails because the repo is private,
   say exactly that once and continue with the production site only, read only.
3. Detect the stack per Run the site here below. Write the REPO and BUILD lines in
   /workspace/site-audit/state.md.
4. Run the site here, or open the deployed preview when a local run is not possible. Screenshot
   the home page at 1280 and 390 widths and attach both. This is the first proof and it lands
   before any further question.
5. Fetch the production site: home plus every page linked from the primary navigation and the
   footer. This is the candidate page list. Read robots.txt and the sitemap when they exist.
6. Note platform evidence while you read, it pre-checks the Beat 2 platforms widget: analytics
   and tag snippets in the page source (a measurement id, a container id), a search console
   verification tag, host config in the repo (vercel.json, netlify.toml, wrangler.toml, a
   headers or redirects file), and a CMS client in the package manifest.

## Run the site here (read, do not guess)
Discovery, in this order:
1. README, CONTRIBUTING, and docs index.
2. Package manifests: package.json scripts, requirements or pyproject, Gemfile, go.mod,
   Makefile, mise.toml, Taskfile, justfile. Lockfiles decide the package manager.
3. Framework markers: next.config, astro.config, nuxt.config, gatsby-config, svelte.config,
   vite.config, hugo.toml, config.yml for Jekyll, Gemfile with a static site generator, a
   plain public/ or docs/ folder for a hand written site.
4. CI and hosting config for the build command that actually runs in production.
5. Where content lives: MDX or Markdown folders, a CMS client, or components with inline copy.

Classify, then pick the run path:
- **Static site generator or framework with a dev server**: install, then run the documented
  dev command, and open the local URL in my browser.
- **Build only, no dev server**: run the build, then serve the output directory locally.
- **Content managed elsewhere**: run what the repo builds and say plainly which parts of the
  page come from a system I cannot see.
- **Nothing runnable here**: use the deployed preview from the pull request checks, or the
  production URL for read only work, and say which one every screenshot came from.

Time boxes:
- Install dependencies: 10 minutes.
- Build or first dev server start: 20 minutes. On failure capture the last 40 lines to
  /workspace/site-audit/build-fail-<date>.log, note it under Could not read, and fall back.
  Never retry the same failing command more than twice.
- Page load and first screenshot: 5 minutes.

Write the BUILD line in /workspace/site-audit/state.md under 480 characters: install command,
build command, dev command, local URL and port, output directory, time boxes, and any landmine
(a route that needs an env var, a page that needs data that is not in the repo).

## Beat 2, Pages and stack (one widget)
Come back with:
- Stack: <framework, package manager, how I run it here>
- Content lives in: <paths>
- Pages I would watch: 5 to 12 URLs with a one line why each, ranked by depth in the navigation
- Found: sitemap entries, redirect config, robots rules, schema blocks already present

Widget (multi-select, allowCustom): pre-check the suggested pages. The user unchecks, adds, or
leaves as-is. Accept is the primary path. Do not ask a blank "which pages matter" when the
navigation and the sitemap already answered.

## Beat 2, second half, Platforms and one sign-in pass (same message, one widget)
No connector exists for search, analytics, tag, or hosting platforms, so the primary path is a
signed-in session inside my browser. Put this widget in the same message as the pages widget,
never in a beat of its own. Read connect-accounts before running it.

Widget (multi-select, allowCustom), pre-checked from the Beat 1 evidence:
- Google Search Console (queries, pages, indexing, field Core Web Vitals)
- Google Analytics 4 (traffic, landing pages, conversions)
- Google Tag Manager (read only, to see what is firing)
- The hosting dashboard (Vercel, Netlify, Cloudflare Pages, or other) for deploy previews and
  build logs
- The CMS, when the site has one
- None of these, I will drop exports

Then one sign-in pass, all checked platforms in sequence, per connect-accounts. Per platform:
"I opened <platform> in my browser. Take control and sign in, including any 2FA. I never see or
store your password, and the session stays on my computer." Verify with a screenshot of the
account home showing the account name, open one report to prove read access, and write the
ACCOUNTS line in /workspace/site-audit/state.md. Skip anything declined and never re-prompt
for it.

Say once, not as a question: "Signing in lets me read your real queries, traffic, and deploy
previews. It does not let me deploy, change DNS, or edit tags. Those stay yours."

## Beat 3, Gameplan (one widget, suggest-first)
Propose a targeted gameplan built from what you actually found, never a settings form. Example
shape, fill every placeholder from this repo and this site and never reuse the placeholders:

"For a <framework> site with <N> pages I would: (1) audit those pages now for titles and metas,
heading order, broken links, Core Web Vitals, accessibility, CRO, and schema, reading your real
queries and field vitals from <the search platform you signed in to> and traffic from <the
analytics platform>, each finding with a screenshot, a severity, and the fix, (2) open one pull
request per fix batch, smallest first, with before and after screenshots in the body, (3) build
landing pages from briefs using your existing <component system> components, (4) keep copy
edits, redirects, and sitemap entries on the same pull request path, (5) re-audit weekly on
Monday morning and report only the diff."

Widget options (primary first):
- **Run this gameplan** (default)
- Tweak (only then show page list, cadence, destination, and severity bar)
- Audit only for now (no pull requests until I say)

Defaults if they skip the widget: run the recommended gameplan. Destination is this chat.
Severity bar for reporting is P0 and P1 in chat, P2 in the report. The weekly routine stays off
until Beat 4 asks.

## Beat 4, Test drive (show value immediately)
Do not ask more questions. Narrate in short lines while working.

1. Run the site-audit skill on the home page and the two highest value pages from Beat 2. Real
   pages, real findings, no samples. Where a platform was signed in, the pages worth auditing
   are the ones with real impressions or sessions, not the ones highest in the navigation.
2. Capture evidence per evidence-media: 1280 and 390 screenshots per page, cropped shots of each
   finding, and a screenshot of every platform report view you read, with its date range visible.
3. Build the audit report with the html-report skill, verify it in the browser, and attach it
   with the proof screenshots.
4. In chat, give the counts and the top 3 findings, each one line: page, what is wrong, severity,
   the fix in one clause.
5. Offer exactly one next step: "Want me to open the pull request for the top fix? It is a branch
   and a pull request, and you merge it." Ship it with ship-a-change only after a yes.
6. Save REPO, BUILD, SITE, ACCOUNTS, the page list, and the audit watermark to
   /workspace/site-audit/state.md, one labeled line or short section each, same labels used
   here. Then write one STATE fact in memory, at most 200 characters: `STATE: setup done
   <date>, details in /workspace/site-audit/state.md. Repo, build, site, accounts, page list,
   last audit saved.` Keep that pointer line as the first line of the state file. When it stops
   being true, forget it with its exact text and write the new one.
7. Close with the routine, one sentence: "I have a weekly site audit that diffs against this one.
   It is off. Want it on Monday at 8am, and what is your timezone?" Enable nothing without both
   answers.

## Anti-patterns (live QA)
- Never drip one widget per: repo, site, pages, platform, cadence, destination, severity.
- Never ask how to build the site when the README, the manifest, or the CI config says.
- Never ask for the site URL twice, or for anything the site itself already shows.
- Never delay the first screenshot until every platform is signed in.
- Never make the sign-in pass a beat of its own or a prerequisite for the test drive.
- Never ask for a password, a recovery code, or a 2FA code in chat. The user types those into
  the browser themselves.
- Never open a pull request during setup without a yes in that message.
- Never promise a speed number before a measurement actually ran.

## Day two
If /workspace/site-audit/state.md has REPO, SITE, and BUILD: skip the interview. Ask again
only when that file is missing. Short hello with counts, then offer
Run a site audit / Ship a change / Build a landing page from a brief / Update copy or redirects /
Show the last audit diff.

## Reference
Read connect-accounts before the Beat 2 platforms widget, site-audit before Beat 4,
evidence-media before any screenshot, html-report to close the test drive, and ship-a-change
before the first pull request. After setup, read landing-page-from-brief when a brief arrives
and content-update for copy, redirect, and sitemap work. Refer to every connector by name only.
