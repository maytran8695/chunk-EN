(() => {
  "use strict";

  // Topic catalog — tierLabel groups topics for display; SET_FILES/SET_LABELS
  // are derived from this so there's a single source of truth to extend when
  // more topics are added later.
  const TOPICS = [
    { id: "core", label: "Core Patterns", tier: "Situations" },
    { id: "meetings-collaboration", label: "Meetings & Collaboration", tier: "Situations" },
    { id: "presentations-demos", label: "Presentations & Demos", tier: "Situations" },
    { id: "persuasion-debate", label: "Persuasion & High-Stakes Debate", tier: "Situations" },
    { id: "collaboration-levels", label: "Collaboration Across Levels", tier: "Situations" },
    { id: "feedback-difficult", label: "Feedback & Difficult Conversations", tier: "Situations" },
    { id: "everyday-social", label: "Everyday & Social", tier: "Situations" },
    { id: "nuance-delivery", label: "Nuance, Delivery & Written Register", tier: "Situations" },
    { id: "fluency-hesitation", label: "Fluency & Hesitation Management", tier: "Real-Time Fluency" },
    { id: "words-fail", label: "When Words Fail", tier: "Real-Time Fluency" },
    { id: "self-repair", label: "Self-Repair & Recovery", tier: "Real-Time Fluency" },
    { id: "adjacency-pairs", label: "Adjacency Pairs & Preference Design", tier: "Real-Time Fluency" },
    { id: "response-tokens", label: "Response Tokens & Active Listenership", tier: "Real-Time Fluency" },
    { id: "topic-management", label: "Topic Management", tier: "Real-Time Fluency" },
    { id: "storytelling", label: "Conversational Storytelling", tier: "Real-Time Fluency" },
    { id: "mid-sentence-breakdown", label: "Mid-Sentence Breakdown", tier: "Real-Time Fluency" },
    { id: "misunderstanding", label: "Misunderstanding, Both Ways", tier: "Real-Time Fluency" },
    { id: "under-fire", label: "Under Fire: Pressure Situations", tier: "Real-Time Fluency" },
    { id: "damage-control", label: "Damage Control", tier: "Real-Time Fluency" },
    { id: "tonicity-stress", label: "Tonicity", tier: "Voice & Presence" },
    { id: "tone-choice", label: "Tone Choice", tier: "Voice & Presence" },
    { id: "decoding-fast-speech", label: "Decoding Fast Speech", tier: "Voice & Presence" },
    { id: "voice-paralanguage", label: "Voice & Paralanguage", tier: "Voice & Presence" },
    { id: "gesture-gaze-presence", label: "Gesture, Gaze & Presence", tier: "Voice & Presence" },
    { id: "rhetoric-memorable", label: "Rhetoric & Memorable Language", tier: "Voice & Presence" },
    { id: "cultural-fluency", label: "Cultural Fluency & Varieties", tier: "Voice & Presence" },
    { id: "emotional-attunement", label: "Emotional Attunement", tier: "Voice & Presence" },
    { id: "collocation-networks", label: "Collocation Networks", tier: "Language Systems" },
    { id: "semantic-prosody", label: "Semantic Prosody & Connotation", tier: "Language Systems" },
    { id: "discourse-markers", label: "Discourse & Pragmatic Markers", tier: "Language Systems" },
    { id: "stance-hedging-boosting", label: "Stance, Hedging & Boosting", tier: "Language Systems" },
    { id: "information-packaging", label: "Information Packaging", tier: "Language Systems" },
    { id: "idiomaticity", label: "Idiomaticity", tier: "Language Systems" },
    { id: "vague-approximative", label: "Vague & Approximative Language", tier: "Language Systems" },
    { id: "near-synonym", label: "Near-Synonym Discrimination", tier: "Language Systems" },
    { id: "confidence", label: "Confidence", tier: "Confidence & Humour" },
    { id: "humour-warmth", label: "Humour & Warmth", tier: "Confidence & Humour" },
  ];
  const SET_FILES = Object.fromEntries(TOPICS.map(t => [t.id, `data/${t.id}.json`]));
  const SET_LABELS = Object.fromEntries(TOPICS.map(t => [t.id, t.label]));
  const SECONDS_PER_QUESTION = 45; // chunk MCQs are shorter than CBAP scenario questions, so less time/question

  const LS_BOOKMARKS = "chunkatlas_bookmarks";
  const LS_WRONG = "chunkatlas_wrong";
  const LS_THEME = "chunkatlas_theme";

  /** @type {Record<string, any>} raw datasets keyed by examId */
  const DATA = {};
  /** @type {Record<string, any>} all questions keyed by uid ("core-Q45") */
  const QUESTIONS_BY_UID = {};

  let session = null; // current quiz session state
  let timerInterval = null;

  // ---------- storage helpers ----------
  function loadSet(key) {
    try { return new Set(JSON.parse(localStorage.getItem(key) || "[]")); }
    catch { return new Set(); }
  }
  function saveSet(key, set) {
    localStorage.setItem(key, JSON.stringify([...set]));
  }

  function uid(examId, id) { return `${examId}-Q${id}`; }

  // ---------- data loading ----------
  async function loadData() {
    const entries = await Promise.all(
      Object.entries(SET_FILES).map(async ([examId, path]) => {
        const res = await fetch(path);
        if (!res.ok) throw new Error(`Failed to load ${path}`);
        return [examId, await res.json()];
      })
    );
    for (const [examId, data] of entries) {
      DATA[examId] = data;
      for (const q of data.questions) {
        const u = uid(examId, q.id);
        QUESTIONS_BY_UID[u] = { ...q, uid: u, examId, sourceLabel: SET_LABELS[examId] };
      }
      const countEl = document.getElementById(`count-${examId}`);
      if (countEl) countEl.textContent = `(${data.questions.length} questions)`;
    }
    renderSourceSelect();
  }

  // ---------- home screen ----------
  function renderSourceSelect() {
    // One row PER TIER (5 total): a checkbox to include/exclude the tier,
    // plus a <select> defaulted to its own first topic — no placeholder, no
    // cross-resetting. All 5 selects stay active at once; Start combines
    // whichever topic is currently picked in each checked tier's dropdown.
    // The checkbox doubles as the tab/ka filter, since every topic's `ka`
    // is 1:1 with its tier. A separate "mix everything" checkbox bypasses
    // the topic picks and pulls every topic within each checked tier instead.
    const option = (value, label, count, selected) =>
      `<option value="${value}" ${selected ? "selected" : ""}>${escapeHtml(label)} (${count} questions)</option>`;
    const tiers = [...new Set(TOPICS.map(t => t.tier))];
    let html = "";
    for (const tier of tiers) {
      const tierTopics = TOPICS.filter(t => t.tier === tier);
      const sampleQ = DATA[tierTopics[0].id]?.questions[0];
      const ka = sampleQ ? sampleQ.ka : "";
      html += `<div class="tier-select-row">`;
      html += `<span class="tier-check-label">`;
      html += `<input type="checkbox" class="tier-toggle" data-tier="${escapeHtml(tier)}" data-ka="${escapeHtml(ka)}" checked>`;
      html += `<label class="tier-select-label">${escapeHtml(tier)}</label>`;
      html += `</span>`;
      html += `<select class="tier-select" data-tier="${escapeHtml(tier)}">`;
      html += tierTopics.map((t, i) => option(t.id, t.label, DATA[t.id] ? DATA[t.id].questions.length : 0, i === 0)).join("");
      html += `</select>`;
      html += `</div>`;
    }
    const totalQuestions = Object.values(QUESTIONS_BY_UID).length;
    html += `<label class="mix-row"><input type="checkbox" id="mix-everything">` +
      `<span>Mix everything (each checked tier pulls ALL its topics, not just the one picked)</span><span class="ka-row-count">${totalQuestions} questions</span></label>`;
    document.getElementById("source-select").innerHTML = html;
    updateTierRowStates();
  }

  function updateTierRowStates() {
    const mixed = document.getElementById("mix-everything")?.checked;
    document.querySelectorAll(".tier-select-row").forEach(row => {
      const toggle = row.querySelector(".tier-toggle");
      const select = row.querySelector(".tier-select");
      select.disabled = mixed || !toggle.checked;
      row.classList.toggle("tier-off", !toggle.checked);
    });
  }

  function getCheckedTierRows() {
    return [...document.querySelectorAll(".tier-select-row")]
      .map(row => ({ toggle: row.querySelector(".tier-toggle"), select: row.querySelector(".tier-select") }))
      .filter(r => r.toggle.checked);
  }

  function getSelectedSource() {
    const mixCheckbox = document.getElementById("mix-everything");
    if (mixCheckbox && mixCheckbox.checked) return "mixed";
    return getCheckedTierRows().map(r => r.select.value);
  }

  function updateReviewButton() {
    const bookmarks = loadSet(LS_BOOKMARKS);
    const wrong = loadSet(LS_WRONG);
    const union = new Set([...bookmarks, ...wrong]);
    const btn = document.getElementById("btn-review");
    const countEl = document.getElementById("review-count");
    countEl.textContent = String(union.size);
    btn.disabled = union.size === 0;
  }

  function getSelectedKAs() {
    return [...document.querySelectorAll(".tier-toggle:checked")].map(i => i.dataset.ka);
  }

  function shuffle(arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function buildQuestionList(source, kaFilter) {
    // source is either "mixed" (every topic) or an array of examIds — one
    // per tier dropdown — whose questions get combined into one session.
    let list;
    if (source === "mixed") {
      list = Object.values(QUESTIONS_BY_UID);
    } else {
      list = source.flatMap(examId =>
        DATA[examId] ? DATA[examId].questions.map(q => QUESTIONS_BY_UID[uid(examId, q.id)]) : []
      );
    }
    list = shuffle(list);
    return list.filter(q => kaFilter.includes(q.ka));
  }

  function startSession(questions, mode, isReview) {
    if (questions.length === 0) {
      alert("No questions match the selected filters.");
      return;
    }
    session = {
      mode,
      isReview: !!isReview,
      questions,
      index: 0,
      answers: {},        // uid -> selected letter
      bookmarked: new Set(loadSet(LS_BOOKMARKS)),
      timeLimit: mode === "exam" ? questions.length * SECONDS_PER_QUESTION : null,
      startedAt: Date.now(),
    };
    showScreen("quiz");
    renderQuestion();
    scrollToTop();
    if (mode === "exam") startTimer();
  }

  // ---------- quiz screen ----------
  function showScreen(name) {
    for (const s of ["home", "quiz", "result"]) {
      document.getElementById(`screen-${s}`).classList.toggle("hidden", s !== name);
    }
  }

  function currentQuestion() {
    return session.questions[session.index];
  }

  function renderQuestion() {
    const q = currentQuestion();
    const total = session.questions.length;

    document.getElementById("quiz-position").textContent = `Question ${session.index + 1} / ${total}`;
    document.getElementById("progress-fill").style.width = `${((session.index + 1) / total) * 100}%`;

    const kaTag = document.getElementById("question-ka");
    kaTag.textContent = q.kaName || q.ka;

    const bookmarkBtn = document.getElementById("btn-bookmark");
    bookmarkBtn.classList.toggle("active", session.bookmarked.has(q.uid));
    bookmarkBtn.textContent = session.bookmarked.has(q.uid) ? "★" : "☆";

    document.getElementById("question-text").textContent = q.question;

    const optionsList = document.getElementById("options-list");
    optionsList.innerHTML = "";
    const selected = session.answers[q.uid];
    const showFeedback = session.mode === "practice" && selected !== undefined;

    for (const letter of ["A", "B", "C", "D"]) {
      const btn = document.createElement("button");
      btn.className = "option-btn";
      btn.disabled = showFeedback;
      if (showFeedback) {
        if (letter === q.correct) btn.classList.add("correct");
        else if (letter === selected) btn.classList.add("incorrect");
      } else if (letter === selected) {
        btn.classList.add("selected");
      }
      btn.innerHTML = `<span class="opt-letter">${letter}.</span><span>${escapeHtml(q.options[letter])}</span>`;
      btn.addEventListener("click", () => selectAnswer(letter));
      optionsList.appendChild(btn);
    }

    const explBox = document.getElementById("explanation-box");
    if (showFeedback) {
      explBox.classList.remove("hidden");
      const correct = selected === q.correct;
      explBox.innerHTML = `<span class="expl-label">${correct ? "✓ Correct" : `✗ Incorrect — correct answer is ${q.correct}`}</span>${formatExplanation(q.explanation)}`;
    } else {
      explBox.classList.add("hidden");
      explBox.innerHTML = "";
    }

    document.getElementById("btn-prev").disabled = session.index === 0;
    const isLast = session.index === total - 1;
    const nextBtn = document.getElementById("btn-next");
    const submitBtn = document.getElementById("btn-submit");
    if (session.mode === "practice") {
      nextBtn.textContent = isLast ? "View results" : "Next →";
      nextBtn.classList.remove("hidden");
      submitBtn.classList.add("hidden");
      nextBtn.disabled = !showFeedback;
    } else {
      nextBtn.classList.toggle("hidden", isLast);
      nextBtn.textContent = "Next →";
      submitBtn.classList.remove("hidden");
    }
  }

  function escapeHtml(str) {
    const div = document.createElement("div");
    div.textContent = str;
    return div.innerHTML;
  }

  function formatExplanation(str) {
    return escapeHtml(str)
      .split("\n\n")
      .map(p => `<p>${p.replace(/\n/g, "<br>")}</p>`)
      .join("");
  }

  function selectAnswer(letter) {
    const q = currentQuestion();
    if (session.mode === "practice" && session.answers[q.uid] !== undefined) return; // already locked
    session.answers[q.uid] = letter;
    renderQuestion();
  }

  function toggleBookmark() {
    const q = currentQuestion();
    if (session.bookmarked.has(q.uid)) session.bookmarked.delete(q.uid);
    else session.bookmarked.add(q.uid);
    saveSet(LS_BOOKMARKS, session.bookmarked);
    renderQuestion();
  }

  function scrollToTop() {
    window.scrollTo({ top: 0, left: 0, behavior: "smooth" });
  }

  function goPrev() {
    if (session.index > 0) { session.index--; renderQuestion(); scrollToTop(); }
  }
  function goNext() {
    if (session.index < session.questions.length - 1) { session.index++; renderQuestion(); scrollToTop(); }
    else if (session.mode === "practice") finishSession();
  }

  function startTimer() {
    let remaining = session.timeLimit;
    const timerEl = document.getElementById("quiz-timer");
    timerEl.classList.remove("hidden");
    const render = () => {
      const h = String(Math.floor(remaining / 3600)).padStart(2, "0");
      const m = String(Math.floor((remaining % 3600) / 60)).padStart(2, "0");
      const s = String(remaining % 60).padStart(2, "0");
      timerEl.textContent = `${h}:${m}:${s}`;
      timerEl.classList.toggle("low-time", remaining <= 300);
    };
    render();
    timerInterval = setInterval(() => {
      remaining--;
      render();
      if (remaining <= 0) {
        clearInterval(timerInterval);
        finishSession();
      }
    }, 1000);
  }
  function stopTimer() {
    if (timerInterval) { clearInterval(timerInterval); timerInterval = null; }
    document.getElementById("quiz-timer").classList.add("hidden");
  }

  function exitQuiz() {
    if (!confirm("Exit the current session? Your progress will not be saved.")) return;
    stopTimer();
    session = null;
    showScreen("home");
    updateReviewButton();
  }

  // ---------- result screen ----------
  function finishSession() {
    stopTimer();

    const wrongSet = loadSet(LS_WRONG);
    const results = session.questions.map(q => {
      const chosen = session.answers[q.uid];
      const isCorrect = chosen === q.correct;
      if (chosen !== undefined) {
        if (isCorrect) wrongSet.delete(q.uid);
        else wrongSet.add(q.uid);
      }
      return { ...q, chosen, isCorrect };
    });
    saveSet(LS_WRONG, wrongSet);
    saveSet(LS_BOOKMARKS, session.bookmarked);

    renderResult(results);
    session.lastResults = results;
    showScreen("result");
    updateReviewButton();
  }

  function renderResult(results) {
    const total = results.length;
    const correctCount = results.filter(r => r.isCorrect).length;
    document.getElementById("score-big").textContent = `${correctCount}/${total}`;
    document.getElementById("score-pct").textContent = `${Math.round((correctCount / total) * 100)}%`;

    const kaStats = {};
    for (const r of results) {
      kaStats[r.ka] ??= { name: r.kaName || r.ka, total: 0, correct: 0 };
      kaStats[r.ka].total++;
      if (r.isCorrect) kaStats[r.ka].correct++;
    }
    const kaTable = document.getElementById("ka-table");
    const rows = Object.entries(kaStats)
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([ka, s]) => `<tr><td>${escapeHtml(s.name)}</td><td>${s.correct}/${s.total}</td><td>${Math.round((s.correct / s.total) * 100)}%</td></tr>`)
      .join("");
    kaTable.innerHTML = `<tr><th>Tab</th><th>Correct</th><th>%</th></tr>${rows}`;

    renderReviewList(results);
    document.getElementById("filter-wrong-only").checked = false;
  }

  function renderReviewList(results) {
    const container = document.getElementById("review-list");
    const wrongOnly = document.getElementById("filter-wrong-only").checked;
    const items = wrongOnly ? results.filter(r => !r.isCorrect) : results;
    container.innerHTML = items.map((r, i) => {
      const chosenText = r.chosen ? `${r.chosen}. ${escapeHtml(r.options[r.chosen])}` : "(not answered)";
      const correctText = `${r.correct}. ${escapeHtml(r.options[r.correct])}`;
      return `
        <div class="review-item ${r.isCorrect ? "correct" : "wrong"}">
          <div class="rq-head"><span>${escapeHtml(r.kaName || r.ka)}</span><span>${r.isCorrect ? "✓ Correct" : "✗ Incorrect"}</span></div>
          <p class="rq-text">${escapeHtml(r.question)}</p>
          <div class="rq-answer ${r.isCorrect ? "" : "wrong-ans"}">Your answer: ${chosenText}</div>
          ${!r.isCorrect ? `<div class="rq-answer correct-ans">Correct answer: ${correctText}</div>` : ""}
          <div class="rq-expl">${formatExplanation(r.explanation)}</div>
        </div>`;
    }).join("");
  }

  // ---------- theme ----------
  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    document.getElementById("theme-toggle").textContent = theme === "dark" ? "Light mode" : "Dark mode";
  }

  function initTheme() {
    const saved = localStorage.getItem(LS_THEME);
    const theme = saved || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    applyTheme(theme);
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute("data-theme");
    const next = current === "dark" ? "light" : "dark";
    localStorage.setItem(LS_THEME, next);
    applyTheme(next);
  }

  // ---------- wiring ----------
  function wireEvents() {
    document.getElementById("theme-toggle").addEventListener("click", toggleTheme);
    document.getElementById("source-select").addEventListener("change", (e) => {
      if (e.target.classList.contains("tier-toggle") || e.target.id === "mix-everything") {
        updateTierRowStates();
      }
    });

    document.getElementById("btn-start").addEventListener("click", () => {
      const source = getSelectedSource();
      const mode = document.querySelector('input[name="mode"]:checked').value;
      const kaFilter = getSelectedKAs();
      if (kaFilter.length === 0) { alert("Please select at least one topic group."); return; }
      const questions = buildQuestionList(source, kaFilter);
      startSession(questions, mode, false);
    });

    document.getElementById("btn-review").addEventListener("click", () => {
      const bookmarks = loadSet(LS_BOOKMARKS);
      const wrong = loadSet(LS_WRONG);
      const uids = [...new Set([...bookmarks, ...wrong])];
      const questions = shuffle(uids.map(u => QUESTIONS_BY_UID[u]).filter(Boolean));
      startSession(questions, "practice", true);
    });

    document.getElementById("btn-bookmark").addEventListener("click", toggleBookmark);
    document.getElementById("btn-prev").addEventListener("click", goPrev);
    document.getElementById("btn-next").addEventListener("click", goNext);
    document.getElementById("btn-submit").addEventListener("click", () => {
      if (confirm("Submit the exam now?")) finishSession();
    });
    document.getElementById("btn-exit-quiz").addEventListener("click", exitQuiz);

    const goHome = () => {
      session = null;
      showScreen("home");
      updateReviewButton();
    };
    document.getElementById("btn-back-home").addEventListener("click", goHome);
    document.getElementById("btn-back-home-fixed").addEventListener("click", goHome);
    document.getElementById("btn-review-wrong-now").addEventListener("click", () => {
      const wrongQuestions = session.lastResults.filter(r => !r.isCorrect).map(r => QUESTIONS_BY_UID[r.uid]);
      if (wrongQuestions.length === 0) { alert("No incorrect answers in this round!"); return; }
      startSession(shuffle(wrongQuestions), "practice", true);
    });
    document.getElementById("filter-wrong-only").addEventListener("change", () => {
      renderReviewList(session.lastResults);
    });
  }

  async function init() {
    initTheme();
    wireEvents();
    updateReviewButton();
    try {
      await loadData();
    } catch (err) {
      alert("Could not load exam data. If you're opening this file directly (file://), run a local server instead, e.g.: python3 -m http.server");
      console.error(err);
    }
  }

  init();
})();
