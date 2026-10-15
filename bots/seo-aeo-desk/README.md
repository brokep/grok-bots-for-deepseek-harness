# SEO & AEO Desk
Turns your keywords into content ideas and writer-ready briefs for search and AI answers. Works from a pasted keyword list or your Search Console.
Converted from the Grok Bot marketplace template by Adam Tanguay (@adamta): https://x.ai/bot/marketplace/bots/seo-aeo-desk

## Install
From the Plugins > Discover tab after adding the market index, or from a shell:
```
npx -y @deepseek-ai/dsh plugin --profile web add "git+https://github.com/brokep/grok-bots-for-deepseek-harness.git#main&path:/bots/seo-aeo-desk"
```

Then start a session and pick **SEO & AEO Desk** in the preset selector. The bot's 7 skills come with the bundle.

## Routines

Enable Plugins > Official > Automation tasks, then paste `setup-prompt.md` into the session once.
- **Content ideas digest**: Once a week, 3 to 5 new page ideas pulled from the keyword source and Search Console, ranked, with the top pick ready to brief.
- **Weekly search report**: Every Monday morning, what moved in Search Console last week, why, and the two to four things worth doing about it.
- **Topic watch**: Each weekday morning, speaks up only when a new question or topic worth a page shows up in the user's space.

## Integrations the original bot used
- notion-workspace: Keep the ideas board, briefs, and question map where your team already writes.
- slack: Post the weekly search report and topic watch to a channel you choose.
- linear: File each brief as a ticket on your content backlog so writers pick it up in the queue.
- hex: Query your warehouse to tie organic pages back to signups and closed deals.
- Profound: Read prompt volumes and AI answer visibility for the topics on your board.
- Google Sheets: Read and write Google Sheets.
