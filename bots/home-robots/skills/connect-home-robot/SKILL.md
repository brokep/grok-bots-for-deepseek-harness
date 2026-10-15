---
name: connect-home-robot
description: "use this when the user wants to connect a robot vacuum, mower, mop, or other home robot that is not Navimow or Matic"
---

# Connect home robot

Part of the Home robots agent preset.

---
name: Connect home robot
description: >-
  use this when the user wants to connect a robot vacuum, mower, mop, or other
  home robot that is not Navimow or Matic
---
Use this when the user wants to add a robot vacuum, mower, mop, or other home robot that is not already covered by Connect Navimow or Connect Matic. If it is a Segway Navimow, run Connect Navimow. If it is a Matic vacuum, run Connect Matic.

Ask the brand and what it is if they did not say. Never ask them to paste a password, 2FA code, or access token into chat.

Official only: a catalog connector if SearchPlugins finds a real one; Home Assistant's core/official integration for that brand including Matter; or the vendor's own documented cloud SDK. Do not use unofficial HACS repos, reverse-engineered local protocols, community Bluetooth pairing, cookie scraping, or app scraping. If the only known path is unofficial, say so and stop.

If Home Assistant is already connected, reuse it.

How to connect:
1. SearchPlugins for the brand. If a real connector exists, confirm, then install and authenticate it.
2. Else look up the official Home Assistant integration on home-assistant.io (examples of official pages: roborock, roomba, husqvarna_automower, matter). Confirm it is a core/official page, not a random GitHub fork.
3. Walk them through that official HA setup (vendor app account, Matter pairing from the robot's app, or the vendor's documented OAuth).
4. If they do not have Home Assistant and the device is local Matter or a HA-only official integration, say they need Home Assistant as the bridge.
5. Enable Home Assistant's Model Context Protocol Server if needed. Get the MCP URL and a long-lived token via secret-request. Confirm, then add the MCP server.
6. Confirm the entity exists (vacuum, lawn_mower, or the official domain).
7. Remember only non-secret facts: brand, type, display name, and how it is connected.

When done, tell them they can say start, pause, go home, clean a named room if mapped, or how's it doing.
