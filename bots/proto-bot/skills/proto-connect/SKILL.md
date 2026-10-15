---
name: proto-connect
description: "Use at setup, when the user adds a tool, or when a connection fails: GitHub, the cloud agent build check and model, the FAL, Higgsfield, or xAI key, and the Figma, Slack, and X connect cards."
---

# proto-connect

Part of the Proto Bot agent preset.

# proto-connect

## GitHub

No GitHub tools, or GetMcpServerStatus shows cursor-github needsAuth: RequestScmConnect, intent connect. A repo Cursor cannot reach: intent access with that repo. Still no GitHub tools: proto-codebase maps the code through CloudAgent.

## Builds

Run CloudAgent models. claude-opus-5-5 offered: "Builds run on Claude Opus 5.5. Want another model?", then proto.py set build_model <their pick>. Not offered: leave build_model empty so their Cursor default runs, and say so. CloudAgent missing or failing: builds come back as a prompt file for any coding agent.

## Media

FAL picked: proto.py fal price fal-ai/nano-banana-pro. Higgsfield: proto.py higgs price. Grok Imagine: proto.py grok price. No key: send the secret-request it names, with its line, then rerun. Then proto.py set media fal, higgs, or grok, the first of their picks in that order. 401: new key. 402 or 403: add credits. None picked: offer Grok Imagine once.

## Connectors

Figma, Slack, and X are connect cards: offer each with a question widget, never install without a yes. Other tools they name: SearchPlugins, same offer.

## Never

Take a key any way but a secret-request card, print one, or put one in a brief, file, or message. Retry a failing key in a loop.
