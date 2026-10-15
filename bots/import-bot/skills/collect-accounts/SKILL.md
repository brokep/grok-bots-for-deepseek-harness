---
name: collect-accounts
description: "use this for the account side: ranked fastest-first pulls of ChatGPT and Claude conversations, projects, and memories, with one sign-in at most and the official exports as the durable copy"
---

# collect-accounts

Part of the Import Bot agent preset.

# Collect accounts

The account side of the dual approach. ChatGPT keeps nothing on disk, and claude.ai holds chat projects, account memory, and conversations that Cowork's local files do not. For each service there is a ladder of methods, fastest and most complete first. Take the first rung that works and fall to the next only when it fails. Never read conversations one at a time in the browser. The browser is for one sign-in and for the three or four pages that have no request behind them.

Everything lands under `/workspace/migration/raw/accounts/<service>/` in the shapes parse-import reads. Never block the plan on an export email, fold it in when it lands.

## Already pulled?

Check `/workspace/migration/raw/accounts/<service>/` first. Files under 24 hours old mean that pull is done. A signed-in browser session from earlier needs no hand-off. Only what is missing gets asked for.

## The one sign-in

When a rung needs the browser, open the service's sign-in page and first tell the user why, in chat, in this shape:

"Next, sign in to <ChatGPT or Claude> in my browser. It is the only way to get your <memories, custom instructions, projects, and conversations>, because nothing on your computer holds them. Finish the sign-in, including any code they text you, then hand the window back."

Then call `request_box_help` once per service with one short instruction, like "Sign in to ChatGPT, then hand the box back." Your turn ends there and resumes on its own when they hand the box back, so nothing else runs meanwhile. Ask while the user is still at the screen approving cards, not after they have walked away. When you resume, take a Screenshot to confirm the signed-in page (name or avatar visible) and add one line to `/workspace/migration/state.md` under "Accounts": "<service>, <account name or email>, signed in <date>, read only." The Import state fact picks it up at the end. Being signed in is never permission to change anything there. Every number and note that comes from a service is labeled where it lands: `live <service> <date>` for pulls from the signed-in session or a token, `export <file> <date>` for official exports.

Hand-off back without a session: one retry offer ("The sign-in did not finish. Without it I skip your <service> memories and conversations. Want to try again?"), then "waiting on" in the receipt. Never ask for a password in chat. Credentials offered anyway are used once in the browser and never written anywhere.

## Running a page script

Once signed in, the bulk pulls are one script each, run in the page with `browser_cdp`: method `Runtime.evaluate`, params `{"expression": <the script text>, "awaitPromise": false}`. Always pass `awaitPromise: false`: without it the call waits for the whole pull, times out, and the timeout stops the page. The script keeps running in the page. Poll every few seconds with `Runtime.evaluate` and `{"expression": "JSON.stringify(window.__gb)"}` for `phase`, `pulled`, `done`. When `done` is true, fetch the bundle the same way with `JSON.stringify(window.__gbBundle)`. A result over 20k characters is saved to a file under `/workspace/browser-cdp/` and the tool returns its `outputFile`. That file holds the whole CDP reply, so unwrap it into the accounts folder:

```bash
python3 -c 'import json,sys; open(sys.argv[2],"w").write(json.load(open(sys.argv[1]))["result"]["value"])' "<outputFile>" "/workspace/migration/raw/accounts/<service>/<service>-pull-<date>.json"
```

If that fails, the script also downloaded the bundle: `find / -name '<service>-pull-*.json' -mmin -30 2>/dev/null | head -1`, then move it to the same folder. parse-import splits the bundle into one file per conversation.

## ChatGPT

**Conversations, in order:**

1. **Codex sign-in on the user's computer, no browser.** The inventory printed `chatgpt login yes` when `~/.codex/auth.json` holds a ChatGPT login. Run the pull script there (macOS and Linux below, Windows the same way collect-local runs its script). The token stays on their computer, only conversation JSON comes back. Then `CopyToBox` the printed archive (same machineId) to `/workspace/migration/accounts-chatgpt.tgz` and extract it into `/workspace/migration/raw/accounts/chatgpt/`. Say to the user only: "Pulling your ChatGPT conversations through your Codex sign-in, no need to log in again." Status `no codex login` or `not a chatgpt account` or `list rejected`: go to rung 2.
2. **Page script after one sign-in.** Run the chatgpt.com page script below in the signed-in page, as "Running a page script" describes. Three hundred conversations take a few minutes.
3. **Official export.** Settings, Data controls, Export data, Confirm. Complete, arrives by email, usually within the hour. Always kick it off after rung 1 or 2 too, as the durable copy. "OpenAI emails you a download link. Paste it here when it lands, or connect Gmail to me and I fetch it myself and disconnect after." On yes, SearchPlugins for Gmail, InstallPlugin, check on the resync. Extract `conversations.json` to `accounts/chatgpt/export/`.
4. Nothing else. Do not click through conversations.

**Memories and custom instructions** (the export does not include them, so this is the only source): Settings, Personalization, Manage memories, copy every entry verbatim to `memories.md`. Custom instructions come from the page script when it works, else Settings, Personalization, Custom instructions, to `custom-instructions.md`. Two pages, once.

**Projects and GPTs:** the Projects list (name, chat count, instructions when shown) to `projects.md`, My GPTs (name, description, instructions when the editor opens) to `gpts.md`. Two pages, once.

### ChatGPT pull through the Codex sign-in, macOS and Linux (one Shell call with the machineId)

```bash
A="${CODEX_HOME:-$HOME/.codex}/auth.json"; T="${TMPDIR:-/tmp}/grokbot-import/chatgpt"; mkdir -p "$T/conversations"; OUT="${TMPDIR:-/tmp}/grokbot-import/chatgpt-conversations.tgz"
[ -f "$A" ] || { echo "status: no codex login"; exit 0; }
grep -q '"auth_mode": *"chatgpt"' "$A" || { echo "status: codex login is not a chatgpt account"; exit 0; }
if command -v python3 >/dev/null 2>&1 && [ -x "$(command -v python3)" ] && python3 -c 'import json' 2>/dev/null; then read -r TOK ACC < <(python3 -c 'import json,sys;o=json.load(open(sys.argv[1]));t=o.get("tokens") or {};print(t.get("access_token") or "-", t.get("account_id") or "-")' "$A")
elif command -v osascript >/dev/null 2>&1; then read -r TOK ACC < <(osascript -l JavaScript -e 'ObjC.import("Foundation");var o=JSON.parse(ObjC.unwrap($.NSString.stringWithContentsOfFileEncodingError("'"$A"'",4,null)));var t=o.tokens||{};(t.access_token||"-")+" "+(t.account_id||"-")')
elif command -v jq >/dev/null 2>&1; then read -r TOK ACC < <(jq -r '[(.tokens.access_token // "-"), (.tokens.account_id // "-")] | join(" ")' "$A")
else echo "status: no json tool"; exit 0; fi
[ "$TOK" != "-" ] && [ -n "$TOK" ] || { echo "status: no chatgpt token"; exit 0; }
H1="Authorization: Bearer $TOK"; H2="ChatGPT-Account-ID: $ACC"; UA="User-Agent: Mozilla/5.0"
n=0; off=0; status="ok"
while [ "$off" -lt 300 ]; do
  page=$(curl -sS -m 30 -H "$H1" -H "$H2" -H "$UA" "https://chatgpt.com/backend-api/conversations?offset=$off&limit=100&order=updated") || { status="list request failed"; break; }
  echo "$page" | grep -q '"items"' || { status="list rejected: $(echo "$page" | tr -d '\n' | head -c 160)"; break; }
  ids=$(echo "$page" | grep -oE '"id": *"[0-9a-fA-F-]{36}"' | grep -oE '[0-9a-fA-F-]{36}' | awk '!seen[$0]++')
  [ -n "$ids" ] || break
  for id in $ids; do
    curl -sS -m 30 -H "$H1" -H "$H2" -H "$UA" "https://chatgpt.com/backend-api/conversation/$id" -o "$T/conversations/$id.json" && n=$((n+1))
    sleep 0.3
  done
  off=$((off+100))
done
( cd "$T" && COPYFILE_DISABLE=1 tar -czf "$OUT" conversations )
echo "status: $status"; echo "conversations: $n"; echo "archive: $OUT"
```

### Windows

Copy `pull-chatgpt-codex.ps1` out of the import-scripts skill, then place it with CopyFromBox and run it by file, the same way collect-local runs the Windows collector.

### Page script, run inside the signed-in chatgpt.com page

```javascript
// Bulk pull of a signed-in chatgpt.com account, run inside the page (the bot's
// browser, after the user signs in). One run: session token, conversation list,
// every conversation, custom instructions, then one downloaded JSON bundle named
// chatgpt-pull-<date>.json. Progress is readable at window.__gb.
//
// Memories, Projects, and GPTs have no stable request here, so collect-accounts
// reads those three pages directly. These requests are the web app's own, not a
// public API, and can change. Every step is best effort and recorded in errors.
(async () => {
  const MAX_CONVERSATIONS = 300, CONCURRENCY = 4;
  const gb = (window.__gb = { phase: "start", listed: 0, pulled: 0, errors: [], done: false });
  const bundle = { service: "chatgpt", pulled_at: new Date().toISOString(), conversations: [], custom_instructions: null, errors: gb.errors };
  let headers = { accept: "application/json" };
  try {
    gb.phase = "session";
    const s = await (await fetch("/api/auth/session", { credentials: "include" })).json();
    if (s && s.accessToken) headers.authorization = `Bearer ${s.accessToken}`;
    const j = async (url) => {
      const r = await fetch(url, { credentials: "include", headers });
      if (!r.ok) throw new Error(`${r.status} ${url}`);
      return r.json();
    };

    gb.phase = "conversation list";
    const list = [];
    for (let offset = 0; list.length < MAX_CONVERSATIONS; offset += 100) {
      let page;
      try { page = await j(`/backend-api/conversations?offset=${offset}&limit=100&order=updated`); }
      catch (e) { gb.errors.push(String(e)); break; }
      const items = page.items || [];
      if (!items.length) break;
      list.push(...items);
      gb.listed = list.length;
      if (items.length < 100) break;
    }
    const ids = list.slice(0, MAX_CONVERSATIONS).map((c) => c.id).filter(Boolean);

    gb.phase = "conversations";
    let i = 0;
    await Promise.all(Array.from({ length: CONCURRENCY }, async () => {
      while (i < ids.length) {
        const id = ids[i++];
        try { bundle.conversations.push(await j(`/backend-api/conversation/${id}`)); gb.pulled = bundle.conversations.length; }
        catch (e) { gb.errors.push(String(e)); }
        await new Promise((r) => setTimeout(r, 150));
      }
    }));

    gb.phase = "custom instructions";
    try { bundle.custom_instructions = await j("/backend-api/user_system_messages"); } catch (e) { gb.errors.push(String(e)); }
  } catch (e) { gb.errors.push("fatal " + String(e)); }

  gb.phase = "download";
  const name = `chatgpt-pull-${new Date().toISOString().slice(0, 10)}.json`;
  const blob = new Blob([JSON.stringify(bundle)], { type: "application/json" });
  const a = Object.assign(document.createElement("a"), { href: URL.createObjectURL(blob), download: name });
  document.body.appendChild(a); a.click(); a.remove();
  window.__gbBundle = bundle;
  gb.done = true; gb.phase = "done";
  console.log(`chatgpt pull: ${bundle.conversations.length} conversations, ${gb.errors.length} errors -> ${name}`);
})();
```

## Claude.ai

There is no official API for claude.ai chat history, and its edge rejects requests that do not come from a browser, so the fast path runs inside the signed-in page.

**Conversations and projects, in order:**

1. **Official export, started first.** Settings, Privacy, Export data. Complete (conversations, projects with instructions, account and per-project memory), arrives by email, often within the hour. Team and Enterprise members do not have the button (only the org's primary owner can export): skip without comment. Same Gmail offer as above. Extract `conversations.json`, `memories.json`, `projects.json` to `accounts/claude/export/`.
2. **Page script after the sign-in.** Run the claude.ai page script below in the signed-in page, as "Running a page script" describes. It pulls the conversation list, every conversation's messages, and every project with its instructions, then downloads one bundle. This is the rung that runs today for everyone, since the export takes time and Team members never get it.
3. Nothing else. Do not click through conversations or open projects one by one.

**Memory** (fast, one page, do it every time since the export may not come): Settings, Capabilities, View and edit memory, copy verbatim to `memory.md`. If the page is unavailable, open a new chat and send Anthropic's own export prompt, "Write out your memories of me verbatim, exactly as they appear in your memory," and save the reply.

### Page script, run inside the signed-in claude.ai page

```javascript
// Bulk pull of a signed-in claude.ai account, run inside the page (the bot's browser,
// after the user signs in). One run: organizations, conversation list, every
// conversation's messages, projects with instructions, then one downloaded JSON
// bundle named claude-pull-<date>.json. Progress is readable at window.__gb.
//
// These are the requests the web app makes for itself. They are not a public API
// and can change. Every step is best effort and recorded in bundle.errors.
(async () => {
  const MAX_CONVERSATIONS = 300, CONCURRENCY = 4;
  const gb = (window.__gb = { phase: "start", listed: 0, pulled: 0, projects: 0, errors: [], done: false });
  const j = async (url) => {
    const r = await fetch(url, { credentials: "include", headers: { accept: "application/json" } });
    if (!r.ok) throw new Error(`${r.status} ${url}`);
    return r.json();
  };
  const bundle = { service: "claude", pulled_at: new Date().toISOString(), organization: null, conversations: [], projects: [], errors: gb.errors };
  try {
    gb.phase = "organizations";
    const orgs = await j("/api/organizations");
    const active = (document.cookie.match(/lastActiveOrg=([^;]+)/) || [])[1];
    const org = (orgs.find((o) => o.uuid === active) || orgs.find((o) => (o.capabilities || []).includes("chat")) || orgs[0]);
    bundle.organization = { uuid: org.uuid, name: org.name };
    const O = `/api/organizations/${org.uuid}`;

    gb.phase = "conversation list";
    const list = [];
    for (let offset = 0; list.length < MAX_CONVERSATIONS; offset += 50) {
      let page;
      try { page = await j(`${O}/chat_conversations_v2?limit=50&offset=${offset}&consistency=strong`); }
      catch (e) { try { page = await j(`${O}/chat_conversations?limit=50&offset=${offset}`); } catch (e2) { gb.errors.push(String(e2)); break; } }
      const items = Array.isArray(page) ? page : (page.data || page.conversations || page.items || []);
      if (!items.length) break;
      list.push(...items);
      gb.listed = list.length;
      if (items.length < 50) break;
    }
    const ids = list.slice(0, MAX_CONVERSATIONS).map((c) => c.uuid || c.id).filter(Boolean);

    gb.phase = "conversations";
    let i = 0;
    await Promise.all(Array.from({ length: CONCURRENCY }, async () => {
      while (i < ids.length) {
        const id = ids[i++];
        try {
          bundle.conversations.push(await j(`${O}/chat_conversations/${id}?tree=True&rendering_mode=messages&render_all_tools=true`));
          gb.pulled = bundle.conversations.length;
        } catch (e) { gb.errors.push(String(e)); }
        await new Promise((r) => setTimeout(r, 150));
      }
    }));

    gb.phase = "projects";
    try {
      const projects = await j(`${O}/projects`);
      for (const p of Array.isArray(projects) ? projects : (projects.data || [])) {
        const entry = { uuid: p.uuid, name: p.name, description: p.description, prompt_template: p.prompt_template, is_private: p.is_private, created_at: p.created_at, docs: [] };
        try { const d = await j(`${O}/projects/${p.uuid}`); Object.assign(entry, { prompt_template: d.prompt_template ?? entry.prompt_template, description: d.description ?? entry.description }); } catch (e) { gb.errors.push(String(e)); }
        try { const docs = await j(`${O}/projects/${p.uuid}/docs`); entry.docs = (Array.isArray(docs) ? docs : docs.data || []).map((d) => ({ file_name: d.file_name, size: d.content ? d.content.length : undefined })); } catch (e) { gb.errors.push(String(e)); }
        bundle.projects.push(entry);
        gb.projects = bundle.projects.length;
      }
    } catch (e) { gb.errors.push(String(e)); }
  } catch (e) { gb.errors.push("fatal " + String(e)); }

  gb.phase = "download";
  const name = `claude-pull-${new Date().toISOString().slice(0, 10)}.json`;
  const blob = new Blob([JSON.stringify(bundle)], { type: "application/json" });
  const a = Object.assign(document.createElement("a"), { href: URL.createObjectURL(blob), download: name });
  document.body.appendChild(a); a.click(); a.remove();
  window.__gbBundle = bundle;           // fallback: the bot can read this in chunks if the download did not land
  gb.done = true; gb.phase = "done";
  console.log(`claude pull: ${bundle.conversations.length} conversations, ${bundle.projects.length} projects, ${gb.errors.length} errors -> ${name}`);
})();
```

## Codex Cloud (only if the user says they use cloud tasks)

Open chatgpt.com/codex, save the task list (titles, repos, dates) to `accounts/codex-cloud/tasks.md`. Titles are enough evidence. One page.

## OpenClaw and Hermes

Local only. Nothing here.

## When a rung fails

Say one plain line ("ChatGPT's bulk pull did not work, so I am relying on the export it is emailing you") and move to the next rung. Record which rung produced what in `sources.md` under a "Method" column with the `live <service> <date>` or `export <file> <date>` label, so a resync knows what to retry. Infrastructure trouble (a rejected request, a blocked download, a locked folder) goes in the receipt's "Could not read" list, never in the body of what was delivered.
