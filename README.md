# chunk-atlas-exam

Chunk Atlas Quiz Trainer — static web app (no build step) for practicing
English business-communication chunks from `ChunkAtlas_EN.jsx`.

Structure and engine (app.js/style.css) copied almost verbatim from
`cbap-cert` (CBAP Mock Exam Trainer) — same author, same pattern, for easy
parallel maintenance.

## Current scope (pilot)

Only **1 topic: "Core Patterns"** (14 communicative-function groups —
opening, framing, explaining, giving examples, clarifying, asking
questions, disagreeing politely, steering, concluding, decision making,
buying thinking time, cutting short, structuring/opinion/nuance) — 54
multiple-choice questions, generated from the source content in
`ChunkAtlas_EN.jsx` (tier `core` / nav tab "Situations", topic `Core
Patterns`).

The other 34 topics of Chunk Atlas (Real-Time Fluency / Voice & Presence /
Language Systems / Confidence & Humour...) have NO questions yet — to be
added once this format is approved.

Question format: context-based 4-option multiple choice — given a
communication situation, pick the correct chunk out of 4 options (1
correct from the matching function, 3 wrong ones pulled from other
functions). "Matching" is folded into this same MCQ format to reuse the
CBAP engine as-is, rather than building a separate drag-and-drop UI.

Filtering/scoring is grouped at **tier level** — the 5 big nav tabs of
`ChunkAtlas_EN.jsx` (Situations / Real-Time Fluency / Voice & Presence /
Language Systems / Confidence & Humour), not the fine per-function
sub-groups (there are 18 of those just within "Core Patterns" alone — too
many for a filter UI). The fine function name (e.g. "Opening",
"Clarifying") still shows up inside each question's explanation text for
learning value, just not as a separate filterable field.

## Run locally

```bash
npm run dev
# or: python3 -m http.server 8010
# open http://localhost:8010
```

## Deploy to Cloudflare Pages

Static site, no bundler — `npm run build` just copies `index.html`,
`style.css`, `app.js`, `data/`, `fonts/` into `dist/` (nothing to
transpile/bundle, this only exists so Cloudflare Pages has a `dist`
directory to publish, matching its default). In the Pages project
settings:

- **Build command:** `npm run build`
- **Build output directory:** `dist`

(Unlike `cbap-cert`, which is configured with output directory `/` and no
build step — either approach works, this one just matches Cloudflare's
usual default instead of requiring a manual setting change.)

## Project structure

- `index.html`, `style.css`, `app.js` — the app
- `data/core-patterns.json` — pilot question bank (parsed from ChunkAtlas_EN.jsx)
  `{ examId, title, questions: [{ id, ka, kaName, question, options, correct, explanation }] }`
  — `ka`/`kaName` currently hardcoded to the "core" / "Situations" tier for
  every question, since that's the only tier populated so far.
- `scripts/generate_core_patterns.py` — script that generates
  `data/core-patterns.json` from hand-curated source content, kept around
  for regenerating/extending later.

Progress (bookmarks and missed questions) is stored in the browser's
`localStorage` — nothing is sent to a server.

## Adding more topics

1. Extract the new topic's content from `ChunkAtlas_EN.jsx` (the `DATA`
   array, `ti`/`la` fields).
2. Write an English context sentence for each communicative-function group
   (the `h` field inside `gr[]`).
3. Set `TIER_ID`/`TIER_NAME` to the topic's actual tier (`core` /
   `fluency` / `presence` / `mastery` / `confidence` / `humour` — note
   `confidence` and `humour` both map to the combined "Confidence &
   Humour" nav tab).
4. Run a generator script similar to `scripts/generate_core_patterns.py`
   to produce a new JSON file.
5. Add an entry to `SET_FILES`/`SET_LABELS` in `app.js`.
6. Once more than one tier has questions, restore a "choose a topic" UI in
   `index.html` (currently omitted since the pilot only has one).
