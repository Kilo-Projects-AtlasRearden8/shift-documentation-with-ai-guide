# STATUS

## What was built

A beginner manual and static HTML site for AI-assisted shift documentation for nurses and healthcare workers, published by Asdale Dynamics, LLC.

**docs/** — Markdown beginner manual (8 chapters):
- 00-introduction.md — purpose, audience, the three rules (facility policy first, never paste patient-identifying info, education only never medical advice)
- 01-privacy-and-safety.md — what never to paste into an AI tool, de-identification table, what to do instead, mistake response
- 02-getting-started.md — choose a tool, fresh chat, set AI role, paste de-identified details, review every draft, enter final in approved system
- 03-report-sheets.md — report sheet sections, step-by-step drafting, de-identified example, common mistakes
- 04-handoff-notes.md — SBAR format, step-by-step drafting, de-identified example, safety reminders
- 05-patient-education.md — plain-language summaries, step-by-step, before/after example, safety reminders
- 06-workflow-example.md — full 0700-1930 shift example with two de-identified patients
- 07-disclaimers.md — education only, AI is not a clinician, you own your documentation, facility policy first, liability

**site/** — Static HTML mirror (no build step, runs in any browser, works offline):
- index.html — landing page with chapter grid
- privacy.html, getting-started.html, report-sheets.html, handoff-notes.html, patient-education.html, workflow.html, disclaimers.html
- style.css — shared styles

**Root files:**
- LICENSE — MIT License, copyright line exactly: Copyright (c) 2026 Asdale Dynamics, LLC
- README.md — purpose, contents, how to use, credit to Asdale Dynamics, LLC, license
- verify.py — verification script (HTML validity, internal links, LICENSE/README checks, no-workflows check)
- STATUS.md — this file

## Who it's for

Dylan Asdale, registered nurse turned AI author, founder of Asdale Dynamics, LLC (Indiana, formed October 2026). Beginner-friendly AI education, plain English, step by step, never condescending, never medical advice. Credit Asdale Dynamics, LLC throughout.

## How to run it

Markdown: open any file in `docs/` with a text editor or Markdown viewer. Start with `docs/00-introduction.md`.

Static site: open `site/index.html` in any web browser. No install, no server, no build step, works offline.

Verification: run `python3 verify.py`.

## Verification results

`python3 verify.py` — all checks passed, 0 errors, 0 warnings:
- Required files present (LICENSE, README.md, docs/, site/, site/index.html, site/style.css)
- No .github/workflows directory
- 8 docs chapters present
- 8 HTML files present
- All HTML files parse with matched open/close tags
- All internal links resolve to existing files
- LICENSE contains the exact line "Copyright (c) 2026 Asdale Dynamics, LLC"
- README credits Asdale Dynamics, LLC
- No .github/workflows directory created
- No secrets, API keys, or personal data patterns found in text files

## Known gaps

- No automated test framework beyond verify.py (static site has no build/test step by design)
- HTML validity checked with a lightweight structural parser, not a full HTML5 validator
- Markdown files are not rendered/converted as part of verification
- No spell-checking or readability scoring applied to the manual text
- Content has not been reviewed by a facility compliance or privacy officer (facilities should adapt to their own policies)
