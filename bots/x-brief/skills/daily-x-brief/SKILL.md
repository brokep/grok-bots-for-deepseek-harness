---
name: daily-x-brief
description: "Use when the user asks what is happening on X, asks to be caught up, or when the daily brief routine runs."
---

# Daily X brief

Part of the X Brief agent preset.

Inputs: the watch list, the seen log, the window since the last brief, and their beat.

Signal bar, used unless they gave you their own: a launch or new version, a funding, hiring, or departure announcement, a number or benchmark someone published, a strong claim from someone with standing in the field, a thread that explains something worth keeping, and a shift in what the field is arguing about. Noise to skip: engagement bait, reposts with no comment, screenshots with no source, generic motivation, giveaways, drama with nothing under it, and rehashes of what you already reported.

1. Read the watch list and the seen log first. Never report a link already in the seen log.
2. Fetch every account and search across the window, posting what you have read as you go so the user sees movement inside a minute.
3. Keep an item only when it clears the bar. Cap the brief at 12 items.
4. Group what survives into 2 to 4 themes and name each theme in plain words.
5. Write each item as one line: the handle, what they said in your own words in twelve words or fewer, the link, and the local time. Quote at most 20 words, inside quote marks, with the handle attached.
6. Write every reported link to the seen log.

Output shape:

Today on your list, N items from M accounts and K searches.

The one thing: two lines on the item that matters most for their beat, and why.

Theme name
- @handle, what they said, link, local time

Being argued about
- The disagreement in one line, then a link for each side.

Worth reading in full
- Up to three links, one clause each on why.

Quiet today
- The accounts on the list with nothing.

Could not open
- Every post or profile you could not read.

Rules: no item without a link. Give engagement counts only when you read them yourself. A day with nothing that clears the bar is one line saying it was quiet, not a padded brief. Never invent a post, a quote, a handle, or a count.

Fallbacks: when X is connected, read through it, since it is the most complete path. Without it, read public post and profile pages and search the public web for the post being quoted elsewhere, and say once that connecting X would fill the gaps. A post that will not open gets named, never reconstructed. Pasted newsletters and link roundups count as one more source.

Save the brief dated under x-brief and attach it here, then deliver it to the destination they picked. Anything that posts or sends goes to them as a draft first.
