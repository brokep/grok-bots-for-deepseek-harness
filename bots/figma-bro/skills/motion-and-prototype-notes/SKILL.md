---
name: motion-and-prototype-notes
description: "Use when a screen has movement to spec or review: prototype interactions, transitions, easing and duration, gesture behavior, or motion going to an engineer."
---

# Motion and prototype notes

Part of the figma bro agent preset.

Inputs: a prototype flow in a connected file, a screen recording, or a description of what should move.

1. Read the prototype: the flows, the starting frame, and each interaction with its trigger (click, drag, hover, after delay), destination, transition type, easing, and duration.
2. Write each interaction as one row: from, trigger, to, transition, easing, duration, and in one clause what the user should feel.
3. Translate into their stack. CSS gets the transition property and the cubic-bezier, Framer Motion gets the animate and transition props, Reanimated and SwiftUI get their own spring and duration terms. Give numbers, not adjectives.
4. Check consistency: durations that should match and don't, three easing curves doing one job, and transitions that contradict the direction of the navigation.
5. Flag what will jank: animating width, height, top, or left instead of transform and opacity, animating a long list, and layout shift mid-transition.
6. Cover what a prototype cannot show: what happens when a user taps mid-animation, what reduced motion should do, and the loading state a real network introduces.
7. Missing motion: name the transitions the screen needs and does not have, as questions rather than inventions.

Output: the interaction table, the stack translation, the consistency and jank findings, the reduced-motion line, and numbered open questions.

Fallback: with only a recording, time the transitions from the video, label every number measured, and say the file holds the exact ones.

Save under design handoff.
