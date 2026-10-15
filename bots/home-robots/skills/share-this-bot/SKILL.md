---
name: share-this-bot
description: "use this when explaining how someone else should import this bot and connect home robots"
---

# Share this bot

Part of the Home robots agent preset.

---
name: Share this bot
description: >-
  use this when explaining how someone else should import this bot and connect
  home robots
---
When the owner wants copy they can send to other people, give them a short note they can paste. Do not dump setup internals or secrets.

1. Open the template link and import the bot.
2. Tell it which robots they have (Navimow, Matic, Roborock, Roomba, Husqvarna, or anything else).
3. Navimow: sign in with the same account used in the Navimow app.
4. Matic and most other home robots: pair through official Home Assistant / Matter from the robot's own app, then let the bot connect to that Home Assistant.
5. Confirm the devices it finds.
6. Talk in plain language: start mowing, start cleaning, clean the kitchen, pause, go home, how's the battery.

Mention that start/resume will ask them to confirm people, pets, and floors are clear.

The bot uses official vendor apps, official Home Assistant integrations, and Matter. It will not use unofficial hacks. Recipients need Home Assistant for Matic and for most other local/Matter robots. Navimow can sign in directly. If they already use Home Assistant, one MCP connection can cover every robot HA already sees.

Do not send client secrets, tokens, device ids, or file paths.
