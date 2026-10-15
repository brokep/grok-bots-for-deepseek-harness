---
name: clip-captions-and-post-copy
description: "Use when the user wants a title, a caption, or post text to go with a clip they are about to publish."
---

# Clip captions and post copy

Part of the Clip Bot agent preset.

Inputs: the clip, its transcript lines, the platform, and who the audience is.

1. Read the actual transcript of the clip. Every claim in the copy has to be something the speaker said.
2. Write per platform, in the user's voice when you have samples of it:
   - Short vertical platforms: one hook line under 60 characters, plus 3 to 5 tags.
   - LinkedIn: two to four sentences, the point first, no hashtag pile.
   - X: one or two sentences with the quote doing the work.
   - Newsletter or blog embed: two sentences of setup and the timestamp.
3. Offer two options per platform, one leading with the quote and one leading with the claim. Let them pick.
4. Credit the speaker and name the source, the show or talk and the date, on anything that quotes a person.
5. Never sharpen a quote. Trim from the ends, never from the middle, and keep the speaker's words.

Output: the copy in chat ready to paste, filed with the clip.

Fallbacks: no platform named means write the LinkedIn and short-vertical versions and ask which one they want more of.

You never post. The copy goes to the user and they publish it. Save with the clip in the clip library.
