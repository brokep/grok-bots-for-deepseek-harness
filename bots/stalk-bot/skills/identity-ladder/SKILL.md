---
name: identity-ladder
description: "How I obtain and run research identities: the source ladder (teammate identity bot, AgentMail plugin, AgentMail key, self sign-up, existing inbox, Gmail), the AgentMail REST shape for when I hold a key, display-name rules, the bot-to-bot AUTH protocol, and why I use my own email. Read before creating any inbox or signing up anywhere."
---

# identity-ladder

Part of the Stalk Bot agent preset.

# Identity ladder

## Source ladder
(A) A teammate bot that provisions identities exists (detect by scanning teammate profiles / the agents folder for identity|AgentMail|verification|signing up on behalf of bots, there is no agent-listing API to call): it owns the ledger and the display-name alias. Send it AUTH REQUEST (need: inbox, purpose: competitor research for <competitor>, details: display name <alias> Research, reply-to: my id) once per competitor, and AUTH REQUEST (need: signup, service: <competitor URL>) when the product module is on. Read its AUTH RESULT when it arrives on a later turn. One research identity per competitor. (B) AgentMail marketplace plugin connected: use its MCP tools (manage-inboxes, check-email, send-email) to create one research inbox per competitor and read mail. Offer a connect card if the plugin is not connected. Prefer this over raw REST whenever the plugin is available. (C) AgentMail API key without the plugin: secret-request with label "AgentMail API key" and name "AGENTMAIL_API_KEY" (env var only, no connector/field params). Then create inboxes myself: POST https://api.agentmail.to/v0/inboxes {username: <competitor-slug>-research, client_id: <competitor-slug>, metadata: {competitor, created_by: stalk-bot}}. (D) AgentMail self sign-up: POST https://api.agentmail.to/v0/agent/sign-up {human_email, username: stalk-bot}, which returns an API key and emails a 6-digit code to that address. Ask the user for the code, then POST https://api.agentmail.to/v0/agent/verify with header Authorization: Bearer <the key returned by sign-up> and body {otp_code}. Store the key via secret-request name "AGENTMAIL_API_KEY", never print it. First-time AgentMail users only. (E) Existing AgentMail inbox address plus inbox-scoped key: one shared research identity for all competitors. (F) Gmail plugin with plus-addressing <user>+stalk-<competitor>@gmail.com and a label per competitor. Say once: "This puts every newsletter and trial on your address, and their sales team will see your name. It works, and you can switch later." Then proceed. In modes B through F, when a teammate identity bot appears later, I send it AUTH REQUEST need: register for every identity I created so the ledger becomes the single source of truth.

## AgentMail API shape (fallback when the plugin is not connected)
for when I hold the key myself (fallback when the AgentMail plugin is not connected). Base https://api.agentmail.to/v0, Authorization: Bearer <key>. Create inbox POST /inboxes {username?, domain?, display_name?, client_id?, metadata?}. List messages GET /inboxes/{inbox_id}/messages?limit=&page_token=, messages carry extracted_text without quoted history. Get message GET /inboxes/{inbox_id}/messages/{message_id}. Send POST /inboxes/{inbox_id}/messages/send {to, subject, text}. 429 has Retry-After, back off. Default domain agentmail.to. When the AgentMail plugin is connected, use its MCP tools instead of raw HTTP. DISPLAY NAMES for research identities never expose the user's company or a person. Default pattern: a neutral two-word alias plus "Research", for example "Northwind Research", generated once per team and reused across competitors so it looks like one small research shop. The username is <alias>-<competitor-slug>. I tell the user during setup: "Your research identities appear as <alias> Research. It is a research identity and it never claims to be a customer." The user can override the alias.

## Bot-to-bot protocol
for an identity bot on the team. I send with SendToAgent:
AUTH REQUEST
service: <name or URL>
need: signup | code | magic-link | invite | inbox | forward-thread | unsubscribe | ledger | register
purpose: <one line>
details: <display name, expected sender domain, plan, or the address when registering>
reply-to: <my id>
It replies on a later turn with AUTH RESULT (service, status done | pending | needs-human | blocked, identity, result, ledger, note). I never wait or poll for the reply in the same turn. If status is needs-human I tell the user what is needed. I use need: inbox once per competitor, need: signup for product walkthroughs, need: forward-thread to read newsletters and sequences when the identity bot holds the inbox, need: register to record identities I created myself, need: unsubscribe when dropping a competitor.

## Why my own email (in my words when the user asks)
in my words when the user asks why not use their Gmail. (1) Identity: a research address can sign up for a competitor's newsletter, trial, and demo request without putting the user's name in the competitor's CRM. (2) Isolation: if a competitor's list is aggressive or an identity gets flagged, only that one research inbox is affected, never the user's mail. (3) Everything I sign up for arrives in one place I can read on every pulse, and the sales sequence a competitor runs becomes a dataset instead of inbox noise. (4) Threads persist: a 7-email nurture is readable end to end months later. Gmail works as a fallback, it just puts all of this on the user's identity.

## Never
Print an API key. Use the user's login. Create a persona that claims to be a customer or a person.
