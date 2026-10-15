---
name: content-update
description: "Use for copy edits, redirects, robots rules, and sitemap entries, and for the copy pass whenever this bot writes words without a brief. Finds where the words or rules actually live, changes only those, verifies on a real page load, and ships one pull request per reason."
---

# content-update

Part of the Website Ops agent preset.

# Content update

Copy edits, redirects, and sitemap changes. Small by nature, same gates as everything else.

## Copy edits
1. Find where the words actually live: a Markdown or MDX file, a content collection, a component
   with inline text, or the CMS. When the CMS is signed in, search it for the string before
   assuming the repo holds it. Copy that lives in the CMS is changed by the user in the CMS,
   not by me, and I say exactly that rather than editing a lookalike string in the repo.
2. Change only the strings the user asked for. Keep the surrounding markup, the component, and
   the file formatting untouched.
3. Check every place the same string appears. A headline usually also lives in the metadata, the
   Open Graph tag, the navigation label, or a schema block. List the extra hits and ask before
   changing them.
4. Screenshot the affected page before and after at 1280 and 390, then ship per ship-a-change.

## Copy pass
Run this on any words I write or rewrite without a brief telling me what to say. With a brief,
the brief's words win and this pass only catches the gaps. A teammate that writes copy owns the
full editorial pass when one exists on this team. This is the floor, not that pass.

1. No em dash, no en dash used as a pause, no double hyphen standing in for one. Use a period,
   a comma, a colon, parentheses, or a spaced hyphen. If a dash feels needed, write two
   sentences.
2. Never invent a fact. No number, price, metric, customer, logo, quote, award, or claim that
   is not already on the site or in the source. A gap stays a visible gap, marked in the pull
   request body as needing input, never filled with something plausible.
3. Lead with the thing. Cut throat clearing. The first line earns the rest.
4. Keep their voice. An edit tightens what is there, it does not rebuild the page in a
   different register. Match the surrounding copy on the same site.
5. Strip the empty verbs and adjectives on sight: leverage, seamless, unlock, empower,
   streamline, robust, cutting edge, best in class, game changing, next generation. Also cut
   rule of three adjective piles and hype with no evidence behind it.
6. Read it back. If a line is trying to sound impressive rather than say something, flatten it.

Do not narrate this pass. Hand back the copy. Only when the user asked for reasons, list the
material changes, one reason each.

## Redirects
0. Before moving or removing any URL, check what it is worth. When the search platform is
   signed in, read its clicks, impressions, and queries for the last 3 months, and when the
   analytics platform is signed in, read its sessions. A page with traffic gets a permanent
   redirect to the closest equivalent, never to the home page, and the numbers go in the pull
   request body. Without either platform, say the page value is unknown and ask before removing.
1. Read the repo's existing redirect mechanism (framework config, a redirects file, middleware,
   or server rules). Use the one that is already there. When the hosting dashboard is signed
   in, compare it with the rules the host actually has, because the host is what runs. Report a
   difference, do not fix it in the dashboard.
2. For each redirect record: source path, destination path, status code, and why. Default to a
   permanent redirect for a moved page and a temporary one for a page coming back.
3. Check for a chain or a loop against the existing rules before adding. A new hop onto an
   existing redirect becomes one direct rule instead.
4. Check inbound links inside the site to the old path and update them in the same pull request,
   so the redirect is a safety net rather than the mechanism.
5. After the build, verify each new rule on the local run or the preview and screenshot the
   result. Never verify a redirect by reading the config alone.

## Sitemap and robots
1. Prefer whatever generates the sitemap already. Edit the generator's inputs, not the generated
   file, unless the file is hand maintained.
2. New pages get an entry. Removed pages come out in the same pull request as the redirect.
3. Never change robots directives or add a noindex rule without an explicit yes. A wrong rule
   here removes pages from search.

## Output
One pull request per reason, per ship-a-change, with before and after screenshots at both widths
in the body and in this chat, plus the list of paths touched and the verification steps.

## Never
Edit a generated file that will be overwritten by the next build. Change a canonical, a robots
rule, or a live URL without an explicit yes. Change a redirect, a header, or a tag inside a
platform dashboard, even when signed in. Bulk rewrite copy the user did not ask about. Deploy
or merge.
