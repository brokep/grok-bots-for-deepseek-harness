---
name: bland-phone-calls
description: "Use when placing, checking, stopping, or summarizing an outbound Bland AI phone call, on first run to configure Bland (API key + voice), or when the user needs to add their own Bland voice."
---

# Bland phone calls

Part of the dial bot agent preset.

---
name: Bland phone calls
description: >-
  Use when placing, checking, stopping, or summarizing an outbound Bland AI
  phone call, on first run to configure Bland (API key + voice), or when the
  user needs to add their own Bland voice.
---
# Bland phone calls

Place and follow outbound Bland AI calls so they sound like a person, not a script.

Prefer the official Bland MCP when connected (`bland_call_send` / `bland_call_get`, or hosted `create_call` / `get_call_log`). Fall back to REST with `BLAND_API_KEY` when MCP is missing, a wait/poll loop is needed, or you need knobs MCP send does not expose (`wait_for_greeting`, `interruptibility`, `background_track`, `temperature`, `pronunciation_guide`).

Docs: https://docs.bland.ai
Send: https://docs.bland.ai/api-v1/post/calls
Speech: https://docs.bland.ai/tutorials/agent-speech
Voices: https://docs.bland.ai/tutorials/btts
Clone API: https://docs.bland.ai/api-v1/post/clone
MCP: https://docs.bland.ai/integrations/mcp/overview

## First-run configuration

Run this **before any outbound call** when Bland is not connected, the API key is missing, or the user has no saved default voice. An imported copy of this bot should run this on the first conversation, even if they have not asked to dial yet.

Do not place a call until the API key is stored and a voice is saved.

### 1. Tell them what you need

In one short message: you place calls through Bland, and you need their **API key** and a **voice** (stock name or clone UUID). Point them at:

- API key: [Bland Settings](https://app.bland.ai/dashboard/settings)
- Voices: [Voices → Studio](https://app.bland.ai/dashboard/voices?tab=studio)

Never ask them to paste the API key into chat.

### 2. Collect the API key

Send a secret-request (masked input, not chat):

- label: `Bland API key`
- connector: `Bland AI`
- field: `BLAND_API_KEY`

Wait until they submit. Then confirm adding the official Bland connector with a question widget (yes/no). After yes:

1. SearchPlugins for Bland. There is no Cursor marketplace plugin. Skip community Bland MCPs.
2. Add the official local CLI MCP with AddMcpServer:
   - name: `Bland AI`
   - command: `npx`
   - args: `["-y", "bland-cli", "mcp"]`
   - env: `{ "BLAND_API_KEY": "<their key>" }` if the key is available to pass through; otherwise add the server named `Bland AI` and rely on the secret-request field `BLAND_API_KEY`, then restart the MCP servers.
3. If the CLI server fails to load, add the official remote MCP instead:
   - name: `Bland AI`
   - url: `https://api.bland.ai/v1/mcp`
   - headers: `{ "Authorization": "Bearer <key>" }`
   Do not use AuthenticateMcpServer for Bland. It is API-key auth, not OAuth, and the OAuth card will 404.
4. Validate with a list-calls read (`bland_call_list` or `GET /v1/calls?limit=1`). 401 means the key is bad — secret-request again. If MCP stays broken, place calls via REST with `Authorization: Bearer $BLAND_API_KEY`.

### 3. Collect the voice

Ask for a voice UUID or a stock name (`maya`, `Josh`, `Florian`, `Derek`, `June`, `Nat`, `Paige`). If they have none, walk through **Add your own voice** below and wait — do not pick a random clone.

Save a profile memory: `The user's default Bland voice ID is <uuid or name>. Use it on every outbound call unless they name a different one.`

### 4. Confirm ready

One short message: Bland is connected, the voice is saved, and you will still confirm number, purpose, and talking points before any call.

## Never dial unconfirmed

A call costs money and rings a real person. Confirm number (E.164), objective, voice, and voicemail policy before sending.

Do not auto-retry the same number within 10 seconds. Do not dial emergency, DNC, or sensitive numbers.

## Voice

Use the user's saved default voice UUID if they have one. Otherwise a stock name (`maya`, `Josh`, `Florian`, `Derek`, `June`, `Nat`, `Paige`). If they have no voice yet, run **First-run configuration** / **Add your own voice** and wait. For clones, always pass the UUID, not the display name (two voices can share a name).

## Task template (fill this in every call)

Write `task` as a briefing you would give a friend before they dial. Official rules: keep it under ~2,000 characters; phrase it as instructions to the agent; say what to do instead of each don't; frame positively ("keep it casual" not "don't be formal").

```
You are calling {callee} at {place} for {user}. Sound like a normal person, not a receptionist.

Goal: {one sentence}. Success is {what to come back with}.

Facts you can use: {only what's needed}.

How to talk:
- Short sentences. Contractions. One question at a time.
- Say times like a person: "nine to seven", "eight in the morning". Never spell letters ("A M", "P M").
- When you have the answer, thank them once and hang up. Do not recap. Do not repeat the answer back unless they ask.
- If they sound busy, get the one fact and get off.

If you hit voicemail: hang up. Do not leave a message.
If they ask who you are: {identity line, e.g. "just checking hours before I stop by"}.
```

`first_sentence` (under 200 characters): one casual line, not a title. Examples: "Hey, quick question about your hours." / "Hi, is this {place}?"

Do not put any of these in the task:

- "Repeat that back to confirm"
- "Summarize the answer"
- "Thank them for their help" as a scripted closer
- "You are a customer service agent"
- A list of don'ts with no replacement

## Default send-call body

Use REST when you need these knobs. MCP `bland_call_send` only takes phone, task, voice, first_sentence, model, from.

| Field | Default | Why |
|---|---|---|
| `voice` | user's saved UUID | Clone or stock |
| `model` | `base` | Full features. `turbo` is more conversational but no transfer/tools |
| `wait_for_greeting` | true | Let them say hello first |
| `interruptibility` | `3` (easy) | Yield when they talk over you. `2` if the line is noisy |
| `background_track` | `office` | Soft room tone. `none` if they want it quiet |
| `temperature` | `0.6` | A little looseness |
| `record` | true | Needed for a recording / some post-call features |
| `max_duration` | 8 | Personal calls should be short |
| `voicemail.action` | `hangup` | Unless they asked for a message |

## Place the call

Required: `phone_number` plus `task`, `pathway_id`, or `persona_id`. Ad-hoc personal calls use `task`, not a one-off pathway.

MCP: `bland_call_send` then poll `bland_call_get` every ~10s until `completed` is true.

REST:

```bash
curl -sS -X POST https://api.bland.ai/v1/calls \
  -H "Authorization: Bearer $BLAND_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "phone_number": "+14155551234",
    "task": "<filled template>",
    "first_sentence": "Hey, quick question about your hours.",
    "voice": "<uuid or name>",
    "model": "base",
    "wait_for_greeting": true,
    "interruptibility": 3,
    "background_track": "office",
    "temperature": 0.6,
    "record": true,
    "max_duration": 8,
    "voicemail": { "action": "hangup" }
  }'
```

Then `GET /v1/calls/$CALL_ID` until done. `answered_by` can lag about a minute.

## After the call

Report: outcome (`status`, `answered_by`, `call_ended_by`), `summary`, short transcript, recording if any, `price`.

## Add your own voice

Walk the user through this when they have no default voice, or they ask how to use their own.

1. Create a Bland account and copy an API key from [Settings](https://app.bland.ai/dashboard/settings). Give it to this bot through the secure key prompt, never in chat.
2. Open [Voices → Studio](https://app.bland.ai/dashboard/voices?tab=studio).
3. **Stock voice:** pick one (`maya`, `Josh`, `Florian`, `Derek`, `June`, `Nat`, `Paige`) and tell the bot the name.
4. **Clone your own (recommended):** click New Voice. Upload one clean ~10 second WAV. One speaker, no music or room echo, at least 100 ms of silence at each end, some emotion in the delivery. Leave the engine on BTTS V3. Name it (1–30 characters, unique). The clone is private and usable immediately. New orgs get one instant clone; a $5 wallet top-up raises that cap.
5. Copy the voice UUID (from the clone response `voice_id`, or `id` on `GET /v1/voices`). Always use the UUID for clones, not the display name.
6. Tell this bot: `use this voice <uuid>`. It will use that on every call until you change it.
7. Optional: for V3 clones, `boost_language_consistency` on is fine if the call stays in the sample's language. Turn it off for code-switching. Expressiveness/stability are TTS preview controls; phone calls use the voice's stored defaults. A thin sample will not be fixed by settings — re-clone.

API alternative: `POST /v1/clone` ([docs](https://docs.bland.ai/api-v1/post/clone)) with `name` + one `audio_samples` file. Response `data.voice_id` is what you pass as `voice`.

## Auth

`Authorization: Bearer <BLAND_API_KEY>`. Key: https://app.bland.ai/dashboard/settings. Collect it with a secret-request, never chat. If Bearer 401s, retry once with the raw key. Validate with a list-calls read.

## Status and errors

`queue_status`: new → queued → allocated → started → complete. Final `status`: completed, failed, busy, no-answer, canceled, unknown.

401 bad key. 400 missing number or task. 429 same number twice in 10s. DNC / sensitive: stop. No balance: tell the user.
