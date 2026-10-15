---
name: flow-critique
description: "Use when the user hands you two or more screens in sequence, like signup, onboarding, or checkout, and wants the whole path reviewed."
---

# Flow critique

Part of the Critiquito: Design Critique agent preset.

Inputs: the screens in order, and the goal the person is trying to reach by the end. Ask for the order when it is unclear.

1. Write the path in one line: the step names and the count. The count is often the finding.
2. Per step, note what the user has to know, decide, or type before they can move on.
3. Look for the path problems a single screen review misses: something asked before the user sees why it matters, the same information asked twice, a decision with no way to change it later, a dead end with no way back, no sense of progress or length, and anything that shifts between steps such as button position, labels, or type scale.
4. Name the step most likely to lose people and say what makes it the one.
5. Run the seven passes from Screen critique on that step only, unless they asked for all of them.
6. Say what you would cut. Most flows carry a step that can be deferred or dropped.

Output shape:
- The path: one line, steps and count.
- Where you lose people: the step, and why.
- Per step: findings with severity, or "nothing material" for the clean ones.
- Cut or defer: the steps that do not need to be here.
- Fix first: the three changes with the most effect on finishing the flow.

Never guess at a step you were not shown. Name the missing steps and review what you have.

Save the flow critique and one open fix list per screen under design critiques.
