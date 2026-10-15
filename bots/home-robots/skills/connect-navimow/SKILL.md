---
name: connect-navimow
description: "use this when the user needs to connect a Segway Navimow robot mower, sign in, finish first-run setup, or re-authenticate"
---

# Connect Navimow

Part of the Home robots agent preset.

---
name: Connect Navimow
description: >-
  use this when the user needs to connect a Segway Navimow robot mower, sign in,
  finish first-run setup, or re-authenticate
---
Walk the user through connecting their Navimow account so this bot can send commands. Keep it conversational. One step at a time. Never ask them to paste a password, 2FA code, or access token into chat.

There is no Navimow connector in the catalog. Control goes through Segway's official navimow-sdk on this computer (cloud API at https://navimow-fra.ninebot.com). Home Assistant is an optional fallback if they already run it.

Store tokens only at /home/box/.navimow/credentials.json (mode 600). Never put tokens, refresh tokens, or client secrets in chat, memory, skills, or routines.

If a credentials file already has an access_token, try listing devices before starting a new login.

Direct sign-in (default):
1. pip install -U navimow-sdk (Python 3.11+).
2. Fetch OAuth constants live from the official Home Assistant integration. Do not invent them and do not copy secrets into memory: https://raw.githubusercontent.com/segwaynavimow/NavimowHA/main/custom_components/navimow/const.py. You need OAUTH2_AUTHORIZE, OAUTH2_TOKEN, CLIENT_ID, CLIENT_SECRET, API_BASE_URL.
3. Start a short-lived local callback on this computer to capture ?code=.
4. Open the authorize URL in the computer's browser with channel=homeassistant and a redirect_uri pointing at that callback.
5. Hand the computer to the user to sign in with their Navimow app account. Never type their password.
6. When the callback gets code, POST it to OAUTH2_TOKEN as application/x-www-form-urlencoded: grant_type=authorization_code, code, client_id, client_secret, redirect_uri.
7. Save the token JSON. Discover mowers with MowerAPI.async_get_devices().
8. Remember only non-secret facts: mower display name, model, and that Navimow is connected.

If several mowers come back, ask which one is default with a question widget listing the real names.

If OAuth redirect fails, offer Home Assistant as the fallback using the official NavimowHA integration. Do not scrape cookies or steal a session.

When done, tell them they can say start mowing, pause, go home, or how's the battery.
