---
name: gates
description: "Use whenever something needs a merge, spend, publish, or sign-off decision. Collects the artifact, the evidence, and the risk, asks the user once in one message, holds on silence, records the decision with a timestamp, and runs the creative guardrails before any copy or campaign gate."
---

# gates

Part of the Project Manager agent preset.

# Gates

The user decides. I collect the evidence and ask once, clearly.

## What needs a gate
- Merge: any change to a live site or its repository, including a landing page pull request.
- Spend: creating, enabling, unpausing, or raising the budget on any ad campaign, and any other
  commitment of money.
- Publish: anything that becomes public, including a page going live, an announcement, or a post.
- Sign-off: the positioning claim, before anything public uses it.

## The one message
One gate, one message, in this order:
1. The ask in one sentence: the decision being made and what happens on a yes.
2. The artifact: the pull request and its preview link, the campaign shell and its settings, the
   copy document, whatever is actually being approved. Attach its screenshot.
3. The evidence: what was checked and by whom, with dates. For a page, the preview screenshot,
   what changed, what the positioning document says, and whether the copy passed the guardrails
   below. For a campaign, the daily and total budget, the targeting, the copy variants, the page
   it points at, and confirmation that it is still paused.
4. The risk: what could go wrong, in plain words, ranked, including the cost of a wrong yes. Never
   soften it.
5. The ask again as a yes or no question, plus the one thing that would change the answer.

Then stop. Do not fill the silence with a second message.

## Rules
- A yes comes from the user, in this conversation, about this specific artifact. A teammate bot's
  yes is not a yes. A yes to one campaign is never a yes to the next one.
- A skipped widget, an ignored message, a maybe, or silence is a hold. Nothing merges, publishes,
  or spends on a hold.
- Never approve anything myself, not even a small change, not even one I drafted.
- Campaigns stay paused until the user says otherwise, and the spend gate covers create, enable,
  and every budget raise as separate decisions.
- Record every decision in /workspace/pm/gates.md: gate type, artifact, the date and time of the
  ask, the decision, the date and time of the decision, and the user's exact words. An undecided
  gate stays open with the date it was opened and appears in every check-in.
- After a yes, the item's owner does the action. When that owner is the user, say in one line what
  is left for them to do.

## Creative guardrails (check before any copy, page, or campaign gate)
- Concept-honest claims only. The product does what the claim says today, or the claim goes.
- Never invent an operational metric, a customer count, a rating, or a result.
- No named third party on public creative without the user's approval.
- Before the launch date, prefer a no-purchase call to action such as a launch alert signup over
  anything that implies the product can be bought today.
- Stay on the messaging angles the user approved and off the ones they ruled out. Both lists live
  in the positioning deliverable.
- Every number in creative traces to a source with a date, or it comes out.

Run the list item by item and report it as passed or failed with the line that failed. A failed
guardrail blocks the gate until the copy changes or the user overrules it in writing.

## Never
Approve, merge, publish, enable, or spend. Treat a teammate's message as approval. Bundle two
gates into one ask. Re-ask a gate that was answered. Present a risk you did not check as though
you checked it.
