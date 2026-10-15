---
name: build-the-x-watch-list
description: "Use when the user first names accounts or topics to watch, adds or drops one, or asks what you are tracking."
---

# Build the X watch list

Part of the X Brief agent preset.

Inputs: handles, profile links, a pasted list, a topic list, an export, or just the field they work in.

1. Normalize every account: strip the @, resolve profile links to handles, and confirm the account exists before you track it. Name the handles you could not find instead of guessing at a spelling.
2. For each account, write who they are in five words or fewer. The brief uses that line to say why their post matters.
3. Turn each topic into real searches. Two or three phrasings per topic, including product names, company names, and the shorthand the field actually uses. A topic with no working search gets dropped with a note, not kept as decoration.
4. Ask once for a mute list: accounts, phrases, or kinds of post they never want to see. Honor it on every run after.
5. Cap the list at 15 accounts and 8 topics unless they insist. Past that the brief becomes the thing they were trying to avoid.
6. Write one row per entry: kind (account, topic, or search), the handle or query, who they are or why it is tracked, how you read it (connector or public page), status, and last checked.
7. Show the list in chat, take one round of edits, then save.

Fallbacks: with only a field to go on, propose up to 12 accounts and 5 topics with links and wait for a yes. When X is connected, seed the list from who they already follow and from their lists, and say what you added. When it is not, offer the connector once as the thing that makes the list better, then move on with what they pasted. A profile you cannot open stays on the list marked unreadable, with one line saying you will be reading it through the public web instead.

Edit the list in the same turn the user adds or drops something. Save under x-brief.
