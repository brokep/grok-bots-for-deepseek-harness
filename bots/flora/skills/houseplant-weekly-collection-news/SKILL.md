---
name: houseplant-weekly-collection-news
description: "use this during the weekly houseplant check to look up a few cheap news items about plants the owner actually owns"
---

# Houseplant weekly collection news

Part of the Flora agent preset.

---
name: Houseplant weekly collection news
description: >-
  use this during the weekly houseplant check to look up a few cheap news items
  about plants the owner actually owns
---
Use this during the weekly houseplant check, after the care list. Look for a few real items from the past week about plants the owner actually owns. Keep it cheap. Missing news is normal. Do not pad. Do not burn weekly usage on a media binge.

## When

Only as part of the weekly check, and only after they have at least one real plant and have watched a practice run. Do not create that weekly reminder until then. Skip sample plants and species guides. If they have no real plants, skip news.

## Token cap (hard)

Per weekly run, do at most:

1. One web search covering **all** owned species in a single query (common names and scientific names together, plus news/study/price, past week).
2. One YouTube title search the same way (`site:youtube.com`, titles and dates only). Do not watch videos. Do not fetch transcripts.
3. At most one full page fetch, and only if a title clearly names an owned species and looks like real news (a paper, a price spike, a pest/recall, a major care change). Prefer the title and link. Do not fetch paywalled journals in full.
4. X only if they already Connected it **and** asked to include X in the weekly. Then one cheap search after reading the X MCP guide and checking credits. Never post. Never like. Never tell them to buy X credits unless that check shows about $0 or the search would exceed the balance. If X is not connected, skip it. Do not Connect X on first-run.

If those few calls find nothing usable, stop. Say nothing new this week for your plants. Do not run extra searches to fill the slot.

Cap the digest at **three items**. Each item: title, source name, date if known, link, one sentence on why it matches an owned plant. No quotes dumped from the article.

Do not install Bright Data, Exa, Firecrawl, Tavily, Context.dev, or any other paid search plugin for this. No YouTube plugin existed in SearchPlugins as of 2026-08-30. No plant-news plugin. Built-in web search is enough.

## Named sources to check (this list, not a crawl of the whole web)

Check in this order, using the capped calls above, not one call per site:

1. Built-in web search (Google-style). Query the owned species plus news, study, price, pest. This is the main pass.
2. YouTube titles through that same web search (`site:youtube.com`). Titles only.
3. PubMed (https://pubmed.ncbi.nlm.nih.gov/) only if a scientific-sounding title appeared, or as the optional one-page fetch. Titles and abstracts, not full PDFs.
4. RHS (https://www.rhs.org.uk/) if a hit is actually theirs.
5. Wikipedia species pages only if a hit is a **new** revision about that species this week. Do not re-read care pages you already used at intake.
6. X (plugin 49086599) only if they Connected it and opted in. Search posts about owned species. Never post. Credits are separate from Grok Bot weekly usage; still keep it to one search.

Do not scrape Plantipedia. Do not use Grokipedia as a news source. Do not invent a Missouri Botanical Garden fetch if it is blocked. University extension pages are fine if they appear in the one web search; name the live URL.

## What counts as news

Include only if it is about a species they own and it is actually new this week:

- A paper or journal note (enzyme, disease, taxonomy)
- Price or availability (resellers, sold-out cultivar)
- Pest, recall, or import alert
- A substantial new care video or article for that species

Skip generic “10 houseplants” listicles, ads, and anything that does not name one of their plants.

## Deliverable

After the watering/fertilizer/frost list, a short “This week in your plants” bit: zero to three items, or one sentence that nothing turned up. Stay in this chat. Do not publish, post, or email it.
