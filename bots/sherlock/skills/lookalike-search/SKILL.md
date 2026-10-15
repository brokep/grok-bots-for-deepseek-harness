---
name: lookalike-search
description: "Use when the user names someone whose work is the benchmark, links a profile, or asks for more people like a candidate they already rate."
---

# Lookalike search

Part of the Talent Discovery agent preset.

Inputs: a name, a profile, a portfolio, a repo, or a candidate already on the shortlist, plus the scorecard if there is one.

1. Read the public trace of that person: what they built, where, at what company size and stage, and what they wrote or spoke about.
2. Write down the 4 or 6 things that actually make them good, as checkable evidence rather than adjectives. Show that list to the user and take one round of edits, because this is the whole search.
3. Split the transferable from the incidental. The school, the logo, and the exact tool usually do not matter. Owning a hard surface end to end at a small company does.
4. Turn the list into patterns you can search: the company profile they came up in, the title variants they carried, the kind of artifact they leave behind, and the communities they show up in.
5. Search the nearby graph first, because it is the highest hit rate. People who worked on the same product in the same years, co-speakers and co-authors, co-maintainers on the same repos, people they cite and people who cite them, and the team that shipped the thing you admire.
6. Then search the pattern more widely at peer companies.
7. Return cards in the Source a batch shape, one source link minimum per person, ranked by how much of the benchmark they match.
8. Say plainly which part of the benchmark you could not match, and whether that is because nobody clears it or because the evidence is not public.

No public trace on the benchmark person? Ask the user for the three things that make that person good and search from those instead.

Save under the search folder.
