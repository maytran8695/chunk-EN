"""Shared question-generation engine, extracted from generate_core_patterns.py
so every per-topic generator script can reuse identical logic (and identical
quality bar) instead of duplicating it.

Usage from a per-topic script:

    from lib import generate_topic

    generate_topic(
        out_path=...,
        exam_id="meetings-collab",
        title="Chunk Atlas — Situations: Meetings & Collaboration",
        tier_id="core",
        tier_name="Situations",
        groups_def=[...],  # same shape as documented below
    )

groups_def shape — list of:
    (function_label, question_context_en, usage_note_en, [(phrase, example_sentence), ...])

- question_context_en: the situation described in the question stem ("You...").
- usage_note_en: general "used when..." explanation (no "You" — third person),
  shown when a phrase from this group appears as a WRONG answer to explain
  what it actually fits.
- example_sentence: a natural, specific sentence using that EXACT phrase,
  shown only for whichever phrase ends up as the CORRECT answer.
"""
import json
import random


def generate_topic(out_path, exam_id, title, tier_id, tier_name, groups_def, seed=42):
    random.seed(seed)

    GROUPS = {name: (ctx, note, phrases) for name, ctx, note, phrases in groups_def}
    all_phrases = []
    for name, ctx, note, phrases in groups_def:
        for phrase, example in phrases:
            all_phrases.append((name, phrase))

    def equivalents_for(group_name, exclude_phrase, k=3):
        _, _, phrases = GROUPS[group_name]
        pool = [p for p, _ in phrases if p != exclude_phrase]
        random.shuffle(pool)
        return pool[:k]

    def build_question(qid, name, ctx, usage_note, phrases, used_correct):
        candidates = [p for p, _ in phrases if p not in used_correct.get(name, set())]
        if not candidates:
            candidates = [p for p, _ in phrases]
        correct_phrase = random.choice(candidates)
        correct_example = dict(phrases)[correct_phrase]
        used_correct.setdefault(name, set()).add(correct_phrase)

        other_pool = [(n, p) for n, p in all_phrases if n != name]
        random.shuffle(other_pool)
        distractors = []
        seen_phrases = set()
        for n, p in other_pool:
            if p == correct_phrase or p in seen_phrases:
                continue
            distractors.append((n, p))
            seen_phrases.add(p)
            if len(distractors) == 3:
                break

        all_options = [(correct_phrase, True, name)] + [(p, False, n) for n, p in distractors]
        random.shuffle(all_options)
        letters = ["A", "B", "C", "D"]
        options = {}
        explanation_blocks = []
        correct_letter = None
        for letter, (phrase, is_correct, group_name) in zip(letters, all_options):
            options[letter] = phrase
            if is_correct:
                correct_letter = letter
                eqs = equivalents_for(group_name, phrase, k=3)
                eqs_str = "\n".join(f'- {e}' for e in eqs)
                article = "an" if group_name[0] in "AEIOU" else "a"
                block = (
                    f'✓ Correct — "{phrase}" is {article} {group_name} chunk: {usage_note}.\n'
                    f'Example: "{correct_example}"'
                    + (f'\nSimilar chunks:\n{eqs_str}' if eqs else '')
                )
            else:
                g_ctx, g_note, g_phrases = GROUPS[group_name]
                eqs = equivalents_for(group_name, phrase, k=3)
                eqs_str = "\n".join(f'- {e}' for e in eqs)
                block = (
                    f'✗ "{phrase}" belongs to {group_name} — {g_note}, not this context.'
                    + (f'\nSimilar chunks:\n{eqs_str}' if eqs else '')
                )
            explanation_blocks.append(block)

        explanation = "\n\n".join(explanation_blocks)

        return {
            "id": qid,
            "ka": tier_id,
            "kaName": tier_name,
            "question": ctx + " Which chunk fits best?",
            "options": options,
            "correct": correct_letter,
            "explanation": explanation,
        }

    questions = []
    qid = 1
    used_correct = {}
    for name, ctx, usage_note, phrases in groups_def:
        n = min(4, max(2, len(phrases) // 2))
        for _ in range(n):
            questions.append(build_question(qid, name, ctx, usage_note, phrases, used_correct))
            qid += 1

    out = {"examId": exam_id, "title": title, "questions": questions}
    with open(out_path, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    total_source_phrases = sum(len(phrases) for _, _, _, phrases in groups_def)
    print(f"{exam_id}: {len(groups_def)} groups, {total_source_phrases} source phrases -> {len(questions)} questions -> {out_path}")
    return len(questions)
