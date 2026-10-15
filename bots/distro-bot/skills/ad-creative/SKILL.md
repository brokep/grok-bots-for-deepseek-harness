---
name: ad-creative
description: "Use to write ad or post copy and make images or video on the user's key."
---

# ad-creative

Part of the Distro Bot agent preset.

# ad-creative

Copy, images, and video for ads and posts, built from what already won.

## Brief

distro.py playbook, the past ads in <home>/accounts, <home>/positioning.md, and the platform's specs first. One angle per ad: the hook, the claim and its proof, the offer, the call to action. 3 to 5 variants that differ in one thing (hook, visual, or offer), so the test reads.

## Copy

Platform lengths: Meta primary text near 125 characters and headlines near 40, Google headlines 30 and descriptions 90, X 280. Voice from the voice teammate's guide (asked for once with SendToAgent, priority true, kept in <home>/voice.md), else the playbook's voice lines. Before showing: every number has a source, no testimonial or customer name without permission, no competitor named, nothing the product can't do today, and nothing ad rules ban (health, money, or personal-attribute claims, before and after).

## Images and video

Provider from distro.py status (media). No key saved: a secret-request card, FAL_KEY (fal.ai/dashboard/keys), HF_KEY as KEY_ID:KEY_SECRET (console.higgsfield.ai), or XAI_API_KEY (console.x.ai). Price first with distro.py fal price <endpoint>, higgs price <model>, or grok price, and ask above creative_cap.
- FAL: distro.py fal run <endpoint> --input <json> (fal-ai/nano-banana-pro for stills, openai/gpt-image-2 for exact text, Kling or Seedance for motion). Inputs: WebFetch fal.ai/models/<endpoint>/llms.txt.
- Higgsfield: distro.py higgs run <model> --input <json> (SOUL 2 stills, Seedance motion).
- Grok Imagine: distro.py grok image "<prompt>" --aspect 4:5, or grok video "<prompt>" --image <start frame>.
A pending job prints its resume command. distro.py sizes <file> --for <platforms> then cuts each placement. Product shots start from real screenshots. FAL and Higgsfield uploads become public links, so never upload private data. No key: the copy plus a one-paragraph image brief.

## Deliver

One SendToUser text with the images (video as an attachment): each variant's copy, the hypothesis it tests, and the cost, saved under <home>/media. Launching is campaign-loop's job.
