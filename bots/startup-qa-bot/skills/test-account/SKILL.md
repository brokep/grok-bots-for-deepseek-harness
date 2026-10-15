---
name: test-account
description: "Use to start my own browser, sign up my own test account with the saved email, catch its verification emails, and check it before every walk. Never any other account, inbox, or browser."
---

# test-account

Part of the Startup QA Bot agent preset.

# test-account

My own test account in the product, signed up with settings.email and used only in my own browser. Never a real customer's account or the user's own. Set it up once and check it before every walk.

## My own browser

The browser tools share cookies and saved logins with the user's other bots, so the product never opens there: I never walk in the user's real session, and my test login never lands in theirs. Screenshot my desktop, then qa.py browser start --match <that shot's path> opens Chrome with my own profile on my own screen. No match: --display :N, the display my prompt gives me. Drive it with Computer, see it with Screenshot. Links from the inbox: qa.py browser open <link>. Leave it running between walks. It uses this computer's own Chrome and installs nothing, so after a restart or a computer update I start it again the same way (displays can change) and sign back in if asked.

## Set up

1. In my browser, sign up with settings.email, name "<Product> QA", and obvious test data anywhere else (Test Co). Prefer an email code or magic link. It wants a password: qa.py password makes one and keeps it in its folder, typed straight into the form. That email already has an account: sign in instead.
2. Verification. Inbox agentmail: list_messages on that inbox from the product since the signup, then get_message for the code or link. Nothing after 2 minutes: check once more, then ask the user to resend or wait. Inbox other: ask the user to paste the code or link.
3. Finish the product's own onboarding with test data. Screenshot the account menu, qa.py shot <path> account, then qa.py set account "<as shown>".

Stops: a card, a phone code, an ID check, or a CAPTCHA: request_box_help "Please finish this in my browser, then hand it back," and never type their details. Single sign-on only: ask them to sign me in once with a test login the same way. Invite only: ask the user to invite settings.email, then accept from the inbox.

## Check, before every walk

qa.py browser status. Not running: start it as in My own browser. Screenshot the account menu in my browser. It must match settings.account. Signed out: sign back in with settings.email (a code from the inbox, or qa.py password). Any other account: stop and tell the user, never walk in it. Never sign up or sign in with any other email.

## The inbox

Read only the product's verification, sign-in, invite, and reset emails. Never send, reply, forward, or unsubscribe, and never open another inbox. Codes and links are used once and never repeated in chat.
