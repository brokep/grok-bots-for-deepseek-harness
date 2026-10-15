---
name: routine-weekly-deep-dive
description: "Scheduled routine: Disabled by default. Friday 10am, one competitor in rotation. Re-walks the product on video, re-runs the feature test pass, diffs against the previous teardown, and delivers a self-contained HTML report. Report only."
---

# Weekly deep dive

Part of the Stalk Bot agent preset.

Schedule, as written by the template author: Disabled by default. Friday 10am, one competitor in rotation. Re-walks the product on video, re-runs the feature test pass, diffs against the previous teardown, and delivers a self-contained HTML report. Report only.

## What to do on each run

# Weekly deep dive

This routine ships disabled. Confirm the user wants a weekly rotation and the timezone before enabling.

When enabled:
1. Read memory for the competitor list and the last deep-dived competitor. Pick the next one in order.
2. If the product module is on for it and a research identity exists: run walk-the-product again in full (onboarding video, feature test pass with clips, screenshots), diff against the previous teardown, and write what changed in the product itself (new screens, new or removed features, moved gates, new integrations).
3. If the product module is off: refresh the feature inventory from docs and changelog instead.
4. Build the HTML report (html-report) and deliver it in the saved destination with 5 lines, the onboarding video, and up to 8 screenshots of what changed. If nothing in the product changed, one line and no report.
5. Save which competitor was covered.

Fires on:
- cron `0 10 * * 5`

Ask the importing user for:
- Timezone
