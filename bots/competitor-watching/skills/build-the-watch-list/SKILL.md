---
name: build-the-watch-list
description: "Use when the user first names competitors, adds or drops one, or asks who you are tracking."
---

# Build the watch list

Part of the Competitor Watch agent preset.

Inputs: competitor names, URLs, a pasted list, a CSV, a shared sheet, or just their category.

1. Get a name and a root domain for every competitor. Given names only, find the domain and confirm it is the company's own site before you use it.
2. For each one, locate and verify four pages: pricing, changelog or release notes, product or features, and careers. Add a blog or newsroom when they publish there. Mark a page type missing when it truly does not exist.
3. Fetch each URL once. Anything that blocks you, redirects oddly, or renders empty gets replaced, or marked unreadable with a note.
4. Write one row per page: competitor, page type, URL, status, last checked. Include the user's own site tagged as theirs when you have it.
5. Show the table in chat, take one round of edits, then save.

Fallbacks: a page you cannot find gets asked for before you drop it. A category instead of names means you propose up to 8 companies with links and wait for approval. A CSV or sheet that will not parse means you ask them to paste the rows.

Cap the list at 8 unless they insist. The watch list is the source of truth for who is tracked, so edit it in the same turn the user adds or drops a competitor. Save under competitors.
