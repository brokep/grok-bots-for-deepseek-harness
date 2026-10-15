---
name: connect-matic
description: "use this when the user needs to connect a Matic robot vacuum, finish first-run setup, or re-authenticate"
---

# Connect Matic

Part of the Home robots agent preset.

---
name: Connect Matic
description: >-
  use this when the user needs to connect a Matic robot vacuum, finish first-run
  setup, or re-authenticate
---
Walk the user through connecting their Matic so this bot can send commands. Keep it conversational. Never ask them to paste a password, 2FA code, or access token into chat.

Matic's official control path is Matter via Home Assistant. This bot cannot reach the robot on the user's Wi-Fi by itself. Do not use unofficial SDKs, reverse-engineered local protocols, community Bluetooth pairing, or app scraping.

If Home Assistant is already connected, reuse it.

Official path: In the Matic app, Settings → Connectivity → Connect to Smart Home App → Enter Pairing Mode → Home Assistant. Official guide: https://support.maticrobots.com/how-to-connect-matic-to-home-assistant
IPv6 must be on. Enable Home Assistant's Model Context Protocol Server. Get the MCP URL and a long-lived token via secret-request. Confirm, then add the MCP server. Confirm a vacuum entity exists. Optionally map Matic rooms to Home Assistant areas.

If they do not have Home Assistant, say they need it as the bridge. Do not offer unofficial workarounds.

When done, tell them they can say start cleaning, clean the kitchen, pause, go home, or is Matic docked.
