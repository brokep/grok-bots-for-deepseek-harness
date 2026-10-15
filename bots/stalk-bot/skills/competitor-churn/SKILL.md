---
name: competitor-churn
description: "Opt-in module. Detect the user's customers lost to a watched competitor from a source they name, attribute the competitor, write a facts brief, and hand the winback body to the user's writing bot or a marked skeleton. Use when the churn module is on, when the churn watch routine fires, or when the user says they lost a customer."
---

# competitor-churn

Part of the Stalk Bot agent preset.

# Competitor churn

Winbacks go to the user's own churned customers only. This is the one module that touches customers, and it never sends.

## Turn on (one ask, only when the user brings it up or enables the module)
Ask once: "Where does closed-lost live? A CRM with a closed-lost reason or competitor field, a sheet, or paste me the cases." Save the source as a CHURN SOURCE line in memory (source, field names, read cadence). If the user names a writing bot or voice skill for customer email, save it as WINBACK WRITER. If no source is given, the module stays off and nothing runs.

## Detect
1. Read the source since the last watermark. A case is a customer marked closed-lost, canceled, or downgraded to zero with a competitor named, or with a reason text that names a watched competitor or their product.
2. Attribute: the named competitor wins. If the reason text names none, look for the competitor's product in the customer's public footprint (their site footer, job posts, X posts) and mark the attribution "inferred," never "confirmed."
3. Skip cases already in /workspace/dossiers/_us/churn/index.md.

## Facts brief (I write this)
/workspace/dossiers/_us/churn/<date>-<customer-slug>.md with: customer, plan or contract they had, date lost, competitor, attribution confidence, the reason in their words if any, what the competitor offers that we do not (from the dossier, with links), what we offer that they do not (from the baseline), three talking points for a winback, one thing not to say. Every claim carries a link and a date.

## Winback body (I do not write customer-facing copy)
- If WINBACK WRITER is set: hand the brief to it with the ask "why-did-you-leave note plus one offer, in the user's voice, from the user." Present its draft unchanged.
- If not set: deliver a skeleton with the three talking points as placeholders in brackets, marked "skeleton, rewrite in your voice before sending."
- Sign-off and from address are always the user. Never an invented signer, never the research identity.
- Save the draft next to the brief. Never send, never schedule a send, never add the customer to any list.

## Feed back
Add the competitor's winning reasons to the dossier's against-us notes and to the next pulse's Proactive suggestions as a theme ("lost <customer> to <competitor> over <reason>").

## Deliver
One line per case in chat: customer, competitor, confidence, brief path, winback status (draft from writer, skeleton, or pending). Cap 5 per run, then "N more in churn/index.md."

## Never
Contact the churned customer myself. Contact the competitor. Use the research identity for anything here. Guess at a reason and present it as theirs. Run this module without a named source.
