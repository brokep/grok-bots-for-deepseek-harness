---
name: public-share-security-audit
description: "Use this before creating a public link, marketplace submission, public template distribution, or redistributing a Bot package."
---

# Public Share & Security Audit

Part of the Alfred agent preset.

---
name: Public Share & Security Audit
description: >-
  Use this before creating a public link, marketplace submission, public
  template distribution, or redistributing a Bot package.
---
# Public Share & Security Audit

Prepare a Bot for safe public sharing or marketplace distribution. Use before creating a public link, marketplace submission, public template distribution, or redistributing a Bot package.

## Workflow

1. Inspect the exact configuration that will be exposed.
2. Remove secrets, credentials, customer data, personal data, internal URLs, private source identifiers, private file paths, and creator-specific company information.
3. Replace private values with onboarding questions or placeholders.
4. Ensure essential behavior does not depend on creator conversation history, learned memory, creator files, creator computer, browser sessions, logins, or existing connector authentication.
5. List required and optional recipient connectors.
6. Require fresh recipient authentication.
7. Ensure first-run onboarding collects company scope, Registry source, timezone, output destination, and approval boundaries.
8. Do not assume shared Routines arrive inactive.
9. Keep scheduled Routines out of the public source until activation behavior has been tested safely.
10. Add version, author, change log, known limitations, example requests, recipient responsibilities, and license or redistribution rules.
11. Test the public copy from a separate eligible account.
12. Verify exact Description, expected Skills, Skill enabled state and invocation, included Routine contents and activation state, fresh authentication, approval enforcement, and absence of creator-specific data.
13. Block release when any critical issue remains.
14. Stop for approval before creating the test share link.
15. Require separate final approval before broad distribution.

## Output

Return:

- Pass, conditional pass, or block
- Sanitized configuration
- Removed private elements
- Recipient setup checklist
- Required connections
- Routine installation policy
- Version and change log
- Known limitations
- Separate-account test evidence
- Unresolved issues
- Exact public-sharing action awaiting approval

## Stop point

Never create a public test link without approval for the exact sanitized version.

Never distribute broadly without separate final approval.
