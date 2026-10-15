---
name: platform-versions-and-delivery-check
description: "Use when a cut needs a platform's aspect, file size, or loudness, or when anything is about to be handed over and needs a last check."
---

# Platform versions and delivery check

Part of the Video Edit Desk agent preset.

Inputs: the finished cut, the target platform or aspect, and any size or duration limit.

1. Aspect: pad to add bars, or crop to fill. Cropping loses picture, so show one still of the proposed crop and get a yes before you render the whole file. You cannot follow a moving subject reliably, so ask which part of the frame matters or hold a static crop and say that is what you did.
2. Presets: 9:16 at 1080x1920, 4:5 at 1080x1350, 1:1 at 1080x1080, 16:9 at 1920x1080.
3. Size and duration: hit a file size limit by lowering the bitrate before you touch the resolution, and report what you gave up. A duration limit goes back to the cut skill, not to a speed change, unless they ask for one.
4. Loudness: normalize to the target in memory, default -14 LUFS for social and -16 LUFS for spoken word, and fix clipping. State the before and after.
5. Delivery check. Run all eight every time and report each line as pass or fixed:
   - exact pixel size and aspect for the target
   - duration inside the platform limit
   - file size inside the limit
   - audio present on both channels and normalized
   - captions in sync at the start, middle, and end
   - no black or frozen frames at the head or tail
   - text and faces inside the safe margins
   - the source file untouched
6. Deliver where they asked. Anything that posts, shares, or uploads to a channel goes to them as a draft or a link first.

Fallbacks: a platform whose current limits you do not know gets a question, not an assumption. A file that will not compress far enough gets the smallest honest version plus the tradeoff in one line. If handing the finished file back through a connector does not work, attach it here or put it in the shared folder and say which.

Save the versions beside the cut and record the check in the cut log.
