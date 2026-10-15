---
name: writing-revision
description: "Draft or revise any kind of writing so it is clearer, better structured, and more effective for its audience. Use for essays, emails, memos, articles, narratives, speeches, social posts, marketing copy, personal writing, documentation, technical writing, reports, proposals, and mixed-format prose while preserving meaning and facts."
---

# Writing revision

Part of the Writing Bot agent preset.

---
name: Writing revision
description: >-
  Draft or revise any kind of writing so it is clearer, better structured, and
  more effective for its audience. Use for essays, emails, memos, articles,
  narratives, speeches, social posts, marketing copy, personal writing,
  documentation, technical writing, reports, proposals, and mixed-format prose
  while preserving meaning and facts.
---
Use this skill to improve any kind of writing while preserving the writer's intent, factual claims, audience fit, and useful voice.

## Workflow

1. Use the writing-revision reference below as the base method.
2. For technical writing, docs, changelogs, UI copy, onboarding text, help text, or product explanations, extend the base workflow with the technical writing extension below.
3. Identify the writing situation before editing:
   - format
   - audience
   - goal
   - desired tone
   - constraints or facts that must stay fixed
4. Rewrite in passes:
   - purpose and reader fit
   - structure and flow
   - paragraph shape
   - sentence clarity
   - voice, tone, and rhythm
   - final polish
5. Preserve facts, names, dates, quotes, commitments, technical terms, legal meaning, and personal details unless the user explicitly asks to change them.
6. For technical writing, apply the technical extension after the base writing pass: technical precision, executable examples, exact UI labels, identifiers, and product truth take priority over smoothness.

## Revision Rules

- Make the main point easy to find.
- Match the structure to the reader's job and the piece's purpose.
- Keep one dominant idea per paragraph or section.
- Prefer concrete language over vague abstraction.
- Improve rhythm without making the writing sound generic.
- Preserve the writer's voice when revising existing text.
- Cut filler and repeated ideas.
- Avoid em dashes. Use space-padded hyphens (` - `), colons, semicolons, commas, or sentence breaks when they fit better.
- Remove cliches, stock idioms, and familiar figures of speech unless the user explicitly wants that register.
- Add transitions only when they clarify the relationship between ideas.
- Do not make claims stronger than the source supports.
- Do not over-polish personal, emotional, or opinionated writing until it loses its human texture.
- Do not rewrite technical detail into vagueness or change commands, paths, labels, version numbers, routes, or identifiers unless they are wrong.

## Writing Revision Reference

Use this reference when drafting or revising prose across formats: essays, articles, emails, memos, reports, proposals, speeches, social posts, product copy, personal writing, stories, and documentation-adjacent text.

### Goal

Make the writing do its job for the intended reader.

Good revision is not just making sentences smoother. It clarifies the purpose, sharpens the structure, preserves what is true, and keeps the voice appropriate for the person, format, and stakes.

### Core Loop

Apply this loop until no meaningful improvement remains:

1. Identify what the piece is trying to do.
2. Identify what the reader needs in order to follow or act.
3. Rewrite structure before polishing sentences.
4. Check whether meaning, facts, and voice survived.
5. Repeat where the draft still drags, confuses, or overreaches.

### Before Writing

Name these before drafting or revising:

- Format: email, essay, memo, announcement, speech, article, proposal, report, story, social post, landing copy, docs, or mixed format
- Audience: one person, team, executives, customers, peers, public readers, experts, beginners, friends, or family
- Goal: inform, persuade, request, explain, teach, reflect, entertain, apologize, announce, summarize, decide, or sell
- Stakes: casual, professional, public, sensitive, high-trust, legal, financial, medical, or reputational
- Voice: plain, warm, formal, direct, narrative, analytical, persuasive, playful, solemn, or personal

If the user supplies a draft, preserve the underlying intent unless they ask for a stronger rewrite.

### Structure Rules

Lead with the reader's need:
- Put the main point, promise, or situation early.
- Do not hide the reason for writing behind throat-clearing.
- For requests, make the ask and deadline easy to find.
- For explanations, give the reader enough context before the hard part.
- For persuasive writing, establish the problem before the recommendation.
- For narrative writing, start with a concrete moment, tension, or image.

Give each section one job:
- Split sections that mix background, argument, instructions, and caveats.
- Merge sections that repeat the same point with different wording.
- Use headings when they help scanning, not as decoration.
- Keep heading style consistent within the piece.

Control progression. Choose the sequence that fits the task:
- Situation, then complication, then resolution for narratives, essays, and strategy memos
- Context, then ask, then details, then next step for emails and internal requests
- Problem, then evidence, then recommendation, then tradeoffs for proposals and decision memos
- Claim, then reasoning, then example, then implication for opinion pieces
- What changed, then why it matters, then what to do for announcements
- Premise, then payoff, then supporting points for social posts

### Paragraph Rules

- Give each paragraph one main idea.
- Start paragraphs with a clear point, turn, or setup.
- Put examples close to the claim they support.
- Move caveats after the main point unless the caveat changes how the reader should interpret the claim.
- Cut sentences that repeat the previous sentence without adding force, evidence, or nuance.
- Vary paragraph length deliberately: shorter for emphasis, longer for explanation.

### Sentence Rules

Use punctuation intentionally:
- Do not use em dashes.
- Use a space-padded hyphen (` - `) only when the sentence benefits from a dash-like break, interruption, or aside.
- Prefer a colon when the second part explains, expands, or names the first part.
- Prefer a semicolon when joining two independent but closely related clauses.
- Prefer a comma or a new sentence when the relationship is simple.
- Do not use punctuation to create drama where clearer syntax would do more work.

Prefer actors and actions:
- Make it clear who is doing what.
- Replace abstract noun-heavy phrasing with verbs.
- Prefer `We decided to delay the launch` over `A decision was made regarding launch timing`.

Reduce drag:
- Cut filler openings: "I just wanted to", "It is important to note that", "In order to", "At the end of the day".
- Move long context out of the way of the main verb.
- Break sentences that carry two unrelated ideas.

Be concrete:
- Replace vague claims with observable details.
- Use examples, numbers, names, scenes, or consequences when they matter.
- Avoid generic intensifiers when a specific fact would do more work.
- Remove cliches, stock idioms, and familiar figures of speech. Replace them with the actual claim, image, detail, or consequence.
- Do not use phrases like "at the end of the day," "game changer," "low-hanging fruit," "silver bullet," "move the needle," "crystal clear," or "unlock value" unless quoting or intentionally matching a known voice.

Keep rhythm human:
- Preserve useful sentence fragments in casual or narrative formats.
- Do not flatten every sentence into the same length.
- Keep distinctive phrasing when it carries personality and does not confuse meaning.

### Voice and Tone

Voice should fit the writer. Tone should fit the situation.

When revising existing text:
- Keep the writer's point of view.
- Keep intentional directness, warmth, humor, restraint, or emotion.
- Do not replace specific phrasing with generic professional polish.
- Smooth awkward wording without erasing personality.

Adjust tone to stakes:
- Use direct, plain language for high-stakes communication.
- Use warmth for personal or relational writing without adding sentimentality.
- Use confidence for persuasive writing without overstating certainty.
- Use restraint for apologies, sensitive updates, or conflict.
- Use energy for announcements without hype.

### Format Guidance

Emails:
- Put the point or ask early.
- Make deadlines, decisions, and requested actions unmistakable.
- Keep background short unless the reader needs it to say yes or act.
- End with a clear next step.

Memos and reports:
- Start with the conclusion, recommendation, or executive summary when readers need fast orientation.
- Separate facts, interpretation, and recommendations.
- Make assumptions and tradeoffs explicit.
- Use bullets and tables only when they make comparison easier.

Essays and articles:
- Build around one dominant idea.
- Use examples before broad abstractions when possible.
- Make each section advance the argument.
- End with a useful implication, not a slogan.

Speeches and scripts:
- Favor spoken clarity over written density.
- Use shorter sentences and visible transitions.
- Repeat key phrases only when repetition adds rhythm or emphasis.
- Read aloud mentally and remove tongue-twisters.

Social posts:
- Open with a concrete observation, claim, or tension.
- Keep one main point per post.
- Cut setup that delays the payoff.
- Avoid engagement-bait phrasing unless explicitly requested.

Marketing and product copy:
- Say what the reader can do, get, avoid, or understand.
- Prefer specific benefits over abstract adjectives.
- Keep claims supportable.
- Make calls to action concrete.

Personal writing:
- Preserve emotional truth and specificity.
- Do not over-organize until the piece feels corporate.
- Keep details that make the experience believable.
- Remove explanation only when the moment already carries the meaning.

### Fact and Meaning Safety

- Do not invent facts, quotes, credentials, dates, metrics, sources, or personal experiences.
- Do not change the level of certainty unless the source supports it.
- Keep names, titles, commitments, deadlines, numbers, and legal or policy wording stable.
- Flag factual gaps instead of smoothing over them.
- For legal, medical, financial, or HR-sensitive writing, prioritize precision and risk reduction over style.

### Orwell Pass

Use Orwell's questions and rules as a diagnostic pass, not as a mechanical style overlay. They are useful when a sentence feels vague, inflated, stale, or needlessly ornate.

Ask:
- What is this sentence trying to say?
- Which words say it most directly?
- Would an image or idiom clarify the idea?
- If using an image or idiom, is it fresh enough to help?
- Can the sentence be shorter without losing meaning?
- Is anything in the sentence avoidably awkward, ugly, or inflated?

Apply the rules with judgment:
- Cut stale metaphors, similes, idioms, and figures of speech.
- Prefer short, plain words when they carry the same meaning.
- Remove words that do not add meaning, rhythm, emphasis, or necessary precision.
- Prefer active voice when it makes the actor and action clearer.
- Avoid foreign phrases, jargon, and specialized terms when everyday English is equally precise.
- Break any rule before producing a sentence that is false, awkward, needlessly blunt, or hostile to the writer's real purpose.

### Revision Modes

Light edit, when the draft is close:
- Fix awkward sentences.
- Tighten repetition.
- Improve transitions.
- Preserve structure and voice.

Strong rewrite, when the draft has the right ideas but weak execution:
- Reorder for reader comprehension.
- Rewrite paragraphs and sentences freely.
- Keep facts, intent, and voice.
- Add missing connective tissue where needed.

Transform, when changing format:
- Identify what must survive from the source.
- Rebuild for the new audience and channel.
- Drop details that do not serve the new format.
- Preserve claims and constraints.

### Failure Modes to Avoid

- Making everything sound like generic business writing
- Preserving sentence order when the structure is the real problem
- Strengthening claims without evidence
- Cutting caveats that protect the meaning
- Adding fake warmth, fake urgency, or fake certainty
- Turning a personal piece into a polished announcement
- Overusing headings, bullets, and bold text
- Making the opening clever but unclear
- Letting rhythm improvements weaken precision

### Quick Checklist

- Is the purpose clear in the first few lines?
- Does the structure match the reader's job?
- Does each paragraph have one job?
- Are the strongest ideas easy to find?
- Are claims, facts, and commitments preserved?
- Does the tone fit the audience and stakes?
- Does the piece avoid em dashes, cliches, and stock idioms?
- Did the Orwell pass catch stale images, needless words, or inflated phrasing without flattening the voice?
- Does the revision sound like a better version of the writer, not a different writer?
- Is the final version shorter, clearer, or more useful in a way the reader will feel?

## Technical Writing Extension

Use this as an extension of the writing-revision reference when the writing is technical: docs, product copy, changelog entries, tutorials, onboarding text, help text, UI copy, technical blog posts, and product explanations.

Do not treat this as a separate revision workflow. Start with the normal writing-revision loop, then apply these extra constraints so clarity does not weaken technical meaning.

### Extra Goal

Make technical writing easy to understand without making it less true.

A technically precise sentence that reads awkwardly should be improved. A smooth sentence that weakens behavior, constraints, or product truth should be rejected.

### Technical Extension Pass

After the base structure, paragraph, and sentence passes:

1. Check whether the revised text preserves system behavior, constraints, and caveats.
2. Check whether commands, identifiers, paths, labels, fields, version numbers, routes, and examples stayed exact.
3. Move prerequisites before steps that depend on them.
4. Put expected outcomes near the actions that produce them.
5. Make examples executable and formatting scannable.

### Preserve Technical Meaning

- Do not simplify away constraints, caveats, edge cases, or system behavior.
- Keep exact names for commands, routes, environment variables, UI labels, files, branches, configuration keys, and API fields.
- Verify before changing product claims, version references, capability statements, or compatibility notes.
- Keep code blocks, commands, JSON, and shell snippets exact unless you are fixing them.
- Do not replace precise technical terms with softer but less accurate language.

### Surface Task-Critical Details

- Put prerequisites before dependent steps.
- Put the expected outcome near the action that produces it.
- State scope and limits explicitly when a reader could misapply the instruction.
- Explain why a step matters when it prevents a likely failure.
- Use imperative phrasing for procedures.

### Technical Structure

- Make the first screen answer the reader's immediate question.
- For docs pages, surface task, concept, or feature scope early.
- For changelog entries, separate improvements from fixes and keep bullets specific.
- For technical blog posts, preserve voice while keeping claims concrete and readable.
- If a page gives steps, make the sequence obvious.
- If a page describes options, organize by concept or field rather than loose narrative flow.

### Formatting Rules

- Keep titles short and descriptive.
- Use headings to break long pages into scan-friendly chunks.
- Use numbered lists for sequences and bullets for unordered facts.
- Wrap commands, env vars, paths, filenames, route segments, and code identifiers in backticks.
- Use fenced code blocks with the correct language when possible.
- Keep link text descriptive enough to scan out of context.
- Use tables only when they make comparison easier.

### UI Copy

- Keep labels short.
- Make buttons and empty states action-oriented.
- Put the most important word early.
- Avoid internal jargon unless users already see it in the product.
- Preserve exact UI labels when referring to existing product surfaces.

### Technical Failure Modes To Avoid

- Turning reference or procedural writing into marketing copy
- Hiding the actor in abstract language
- Burying the action in nouns
- Front-loading too much context before the main point
- Mixing unrelated goals in the same paragraph or section
- Ending sentences on weak, empty, or generic words
- Replacing precise terms with vague reader-friendly wording
- Over-formatting simple content

### Technical Checklist

- Can a reader identify who does what on the first pass?
- Are prerequisites and constraints in the right place?
- Are commands, paths, labels, identifiers, and examples preserved exactly?
- Is the revised text more direct without losing technical meaning?
- Is formatting helping the reader scan, not decorating the page?
