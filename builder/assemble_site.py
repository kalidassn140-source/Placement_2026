# builder/assemble_site.py
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding='utf-8')

from app_css import APP_CSS
from app_js import APP_JS

print("Assembling enhanced index.html...")

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>PrepMaster Pro — Complete Placement Preparation & Coding Practice Platform</title>

  <!-- PWA & Offline Manifest -->
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#3b82f6">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

  <!-- KaTeX CSS & JS for LaTeX Math Rendering -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>

  <style>
{APP_CSS}
  </style>
</head>
<body>

  <!-- TOPBAR -->
  <header class="topbar">
    <div class="topbar-left">
      <!-- Visible Three-Dot Navigation Menu Button -->
      <button class="three-dot-btn" id="three-dot-toggle" title="Open Syllabus Navigator (Three-dot Menu)" aria-label="Open Navigation">
        &#8942;
      </button>
      <div class="brand-title" onclick="navigateTo('welcome')">
        <span>PrepMaster <span style="color:var(--pri)">Pro</span></span>
        <span class="badge" id="global-verified-badge">32,900 Verified Qs (75/15/10 Rule)</span>
      </div>
    </div>

    <div class="topbar-right">
      <button class="btn" onclick="navigateTo('welcome')" title="Personal Welcome Dashboard">🏠 Home</button>
      <button class="btn" onclick="navigateTo('calendar')" title="Study Planner & Preparation Calendar">📅 Calendar</button>
      <button class="btn" onclick="navigateTo('catalog')" title="All Syllabus Topics">📚 Topics</button>
      <button class="btn btn-primary" onclick="navigateTo('coding_practice')" title="Interactive Coding Practice & Compiler">💻 Coding Practice</button>
      <button class="btn" onclick="navigateTo('custom_tests')" title="Mock Tests & Custom Exams">⏱️ Custom Tests</button>
      <button class="btn" onclick="navigateTo('formulas')" title="Formula Book">📐 Formulas</button>
      <button class="btn" onclick="navigateTo('study', CUR_TOPIC)" title="Study Notes">📖 Study</button>
      <button class="btn" onclick="navigateTo('reports')" title="Analytics & Progress">📊 Reports</button>
      <button class="btn" onclick="navigateTo('admin')" title="Content Management & Admin">⚙️ Admin</button>
      <button class="btn btn-sm" id="offline-status-btn" onclick="triggerOfflinePackDownload()" title="Click to download full offline question pack and verify PWA caching" style="display:flex;align-items:center;gap:6px;">
        <span id="offline-dot" style="width:8px;height:8px;border-radius:50%;background:#22c55e;display:inline-block;"></span>
        <span id="offline-status-text">Online</span>
      </button>
      <button class="btn" onclick="openShortcutsModal()" title="Keyboard Shortcuts Help">⌨️ Keys</button>

      <button class="btn btn-sm" id="theme-toggle-btn" onclick="toggleThemeQuick()" title="Switch Light/Dark Mode" style="font-weight:700;">🌓 Theme</button>
      <button class="user-btn" onclick="openSettingsModal()" title="User Profile & Settings">
        <div class="user-avatar" id="header-user-avatar">K</div>
        <span id="header-user-name">Kalidass S</span>
      </button>
    </div>
  </header>

  <!-- SIDEBAR DRAWER & BACKDROP -->
  <div id="sidebar-backdrop"></div>
  <aside id="sidebar" aria-label="Main Navigation">
    <div class="sidebar-header">
      <div style="display:flex;align-items:center;gap:8px">
        <b style="font-size:1.15rem">Syllabus Navigator</b>
        <span class="diff-pill easy" style="font-size:0.72rem">327 Topics</span>
      </div>
      <button class="btn btn-sm" onclick="toggleSidebar(false)">✕</button>
    </div>

    <div class="sidebar-nav">
      <button class="btn btn-sm" onclick="navigateTo('welcome')">🏠 Home Dashboard</button>
      <button class="btn btn-sm" onclick="navigateTo('calendar')">📅 Study Calendar</button>
      <button class="btn btn-sm" onclick="navigateTo('catalog')">📚 Question Catalog</button>
      <button class="btn btn-sm btn-primary" onclick="navigateTo('coding_practice')">💻 Coding Practice & IDE</button>
      <button class="btn btn-sm" onclick="navigateTo('custom_tests')">⏱️ Mock Tests</button>
      <button class="btn btn-sm" onclick="navigateTo('practice', CUR_TOPIC)">⚡ Practice Mode</button>
      <button class="btn btn-sm" onclick="navigateTo('study', CUR_TOPIC)">📖 Study Guides</button>
      <button class="btn btn-sm" onclick="navigateTo('formulas')">📐 Formula Book</button>
      <button class="btn btn-sm" onclick="navigateTo('bookmarks')">★ Bookmarks</button>
      <button class="btn btn-sm" onclick="navigateTo('reports')">📊 Analytics</button>
      <button class="btn btn-sm" onclick="navigateTo('admin')">⚙️ Protected Admin</button>
    </div>

    <!-- 4 DROPDOWN SELECTORS FOR SYLLABUS -->
    <div id="sidebar-dropdowns-container" class="sidebar-dropdowns-container"></div>

    <div class="sidebar-topic-list" id="sidebar-topics-container">
      <!-- Generated dynamically from catalog -->
    </div>
  </aside>

  <!-- MAIN CONTAINER -->
  <main class="container">

    <!-- VIEW 0: WELCOME DASHBOARD -->
    <div id="welcome-view">
      <div id="welcome-container"></div>
    </div>

    <!-- VIEW 1: CATALOG VIEW -->
    <div id="catalog-view" style="display:none;">
      <!-- CATEGORY SWITCHER TABS -->
      <div class="category-tabs">
        <button class="cat-tab-btn active" data-cat="all">All Categories (327 Topics)</button>
        <button class="cat-tab-btn" data-cat="Coding Questions">💻 Coding Questions (166 Topics)</button>
        <button class="cat-tab-btn" data-cat="Quantitative Aptitude">📐 Quantitative Aptitude (74 Topics)</button>
        <button class="cat-tab-btn" data-cat="Verbal Ability and Logical Reasoning">🧠 Verbal & Logical (87 Topics)</button>
        <button class="cat-tab-btn" data-cat="Coding IDE" onclick="navigateTo('coding_practice')" style="background:var(--card-subtle);border-color:var(--pri);">⚡ Coding IDE & LeetCode (<span id="cat-tab-coding-count">1,540</span> Problems)</button>
      </div>

      <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap;">
        <div style="flex:1;min-width:280px;">
          <input type="text" id="catalog-search-input" class="search-input" placeholder="🔍 Search any topic across all 327 subjects (e.g. Binary Search, Dynamic Programming, Percentage, Syllogisms)...">
        </div>
        <div style="display:flex;gap:8px;align-items:center;">
          <span class="diff-pill easy" id="catalog-count-pill">327 Topics</span>
          <button class="btn btn-sm" onclick="navigateTo('practice', 'coding_pf_basic')">⚡ Quick Start Practice</button>
        </div>
      </div>
      <div class="topic-grid" id="catalog-grid"></div>
    </div>

    <!-- VIEW 2: PRACTICE VIEW -->
    <div id="practice-view" style="display:none;">
      <div id="practice-card-container"></div>
    </div>

    <!-- VIEW 3: TEST VIEW -->
    <div id="test-view" style="display:none;">
      <div style="display:flex;justify-content:space-between;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 18px;margin-bottom:16px;flex-wrap:wrap;gap:10px;">
        <div style="font-weight:700;font-size:1.1rem;">⏱️ Mock Examination Mode</div>
        <div style="display:flex;align-items:center;gap:12px;">
          <span>Time Remaining:</span>
          <span id="test-timer-display" style="font-size:1.35rem;font-weight:900;color:var(--pri);font-family:monospace;">60:00</span>
          <button class="btn btn-primary btn-sm" onclick="confirmSubmitTest()" style="background:var(--ok);border-color:var(--ok);">Submit Test</button>
        </div>
      </div>

      <div class="test-layout">
        <div id="test-card-container"></div>
        <div id="test-palette-container"></div>
      </div>
    </div>

    <!-- VIEW 4: TEST RESULT VIEW -->
    <div id="test-result-view" style="display:none;">
      <div id="test-result-container"></div>
    </div>

    <!-- VIEW 5: CODING PRACTICE (TOPIC LIST & PROBLEMS) -->
    <div id="coding-practice-view" style="display:none;">
      <div id="coding-practice-container"></div>
    </div>

    <!-- VIEW 6: CODING PRACTICE IDE & COMPILER -->
    <div id="coding-ide-view" style="display:none;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:10px;background:var(--card);padding:10px 16px;border-radius:var(--radius);border:1px solid var(--line);">
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
          <button class="btn btn-sm" onclick="navigateTo('coding_practice')">← Browse 29 Topics (1,540 Probs)</button>
          <select id="ide-topic-select" class="search-input" style="width:200px;padding:4px 8px;" onchange="handleIDETopicChange(this.value)">
            <!-- Populated dynamically with 29 topics -->
          </select>
          <select id="ide-problem-select" class="search-input" style="width:260px;padding:4px 8px;" onchange="openCodingIDE(this.value)">
            <!-- Populated dynamically with problems -->
          </select>
        </div>
        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
          <button class="btn btn-sm" onclick="prevCodingProblem()" title="Previous problem">← Prev</button>
          <button class="btn btn-sm btn-primary" onclick="nextCodingProblem()" title="Next problem">Next →</button>
          <button class="btn btn-sm" onclick="resetIDECode()">Reset</button>
          <button class="btn btn-sm" onclick="clearIDEEditor()">Clear</button>
        </div>
      </div>

      <div class="coding-ide-layout">
        <!-- LEFT: PROBLEM DESCRIPTION & TEST CASES -->
        <div class="coding-desc-panel" id="ide-problem-desc">
          <!-- Populated dynamically -->
        </div>

        <!-- RIGHT: CODE EDITOR & EXECUTION RUNNER -->
        <div class="coding-editor-panel">
          <div class="editor-topbar">
            <div style="display:flex;align-items:center;gap:8px;">
              <span style="font-size:0.85rem;font-weight:700;">Language:</span>
              <select id="ide-lang-select" class="search-input" style="width:130px;padding:4px 8px;" onchange="handleIDELangChange(this.value)">
                <option value="python">Python 3</option>
                <option value="c">C (GCC)</option>
                <option value="cpp">C++ (G++)</option>
                <option value="java">Java 17</option>
                <option value="javascript">JavaScript (Node)</option>
                <option value="sql">SQL (SQLite)</option>
                <option value="html">HTML5 / CSS</option>
              </select>
            </div>
            <div style="display:flex;gap:8px;">
              <button class="btn btn-sm" onclick="runIDECode(false)">▶ Run Code</button>
              <button class="btn btn-sm btn-primary" onclick="runIDECode(true)" style="background:var(--ok);border-color:var(--ok);">Submit Solution ✓</button>
            </div>
          </div>

          <div class="editor-container-wrapper">
            <div class="editor-gutter" id="ide-gutter">1<br>2<br>3<br>4<br>5</div>
            <div class="code-editor-surface">
              <pre class="highlight-layer" id="ide-highlight-layer" aria-hidden="true"><code id="ide-highlight-code"></code></pre>
              <textarea id="ide-code-textarea" class="code-textarea" spellcheck="false" autocomplete="off" autocorrect="off" autocapitalize="off" oninput="handleCodeInput()" onscroll="syncHighlightScroll()" onkeydown="handleEditorKeyDown(event)"></textarea>
            </div>
          </div>

          <!-- TERMINAL & CONSOLE PANEL -->
          <div class="editor-console-panel" id="ide-console-panel">
            <div class="console-topbar">
              <div class="console-tabs">
                <button class="console-tab-btn active" id="tab-btn-output" onclick="switchConsoleTab('output')">📊 Test Results & 5 Test Cases</button>
                <button class="console-tab-btn" id="tab-btn-custom" onclick="switchConsoleTab('custom')">⚙️ Custom Input & Custom Output</button>
              </div>
              <button class="console-expand-btn" id="ide-expand-btn" onclick="toggleConsoleExpand()" title="Toggle expanded console mode">
                <span id="ide-expand-icon">⤢</span> <span id="ide-expand-text">Expand Console</span>
              </button>
            </div>

            <!-- TAB 1: 5 TEST CASES & VERDICT RESULTS -->
            <div id="console-view-output" style="display:flex;flex-direction:column;flex:1;overflow-y:auto;padding:12px;">
              <div id="ide-verdict-banner"></div>
              <div class="console-output-content" id="ide-console-output" style="margin-bottom:8px;">Ready. Click 'Run Code' or 'Submit Solution' to execute across 5 test cases.</div>
              <div id="ide-testcases-table-container"></div>
              <iframe id="ide-html-preview-frame" style="display:none;width:100%;height:220px;border:1px solid var(--line);background:white;border-radius:6px;margin-top:8px;"></iframe>
            </div>

            <!-- TAB 2: DEDICATED CUSTOM INPUT AND CUSTOM OUTPUT -->
            <div id="console-view-custom" style="display:none;flex:1;overflow-y:auto;padding:12px;">
              <div class="custom-io-container">
                <div class="custom-io-col">
                  <label for="ide-custom-input">
                    <span>Standard Input (stdin)</span>
                    <button class="btn btn-sm btn-primary" onclick="runCustomInput()" style="padding:4px 10px;font-size:0.8rem;">▶ Run Custom Input</button>
                  </label>
                  <textarea id="ide-custom-input" class="custom-io-textarea" placeholder="Provide test arguments, matrices, integers, or strings to pass into your code..."></textarea>
                </div>
                <div class="custom-io-col">
                  <label for="ide-custom-stdout">
                    <span>Standard Output (stdout)</span>
                    <span id="ide-custom-meta" style="font-size:0.78rem;color:var(--mut);">Status: Idle</span>
                  </label>
                  <pre id="ide-custom-stdout" class="custom-stdout-box">(Custom execution output will appear here after clicking 'Run Custom Input')</pre>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- VIEW 7: CUSTOM TESTS -->
    <div id="custom-tests-view" style="display:none;">
      <div id="custom-tests-container"></div>
    </div>

    <!-- VIEW 8: STUDY MATERIAL VIEW -->
    <div id="study-view" style="display:none;">
      <div id="study-container"></div>
    </div>

    <!-- VIEW 9: FORMULA BOOK VIEW -->
    <div id="formulas-view" style="display:none;">
      <div style="margin-bottom:20px;">
        <h2>📐 Dedicated Formula Book & Mathematical Reference</h2>
        <input type="text" id="formula-search-input" class="search-input" placeholder="Search formulas by name, concept, or variable..." oninput="renderFormulaBook()">
      </div>
      <div class="formula-grid" id="formulas-container"></div>
    </div>

    <!-- VIEW 10: PERFORMANCE REPORTS VIEW -->
    <div id="reports-view" style="display:none;">
      <div id="reports-container"></div>
    </div>

    <!-- VIEW 11: ADMIN & CONTENT MANAGEMENT VIEW -->
    <div id="admin-view" style="display:none;">
      <div id="admin-container"></div>
    </div>

    <!-- VIEW 12: BOOKMARKS VIEW -->
    <div id="bookmarks-view" style="display:none;">
      <div id="bookmarks-container"></div>
    </div>

    <!-- VIEW 13: PREPARATION CALENDAR & STUDY OF THE DAY -->
    <div id="calendar-view" style="display:none;">
      <div class="calendar-wrapper">
        <div class="calendar-header-bar">
          <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
            <h2 class="calendar-month-title" id="calendar-month-heading" style="margin:0;">📅 Preparation Calendar & Study Schedule</h2>
            <div style="display:flex;gap:6px;">
              <button class="btn btn-sm" onclick="changeCalendarMonth(-1)">◀ Prev</button>
              <button class="btn btn-sm" onclick="goToCalendarToday()">Today</button>
              <button class="btn btn-sm" onclick="changeCalendarMonth(1)">Next ▶</button>
            </div>
          </div>
          <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap;">
            <span class="diff-pill easy" id="cal-streak-pill" style="font-size:0.85rem;padding:6px 12px;">🔥 Study Consistency Tracker</span>
            <button class="btn btn-primary btn-sm" onclick="openCalendarDayPortal(getTodayDateStr())">+ Plan Today's Study Topics</button>
          </div>
        </div>

        <div style="font-size:0.92rem;color:var(--mut);margin-bottom:16px;">
          Click on any date to assign or practice <b>Coding of the Day</b>, <b>Quantitative Aptitude of the Day</b>, and <b>Verbal & Logical Reasoning of the Day</b>.
        </div>

        <div class="calendar-grid" id="calendar-grid-container">
          <!-- Populated dynamically with calendar days -->
        </div>
      </div>
    </div>

  </main>

  <!-- ------------------------------------------------------------- -->
  <!-- MODAL: CODING TOPIC PROBLEMS BROWSER -->
  <!-- ------------------------------------------------------------- -->
  <div id="coding-topic-modal" class="modal-backdrop">
    <div class="modal-dialog modal-lg">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <h3 style="margin:0;" id="coding-modal-title">Problems</h3>
        <button class="btn btn-sm" onclick="closeCodingTopicModal()">✕</button>
      </div>
      <div id="coding-modal-problem-list" style="max-height:65vh;overflow-y:auto;"></div>
    </div>
  </div>

  <!-- ------------------------------------------------------------- -->
  <!-- MODAL: CREATE CUSTOM TEST (ADMIN ONLY) -->
  <!-- ------------------------------------------------------------- -->
  <div id="create-test-modal" class="modal-backdrop">
    <div class="modal-dialog modal-lg">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <h3 style="margin:0;">Create Custom Examination / Mock Test</h3>
        <button class="btn btn-sm" onclick="closeCreateTestModal()">✕</button>
      </div>

      <div style="display:flex;flex-direction:column;gap:14px;">
        <div>
          <label style="font-weight:600;font-size:0.85rem;">Test Name</label>
          <input type="text" id="ct-name" class="search-input" placeholder="e.g. Placement Round 1 Mock 01" style="margin-top:4px;">
        </div>

        <div>
          <label style="font-weight:600;font-size:0.85rem;">Description (Optional)</label>
          <input type="text" id="ct-desc" class="search-input" placeholder="e.g. Comprehensive 50-question placement simulation" style="margin-top:4px;">
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;">
          <div>
            <label style="font-weight:600;font-size:0.85rem;">Total Questions</label>
            <input type="number" id="ct-qcount" class="search-input" value="30" min="5" max="200" style="margin-top:4px;">
          </div>
          <div>
            <label style="font-weight:600;font-size:0.85rem;">Duration (Minutes)</label>
            <input type="number" id="ct-duration" class="search-input" value="60" min="0" max="300" style="margin-top:4px;">
          </div>
          <div>
            <label style="font-weight:600;font-size:0.85rem;">Difficulty</label>
            <select id="ct-diff" class="search-input" style="margin-top:4px;">
              <option value="all">All Difficulties (Standard Distribution)</option>
              <option value="Hard">Hard Only (75% Level)</option>
              <option value="Medium">Medium Only</option>
              <option value="Easy">Easy Only</option>
            </select>
          </div>
        </div>

        <div style="display:flex;gap:20px;">
          <label style="display:flex;align-items:center;gap:6px;font-size:0.9rem;">
            <input type="checkbox" id="ct-rand-q" checked> Randomize Question Order
          </label>
          <label style="display:flex;align-items:center;gap:6px;font-size:0.9rem;">
            <input type="checkbox" id="ct-rand-o" checked> Randomize Options
          </label>
        </div>

        <div>
          <label style="font-weight:600;font-size:0.85rem;margin-bottom:6px;display:block;">Select Syllabus Topics to Include</label>
          <div id="create-test-topic-list" style="max-height:220px;overflow-y:auto;border:1px solid var(--line);border-radius:8px;padding:10px;"></div>
        </div>

        <div style="display:flex;justify-content:flex-end;gap:10px;border-top:1px solid var(--line);padding-top:14px;">
          <button class="btn" onclick="closeCreateTestModal()">Cancel</button>
          <button class="btn btn-primary" onclick="saveCustomTestFromForm()">Create & Save Test</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ------------------------------------------------------------- -->
  <!-- MODAL: ADD QUESTION WIZARD (ADMIN ONLY) -->
  <!-- ------------------------------------------------------------- -->
  <div id="add-question-modal" class="modal-backdrop">
    <div class="modal-dialog modal-lg">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <h3 style="margin:0;">+ Add Verified Question (Admin Only)</h3>
        <button class="btn btn-sm" onclick="closeAddQuestionModal()">✕</button>
      </div>

      <div style="display:flex;flex-direction:column;gap:14px;">
        <!-- STEP 1 & 2: CATEGORY & TOPIC -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
          <div>
            <label style="font-weight:600;font-size:0.85rem;">Step 1: Category</label>
            <select id="aq-category" class="search-input" style="margin-top:4px;" onchange="handleAQCategoryChange(this.value)"></select>
          </div>
          <div>
            <label style="font-weight:600;font-size:0.85rem;">Step 2: Topic</label>
            <select id="aq-topic" class="search-input" style="margin-top:4px;"></select>
          </div>
        </div>

        <!-- STEP 3: DETAILS -->
        <div>
          <label style="font-weight:600;font-size:0.85rem;">Step 3: Question Statement</label>
          <textarea id="aq-statement" class="search-input" style="height:70px;margin-top:4px;" placeholder="Enter complete question statement..."></textarea>
        </div>

        <div>
          <label style="font-weight:600;font-size:0.85rem;">Optional Code Snippet or Diagram</label>
          <textarea id="aq-code" class="search-input" style="height:50px;font-family:monospace;margin-top:4px;" placeholder="Optional code block or diagram description..."></textarea>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
          <div>
            <label style="font-size:0.82rem;font-weight:600;">Option A</label>
            <input type="text" id="aq-opt-a" class="search-input" placeholder="Option A text">
          </div>
          <div>
            <label style="font-size:0.82rem;font-weight:600;">Option B</label>
            <input type="text" id="aq-opt-b" class="search-input" placeholder="Option B text">
          </div>
          <div>
            <label style="font-size:0.82rem;font-weight:600;">Option C</label>
            <input type="text" id="aq-opt-c" class="search-input" placeholder="Option C text">
          </div>
          <div>
            <label style="font-size:0.82rem;font-weight:600;">Option D</label>
            <input type="text" id="aq-opt-d" class="search-input" placeholder="Option D text">
          </div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
          <div>
            <label style="font-weight:600;font-size:0.85rem;">Verified Correct Option</label>
            <select id="aq-correct-idx" class="search-input" style="margin-top:4px;">
              <option value="0">Option A</option>
              <option value="1">Option B</option>
              <option value="2">Option C</option>
              <option value="3">Option D</option>
            </select>
          </div>
          <div>
            <label style="font-weight:600;font-size:0.85rem;">Difficulty Classification</label>
            <select id="aq-diff" class="search-input" style="margin-top:4px;">
              <option value="Hard">Hard (75% Standard)</option>
              <option value="Medium">Medium (10% Standard)</option>
              <option value="Easy">Easy (15% Standard)</option>
            </select>
          </div>
        </div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
          <div>
            <label style="font-weight:600;font-size:0.85rem;">Hint (Strategy Clue)</label>
            <input type="text" id="aq-hint" class="search-input" placeholder="Clue that nudges without giving away answer">
          </div>
          <div>
            <label style="font-weight:600;font-size:0.85rem;">Analysis Technique / Rule</label>
            <input type="text" id="aq-tech" class="search-input" placeholder="e.g. Master Theorem Case 2">
          </div>
        </div>

        <div>
          <label style="font-weight:600;font-size:0.85rem;">Explanation of Correct & Incorrect Options</label>
          <textarea id="aq-explanation" class="search-input" style="height:60px;" placeholder="Detailed justification..."></textarea>
        </div>

        <div>
          <label style="font-weight:600;font-size:0.85rem;">Step-by-Step Solution</label>
          <textarea id="aq-step" class="search-input" style="height:60px;" placeholder="Step 1: ...&#10;Step 2: ..."></textarea>
        </div>

        <!-- STEP 4: PREVIEW -->
        <div style="border-top:1px solid var(--line);padding-top:10px;">
          <button class="btn btn-sm" onclick="previewNewQuestion()">Step 4: Live Preview Question</button>
          <div id="aq-preview-box" style="margin-top:10px;"></div>
        </div>

        <!-- STEP 5: SAVE -->
        <div style="display:flex;justify-content:flex-end;gap:10px;border-top:1px solid var(--line);padding-top:14px;">
          <button class="btn" onclick="closeAddQuestionModal()">Cancel</button>
          <button class="btn btn-sm" onclick="saveNewQuestion(true)">Save & Add Another</button>
          <button class="btn btn-primary" onclick="saveNewQuestion(false)">Save Question</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ------------------------------------------------------------- -->
  <!-- MODAL: SETTINGS & APPEARANCE -->
  <!-- ------------------------------------------------------------- -->
  <div id="settings-modal" class="modal-backdrop">
    <div class="modal-dialog">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <h3 style="margin:0;">User Profile & Personalization</h3>
        <button class="btn btn-sm" onclick="closeSettingsModal()">✕</button>
      </div>

      <div style="display:flex;flex-direction:column;gap:16px;">
        <div>
          <label style="font-weight:600;font-size:0.9rem;">Display Theme</label>
          <select id="theme-select" class="search-input" style="margin-top:6px;" onchange="handleAdminThemeSelect(this.value)">
            <option value="dark">Dark Theme (Recommended)</option>
            <option value="light">Light Theme</option>
            <option value="forest">Emerald Forest</option>
            <option value="dragon">Dragon Crimson</option>
            <option value="ocean">Deep Ocean</option>
            <option value="wizard">Arcane Wizard Purple</option>
            <option value="fairy">Fairy Blossom</option>
            <option value="royal">Royal Amber</option>
          </select>
        </div>

        <div style="border-top:1px solid var(--line);padding-top:16px;display:flex;justify-content:space-between;align-items:center;">
          <button class="btn btn-sm" onclick="closeSettingsModal(); navigateTo('admin');">Open Full Admin Settings →</button>
          <button class="btn btn-primary" onclick="closeSettingsModal()">Close</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ------------------------------------------------------------- -->
  <!-- MODAL: SHORTCUTS GUIDE -->
  <!-- ------------------------------------------------------------- -->
  <div id="shortcuts-modal" class="modal-backdrop">
    <div class="modal-dialog">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
        <h3 style="margin:0;">⌨️ Complete Keyboard Shortcuts Reference</h3>
        <button class="btn btn-sm" onclick="closeShortcutsModal()">✕</button>
      </div>

      <div style="display:flex;flex-direction:column;gap:16px;font-size:0.9rem;">
        <div>
          <h4 style="color:var(--pri);margin:0 0 6px 0;">⚡ Practice Mode Shortcuts</h4>
          <table style="width:100%;border-collapse:collapse;">
            <tr><td style="padding:4px 0;"><b>Up / Down Arrow</b></td><td>Move focus between options</td></tr>
            <tr><td style="padding:4px 0;"><b>Enter</b></td><td>Select focused option; if answered, advance to next question</td></tr>
            <tr><td style="padding:4px 0;"><b>1, 2, 3, 4 or A, B, C, D</b></td><td>Select corresponding option immediately</td></tr>
            <tr><td style="padding:4px 0;"><b>Left / Right Arrow</b></td><td>Previous / Next question</td></tr>
            <tr><td style="padding:4px 0;"><b>H</b></td><td>Show or hide hint clue</td></tr>
            <tr><td style="padding:4px 0;"><b>S</b></td><td>Show verified correct answer & solution</td></tr>
            <tr><td style="padding:4px 0;"><b>R</b></td><td>Reset current question attempt</td></tr>
            <tr><td style="padding:4px 0;"><b>M</b></td><td>Switch to Test mode for this topic</td></tr>
          </table>
        </div>

        <div style="border-top:1px solid var(--line);padding-top:10px;">
          <h4 style="color:var(--purple);margin:0 0 6px 0;">⏱️ Test Mode Shortcuts</h4>
          <table style="width:100%;border-collapse:collapse;">
            <tr><td style="padding:4px 0;"><b>1, 2, 3, 4 / A, B, C, D</b></td><td>Record answer and advance to next question</td></tr>
            <tr><td style="padding:4px 0;"><b>Left / Right Arrow</b></td><td>Previous / Next question</td></tr>
            <tr><td style="padding:4px 0;"><b>Shift + Enter</b></td><td>Submit examination (with confirmation)</td></tr>
            <tr><td style="padding:4px 0;"><b>M</b></td><td>Switch to Practice mode</td></tr>
          </table>
        </div>

        <div style="border-top:1px solid var(--line);padding-top:10px;">
          <h4 style="color:var(--ok);margin:0 0 6px 0;">🌐 Global & Study Navigation</h4>
          <table style="width:100%;border-collapse:collapse;">
            <tr><td style="padding:4px 0;"><b>[ and ]</b></td><td>Cycle main categories (Coding, Quant, Verbal)</td></tr>
            <tr><td style="padding:4px 0;"><b>Ctrl + Left / Right</b></td><td>Previous / Next category</td></tr>
            <tr><td style="padding:4px 0;"><b>/ (Forward Slash)</b></td><td>Focus study material search field</td></tr>
            <tr><td style="padding:4px 0;"><b>Escape</b></td><td>Close any open modal or navigation drawer</td></tr>
          </table>
        </div>

        <div style="border-top:1px solid var(--line);padding-top:12px;text-align:right;">
          <button class="btn btn-primary" onclick="closeShortcutsModal()">Got It</button>
        </div>
      </div>
    </div>
  </div>

  <script>
    function switchConsoleTab(tab) {{
      $('#tab-btn-output').classList.toggle('active', tab === 'output');
      $('#tab-btn-input').classList.toggle('active', tab === 'input');
      $('#console-view-output').style.display = (tab === 'output') ? 'flex' : 'none';
      $('#console-view-input').style.display = (tab === 'input') ? 'block' : 'none';
    }}
  </script>

  <!-- LOAD PRESERVED QUESTION BANKS -->
  <script src="data/catalog_and_meta.js"></script>
  <script src="data/coding_part1.js"></script>
  <script src="data/coding_part2.js"></script>
  <script src="data/quant_questions.js"></script>
  <script src="data/verbal_logical_questions.js"></script>

  <!-- LOAD NEW CODING PRACTICE & COMPILER PROBLEM BANK -->
  <script src="data/coding_practice_problems.js"></script>

  <!-- LOAD AUDIT SUMMARY & DUPLICATES ARCHIVE PREVIEW -->
  <script src="data/audit_data.js"></script>
  <script src="data/duplicates_preview.js"></script>

  <!-- ------------------------------------------------------------- -->
  <!-- MODAL: REVIEW SUSPECTED DUPLICATES (SIDE-BY-SIDE COMPARISON) -->
  <!-- ------------------------------------------------------------- -->
  <div id="review-duplicates-modal" class="modal-backdrop">
    <div class="modal-dialog modal-lg" style="max-width:920px;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid var(--line);padding-bottom:10px;">
        <div style="display:flex;align-items:center;gap:10px;">
          <h3 style="margin:0;">🔍 Suspected Duplicate Comparison</h3>
          <span class="diff-pill hard" id="dup-similarity-pill">94% Semantic Match</span>
        </div>
        <button class="btn btn-sm" onclick="closeReviewDuplicatesModal()">✕</button>
      </div>

      <div style="display:flex;gap:12px;margin-bottom:14px;background:var(--card-subtle);padding:10px 14px;border-radius:8px;font-size:0.85rem;border:1px solid var(--line);flex-wrap:wrap;">
        <div><b>Topic:</b> <span id="dup-modal-topic">For Loops</span></div>
        <div>&bull;</div>
        <div><b>Category:</b> <span id="dup-modal-category">Coding IDE</span></div>
        <div>&bull;</div>
        <div><b>Duplicate Flag:</b> <span id="dup-modal-reason">Template Clone / Identical Logic</span></div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">
        <div style="background:var(--card);border:1px solid var(--line);border-radius:8px;padding:14px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
            <b style="color:var(--pri);">Record A (Retained / Canonical)</b>
            <span class="diff-pill easy" id="dup-rec-a-id">rec_a_001</span>
          </div>
          <div id="dup-rec-a-statement" style="font-size:0.95rem;line-height:1.55;margin-bottom:10px;white-space:pre-wrap;background:var(--bg);padding:10px;border-radius:6px;border:1px solid var(--line);"></div>
          <div id="dup-rec-a-meta" style="font-size:0.82rem;color:var(--mut);"></div>
        </div>

        <div style="background:var(--card);border:1px solid var(--badBorder);border-radius:8px;padding:14px;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
            <b style="color:var(--bad);">Record B (Suspected Duplicate)</b>
            <span class="diff-pill hard" id="dup-rec-b-id">rec_b_002</span>
          </div>
          <div id="dup-rec-b-statement" style="font-size:0.95rem;line-height:1.55;margin-bottom:10px;white-space:pre-wrap;background:var(--bg);padding:10px;border-radius:6px;border:1px solid var(--badBorder);"></div>
          <div id="dup-rec-b-meta" style="font-size:0.82rem;color:var(--mut);"></div>
        </div>
      </div>

      <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:14px;flex-wrap:wrap;gap:10px;">
        <div style="font-size:0.84rem;color:var(--mut);">
          Actions apply to the active in-memory dataset and audit log.
        </div>
        <div style="display:flex;gap:10px;">
          <button class="btn btn-sm" onclick="approveRecordAsUnique()">Approve as Unique ✓</button>
          <button class="btn btn-sm" style="color:var(--bad);border-color:var(--bad);" onclick="archiveSuspectedDuplicate()">Archive Duplicate 🗄️</button>
          <button class="btn btn-sm btn-primary" onclick="closeReviewDuplicatesModal()">Close</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ------------------------------------------------------------- -->
  <!-- MODAL: ARCHIVED DUPLICATES VIEWER -->
  <!-- ------------------------------------------------------------- -->
  <div id="archived-duplicates-modal" class="modal-backdrop">
    <div class="modal-dialog modal-lg" style="max-width:960px;">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid var(--line);padding-bottom:10px;">
        <div>
          <h3 style="margin:0;">🗄️ Recoverable Duplicates Archive</h3>
          <div style="font-size:0.85rem;color:var(--mut);margin-top:2px;">
            Safely preserved duplicate records &bull; <span id="archive-modal-count">24,137</span> Total Archived Records
          </div>
        </div>
        <div style="display:flex;gap:8px;">
          <button class="btn btn-sm" onclick="downloadArchivedDuplicatesJSON()">💾 Download Full Archive (JSON)</button>
          <button class="btn btn-sm" onclick="closeArchivedDuplicatesModal()">✕</button>
        </div>
      </div>

      <div style="display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap;">
        <input type="text" id="archive-search-input" class="search-input" placeholder="🔍 Search archived questions or topics..." style="flex:1;min-width:260px;" oninput="filterArchivedDuplicatesList()">
        <select id="archive-filter-reason" class="search-input" style="width:200px;" onchange="filterArchivedDuplicatesList()">
          <option value="all">All Duplicate Types</option>
          <option value="template_clone">Template Clones</option>
          <option value="exact_text">Exact Duplicates</option>
        </select>
      </div>

      <div id="archive-records-container" style="max-height:55vh;overflow-y:auto;border:1px solid var(--line);border-radius:8px;padding:10px;display:flex;flex-direction:column;gap:10px;background:var(--bg);">
        <!-- Populated dynamically -->
      </div>

      <div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:12px;margin-top:12px;">
        <span style="font-size:0.84rem;color:var(--mut);" id="archive-pagination-info">Showing records 1 - 50 of 24,137</span>
        <button class="btn btn-primary btn-sm" onclick="closeArchivedDuplicatesModal()">Close</button>
      </div>
    </div>
  </div>

  <!-- CALENDAR DAY STUDY PORTAL & ASSIGNMENT MODAL -->
  <div id="calendar-day-modal" class="modal-backdrop">
    <div class="modal-dialog modal-lg">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid var(--line);padding-bottom:10px;">
        <div>
          <h3 style="margin:0;font-size:1.3rem;" id="cal-modal-title">📅 Study Plan for Date</h3>
          <div style="font-size:0.85rem;color:var(--mut);margin-top:2px;">Select daily topics or jump straight into practice.</div>
        </div>
        <button class="btn btn-sm" onclick="closeCalendarDayModal()">✕</button>
      </div>
      <div id="cal-modal-body">
        <!-- Dynamic topic assignment dropdowns & practice links -->
      </div>
    </div>
  </div>

  <!-- APPLICATION ENGINE SCRIPT -->
  <script>
{APP_JS}
  </script>
</body>
</html>
"""

out_html = "f:/placement/1round ready2/index.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Enhanced index.html assembled successfully! Size: {os.path.getsize(out_html) / 1024:.2f} KB")
