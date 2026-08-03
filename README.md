# chunk-atlas-exam

Chunk Atlas Quiz Trainer — static web app (no build step) for practicing
English business-communication chunks from `ChunkAtlas_EN.jsx`.

Structure and engine (app.js/style.css) copied almost verbatim from
`cbap-cert` (CBAP Mock Exam Trainer) — same author, same pattern, for easy
parallel maintenance.

## Current scope

**Complete: 37 topics, 1477 multiple-choice questions**, covering all 5
nav tabs of `ChunkAtlas_EN.jsx` — Situations (8 topics), Real-Time Fluency
(11), Voice & Presence (8), Language Systems (8), and Confidence & Humour
(2 topics: "Confidence" and "Humour & Warmth" share one combined tab,
matching the source app's own `NAV_TIERS` grouping).

Question format: context-based 4-option multiple choice — given a
communication situation, pick the correct chunk out of 4 options (1
correct from the matching function, 3 wrong ones pulled from other
functions). Every option's explanation states which function it belongs
to and why it does/doesn't fit this context, plus 3 "Similar chunks" from
the same function group; the correct answer also gets a full example
sentence using the exact chunk. "Matching" is folded into this same MCQ
format to reuse the CBAP engine as-is, rather than building a separate
drag-and-drop UI.

Filtering/scoring in step 2 ("Filter by tab") is grouped at **tier
level** — the same 5 tabs as the topic picker — not the fine per-function
sub-groups (there are 250+ of those across all topics — too many for a
filter UI). The fine function name (e.g. "Opening", "Clarifying") still
shows up inside each question's explanation text for learning value. Step
1 ("Choose a topic") lets you pick one specific topic or "Mix everything"
across all 37.

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

- `index.html`, `style.css`, `app.js` — the app. `app.js`'s `TOPICS` array
  is the single source of truth for which topics exist, their display
  labels, and their tier grouping — the home-screen topic picker and tier
  filter are both rendered from it (plus the loaded question counts), as
  a compact row list (not a card grid) so a 37-topic list stays scannable.
- `data/<exam-id>.json` — one question bank per topic (37 files), each
  `{ examId, title, questions: [{ id, ka, kaName, question, options, correct, explanation }] }`
  — `ka`/`kaName` on every question is the TIER id/name (e.g.
  `core`/"Situations", `presence`/"Voice & Presence",
  `growth`/"Confidence & Humour"), not the fine function group.
- `scripts/lib.py` — shared question-generation engine (`generate_topic()`):
  builds the 4-option MCQs, picks distractors from other function groups,
  picks "Similar chunks" equivalents, and formats the explanation text
  (including `smart_quote()`, which avoids doubled `""..."""` marks when a
  source phrase/example already contains embedded quote characters).
  Change the explanation format/logic here — it applies to every topic
  the next time its generator script is re-run.
- `scripts/generate_<exam-id>.py` — one script per topic (37 total). Each
  defines a hand-curated `groups_def` (function label, question context,
  usage note, and a `(phrase, example sentence)` list per function group)
  and calls `lib.generate_topic()`. Source phrase content is copied by
  hand from the matching topic in `ChunkAtlas_EN.jsx`; usage notes and
  example sentences are original writing, not extracted from the source.

Progress (bookmarks and missed questions) is stored in the browser's
`localStorage` — nothing is sent to a server.

## Regenerating / extending content

To pick up a `lib.py` engine change (e.g. an explanation-format tweak)
across every topic at once:

```bash
for f in scripts/generate_*.py; do python3 "$f"; done
```

To add a topic that doesn't exist yet (all 5 tabs are now covered, but
`ChunkAtlas_EN.jsx` itself could grow more topics later):

1. Extract the new topic's content from `ChunkAtlas_EN.jsx` (the `DATA`
   array, `ti`/`la` fields) — only items with `"t": "i"` are real chunks;
   skip `"t": "n"` (prose) and `"t": "c"` (comparison) items, and skip any
   group that's pure meta-advice with no actual chunks (e.g. Core
   Patterns' "H15", a numbered list of speaking tips).
2. For each function-group header (`h` field inside `gr[]`), write an
   English `question_context` ("You..."), an impersonal `usage_note`
   ("used to/when..."), and — for every phrase in that group — a natural,
   specific example sentence using that exact phrase. Split a header into
   multiple `groups_def` entries if it bundles clearly distinct functions
   (see e.g. `generate_core_patterns.py`'s "H14" split into 5).
3. Write `scripts/generate_<exam-id>.py` following the structure of an
   existing script, importing `generate_topic` from `lib.py`, with the
   correct `tier_id`/`tier_name` for its tab.
4. Run it (`python3 scripts/generate_<exam-id>.py`) to produce
   `data/<exam-id>.json`.
5. Add an entry to the `TOPICS` array in `app.js` (id, label, tier) — the
   home-screen UI picks it up automatically, no other UI changes needed.
