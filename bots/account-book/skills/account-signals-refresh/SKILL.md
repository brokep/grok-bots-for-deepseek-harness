---
name: account-signals-refresh
description: "Use when the user asks what is new at an account, before briefing an account you have researched before, or when the weekly signals routine runs."
---

# Account signals refresh

Part of the Account Research Desk agent preset.

Inputs: the account list, each account file, and the date of the last check.

Default bar for what counts, used unless the user gave you their own: funding or an acquisition, a leadership change in the function they sell into, a launch or a public roadmap post, a pricing or packaging change, hiring that points at a new initiative, a new office or market, layoffs or a restructure, a public outage or security incident, and earnings or investor commentary when it is public. Add anything the user asked you to always flag. Noise to ignore: award posts, routine hiring churn, blog reposts, conference booth announcements, and anniversary content.

1. Read the account file and the date of your last check. Never work out what is new from memory.
2. Check each company's own newsroom, blog, and careers page first, then the open web for anything since that date.
3. Save what you found with today's date before you write the summary. That is what the next check compares against.
4. Keep only what clears the bar. Date every item from the source's own date and say when a date is approximate.
5. Write one line per signal: the account, what happened, the date, the source URL, and what it means for this deal in plain words.

Output: signals grouped by account, newest first, then one line naming the accounts with nothing new.

Fallbacks: an account with no public news in the window gets one quiet line, never a padded section. Paywalled coverage gets named as paywalled instead of summarized from its headline. A rumor stays a rumor and gets labeled as one.

Save every signal dated into the account file, and say which part of the account plan a signal should change.
