---
name: pptx-compat
description: "Makes every generated pptx open cleanly in PowerPoint and import into Google Slides by round-tripping it through LibreOffice and checking the result before delivery."
---

# pptx-compat

Part of the EBR & Value Deck Builder agent preset.

# pptx-compat

## Why this exists

A deck generated with python-pptx can render correctly in LibreOffice and still trigger PowerPoint's repair dialog or fail to import into Google Slides. It happens often enough to be worth its own step, and the owner finds out in front of the customer if it is skipped. Run this on every deck before handing it over.

## Steps

1. Generate the deck with python-pptx as usual and save it.
2. Round-trip: convert the saved file through LibreOffice headless to pptx again (`soffice --headless --convert-to pptx --outdir <dir> <file>`). Use the converted file as the deliverable.
3. Verify: reopen the converted file with python-pptx and check the slide count, that every slide has its title, and that images and charts are still present. Render the first and last slide to PNG and look at them.
4. If the customer uses Google Slides, say in the delivery note that the file imports via File, Import slides, and that charts arrive as images if native chart import fails.
5. Deliver the converted pptx, and a PDF export from the same LibreOffice run when the owner asked for one.

## Rules

- Never deliver the pre-round-trip file.
- If LibreOffice is unavailable, say so plainly and deliver the raw pptx with a warning about PowerPoint's repair dialog rather than silently skipping the step.
- Keep the fonts from the brand kit; substitute only when a font is missing on the machine and say which one was swapped.
