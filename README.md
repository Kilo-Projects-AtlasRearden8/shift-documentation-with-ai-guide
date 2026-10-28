# AI-Assisted Shift Documentation

A beginner manual for nurses and healthcare workers on using AI to draft shift documentation — report sheets, handoff notes, and patient-education summaries — step by step, privacy first, never medical advice.

Published by **Asdale Dynamics, LLC** (Indiana, formed October 2026), by Dylan Asdale, a registered nurse turned AI author.

## What this is

Plain-English, step-by-step guidance for using AI to help with nursing and healthcare shift documentation. It covers:

- Privacy rules — what never to paste into an AI tool (no patient names, MRNs, dates of birth, room numbers, or anything identifying)
- Facility policy first — your employer's rules override anything in this manual
- Getting started with an AI tool
- Drafting report sheets
- Writing SBAR handoff notes
- Creating plain-language patient-education summaries
- A full start-to-finish shift workflow example
- Education-only disclaimers — never medical advice

## What this is not

- Medical advice. AI cannot assess patients, diagnose, recommend medications, or replace clinical judgment.
- A substitute for your facility's policies, nursing training, or your clinical judgment.
- A tool for pasting patient-identifying information into AI.

## Contents

- `docs/` — beginner manual in Markdown (8 chapters)
- `site/` — static HTML mirror with CSS (runs in any browser, no build step)
- `LICENSE` — MIT License, Copyright (c) 2026 Asdale Dynamics, LLC

## How to use

### Markdown (docs/)
Open any `.md` file in `docs/` with a text editor or Markdown viewer. Start with `docs/00-introduction.md`, then `docs/01-privacy-and-safety.md`.

### Static HTML site (site/)
Open `site/index.html` in any web browser. No install, no build step, no server required. The site is local-first and works offline.

## Verification

Run the verification script:

```
python3 verify.py
```

It checks that all HTML files parse, every internal link resolves, required pages exist, and the LICENSE copyright line matches.

## Credit

Written and published by Asdale Dynamics, LLC. Dylan Asdale is a registered nurse turned AI author and founder of Asdale Dynamics, LLC. His book *The Massive AI Manual* and hub site dylanasdale.github.io explain AI "like a friend would": plain English, step by step, never condescending.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.

Education only — not medical advice. Facility policy comes first.
