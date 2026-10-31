# builder/app_css.py

APP_CSS = """
:root, :root[data-theme="light"] {
  --bg: #f8fafc;
  --card: #ffffff;
  --card-subtle: #f1f5f9;
  --ink: #0f172a;
  --mut: #475569;
  --pri: #2563eb;
  --priL: #dbeafe;
  --priHover: #1d4ed8;
  --ok: #16a34a;
  --okL: #dcfce7;
  --okBorder: #86efac;
  --bad: #dc2626;
  --badL: #fee2e2;
  --badBorder: #fca5a5;
  --line: #cbd5e1;
  --warn: #d97706;
  --warnL: #fef3c7;
  --purple: #7c3aed;
  --purpleL: #ede9fe;
  --maxw: 100%;
  --font-size: 16px;
  --card-pad: 20px;
  --radius: 12px;
  --shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
}

:root[data-theme="dark"] {
  --bg: #0b1017;
  --card: #151d28;
  --card-subtle: #1a2332;
  --ink: #f1f5f9;
  --mut: #94a3b8;
  --pri: #3b82f6;
  --priL: #1e2d42;
  --priHover: #60a5fa;
  --ok: #22c55e;
  --okL: #132f1e;
  --okBorder: #166534;
  --bad: #ef4444;
  --badL: #3b1717;
  --badBorder: #991b1b;
  --line: #243142;
  --warn: #f59e0b;
  --warnL: #362912;
  --purple: #a855f7;
  --purpleL: #2e1d44;
  --maxw: 100%;
  --shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

:root[data-theme="forest"] {
  --bg: #091811; --card: #11261c; --card-subtle: #173326; --ink: #e8f5ee; --mut: #8eb39d;
  --pri: #10b981; --priL: #163e2c; --priHover: #34d399; --ok: #22c55e; --okL: #132f1e;
  --bad: #f87171; --badL: #3b1717; --line: #1c422f; --warn: #fbbf24; --maxw: 100%;
}

:root[data-theme="dragon"] {
  --bg: #140d12; --card: #22141e; --card-subtle: #2d1b28; --ink: #fde8ef; --mut: #b88da0;
  --pri: #f43f5e; --priL: #3d1724; --priHover: #fb7185; --ok: #10b981; --okL: #132f1e;
  --bad: #ff3344; --badL: #451216; --line: #3d2335; --warn: #fbbf24; --maxw: 100%;
}

:root[data-theme="ocean"] {
  --bg: #071924; --card: #0e2738; --card-subtle: #13334a; --ink: #e0f2fe; --mut: #7dd3fc;
  --pri: #0284c7; --priL: #133e5c; --priHover: #38bdf8; --ok: #14b8a6; --okL: #0d332f;
  --bad: #f43f5e; --badL: #3d1724; --line: #194663; --warn: #f59e0b; --maxw: 100%;
}

:root[data-theme="wizard"] {
  --bg: #0d0b1a; --card: #17132e; --card-subtle: #201b40; --ink: #f3e8ff; --mut: #c084fc;
  --pri: #9333ea; --priL: #2c164a; --priHover: #c084fc; --ok: #10b981; --okL: #132f1e;
  --bad: #f43f5e; --badL: #3d1724; --line: #31285e; --warn: #fbbf24; --maxw: 100%;
}

:root[data-theme="fairy"] {
  --bg: #fdf2f8; --card: #ffffff; --card-subtle: #fce7f3; --ink: #3b0764; --mut: #86198f;
  --pri: #c026d3; --priL: #fae8ff; --priHover: #e879f9; --ok: #16a34a; --okL: #dcfce7;
  --bad: #dc2626; --badL: #fee2e2; --line: #f5d0fe; --warn: #d97706; --maxw: 100%;
}

:root[data-theme="royal"] {
  --bg: #fcf9f2; --card: #ffffff; --card-subtle: #f7f0e3; --ink: #451a03; --mut: #78350f;
  --pri: #b45309; --priL: #fef3c7; --priHover: #d97706; --ok: #15803d; --okL: #dcfce7;
  --bad: #b91c1c; --badL: #fee2e2; --line: #fde68a; --warn: #b45309; --maxw: 100%;
}

* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: var(--font-size);
  line-height: 1.55;
  transition: background 0.2s, color 0.2s;
  overflow-x: hidden;
}

/* TOPBAR */
header.topbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--card);
  border-bottom: 1px solid var(--line);
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
}
.topbar-left {
  display: flex;
  align-items: center;
  gap: 14px;
}
.three-dot-btn {
  background: transparent;
  border: 1px solid var(--line);
  border-radius: 8px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: var(--ink);
  cursor: pointer;
  transition: all 0.2s;
}
.three-dot-btn:hover {
  background: var(--priL);
  color: var(--pri);
  border-color: var(--pri);
}
.brand-title {
  font-weight: 800;
  font-size: 1.25rem;
  letter-spacing: -0.02em;
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}
.brand-title span.badge {
  font-size: 0.72rem;
  padding: 3px 8px;
  border-radius: 99px;
  background: var(--okL);
  color: var(--ok);
  font-weight: 700;
  border: 1px solid var(--okBorder);
}
.topbar-right {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.btn {
  background: var(--card);
  color: var(--ink);
  border: 1px solid var(--line);
  padding: 7px 14px;
  border-radius: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.15s;
  user-select: none;
}
.btn:hover {
  background: var(--priL);
  color: var(--pri);
  border-color: var(--pri);
}
.btn.active, .btn-primary {
  background: var(--pri);
  color: #ffffff;
  border-color: var(--pri);
}
.btn.active:hover, .btn-primary:hover {
  background: var(--priHover);
}
.btn-sm {
  padding: 4px 10px;
  font-size: 0.8rem;
}
.user-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 10px;
  border-radius: 99px;
  border: 1px solid var(--line);
  background: var(--card-subtle);
  cursor: pointer;
  font-weight: 600;
  font-size: 0.88rem;
}
.user-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--pri);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  object-fit: cover;
  overflow: hidden;
}

/* SIDEBAR DRAWER */
#sidebar-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(2px);
  z-index: 150;
  display: none;
}
#sidebar-backdrop.open { display: block; }
#sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 360px;
  max-width: 85vw;
  background: var(--card);
  border-right: 1px solid var(--line);
  z-index: 200;
  transform: translateX(-100%);
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  box-shadow: 4px 0 24px rgba(0,0,0,0.15);
}
#sidebar.open { transform: translateX(0); }
.sidebar-header {
  padding: 16px;
  border-bottom: 1px solid var(--line);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.sidebar-search {
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
}
.search-input {
  width: 100%;
  padding: 8px 12px;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: var(--bg);
  color: var(--ink);
  font-size: 0.9rem;
}
.sidebar-nav {
  padding: 10px 16px;
  border-bottom: 1px solid var(--line);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}
.sidebar-topic-list {
  flex: 1;
  overflow-y: auto;
  padding: 8px 12px;
}
.topic-tree-group {
  margin-bottom: 12px;
}
.topic-tree-group h4 {
  margin: 8px 6px 4px 6px;
  font-size: 0.78rem;
  text-transform: uppercase;
  color: var(--mut);
  letter-spacing: 0.05em;
}
.topic-nav-item {
  padding: 8px 10px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.88rem;
  color: var(--ink);
  text-decoration: none;
  cursor: pointer;
  transition: background 0.15s;
}
.topic-nav-item:hover, .topic-nav-item.active {
  background: var(--priL);
  color: var(--pri);
  font-weight: 600;
}

/* MAIN EXPANSIVE LAYOUT */
main.container {
  max-width: var(--maxw, 100%);
  width: 100%;
  margin: 16px auto;
  padding: 0 24px 80px 24px;
  box-sizing: border-box;
}

/* SECTION TABS (Category Switcher) */
.category-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
  overflow-x: auto;
  padding-bottom: 4px;
}
.cat-tab-btn {
  padding: 10px 18px;
  border-radius: 10px;
  border: 1px solid var(--line);
  background: var(--card);
  color: var(--mut);
  font-weight: 700;
  font-size: 0.95rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
  transition: all 0.2s;
}
.cat-tab-btn:hover {
  color: var(--ink);
  border-color: var(--pri);
}
.cat-tab-btn.active {
  background: var(--pri);
  color: white;
  border-color: var(--pri);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
}

/* TOPIC CATALOG GRID */
.topic-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
  gap: 16px;
  margin-top: 16px;
}
.topic-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 12px;
  box-shadow: var(--shadow);
  transition: transform 0.15s, border-color 0.15s;
}
.topic-card:hover {
  transform: translateY(-2px);
  border-color: var(--pri);
}
.topic-card-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 8px;
}
.topic-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--ink);
  margin: 0;
}
.topic-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  font-size: 0.8rem;
  color: var(--mut);
}
.diff-pill {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 4px;
}
.diff-pill.hard { background: var(--badL); color: var(--bad); }
.diff-pill.med { background: var(--warnL); color: var(--warn); }
.diff-pill.easy { background: var(--okL); color: var(--ok); }
.topic-actions {
  display: flex;
  gap: 8px;
  margin-top: 4px;
}

/* QUESTION CARD (PRACTICE & TEST) */
.q-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: var(--card-pad);
  box-shadow: var(--shadow);
  margin-bottom: 20px;
}
.q-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--line);
}
.q-badges {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.q-statement, .q-statement-block {
  font-size: 1.15rem;
  font-weight: 500;
  line-height: 1.6;
  margin-bottom: 20px;
}
.q-directive {
  font-weight: 700;
  color: var(--pri);
  margin-bottom: 8px;
  font-size: 1.05rem;
  letter-spacing: 0.2px;
}
.q-actual-question {
  font-size: 1.15rem;
  line-height: 1.65;
  white-space: pre-line;
}
.q-code-block {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.92rem;
  overflow-x: auto;
  margin: 12px 0 20px 0;
  line-height: 1.45;
}

/* OPTIONS LIST */
.options-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}
.option-item {
  background: var(--card);
  border: 2px solid var(--line);
  border-radius: 10px;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  transition: all 0.15s ease-out;
  position: relative;
  user-select: none;
}
.option-item:hover {
  background: var(--card-subtle);
  border-color: var(--pri);
}
.option-item.focused {
  outline: 2px solid var(--pri);
  background: var(--priL);
}
.option-badge {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: var(--bg);
  border: 1px solid var(--line);
  color: var(--mut);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.9rem;
  flex-shrink: 0;
  transition: all 0.15s;
}
.option-text {
  flex: 1;
  font-size: 1rem;
}

/* INSTANT FEEDBACK STATES (PRACTICE MODE) */
.option-item.is-correct {
  background: var(--okL) !important;
  border-color: var(--ok) !important;
  color: var(--ink) !important;
}
.option-item.is-correct .option-badge {
  background: var(--ok);
  color: white;
  border-color: var(--ok);
}
.option-item.is-wrong {
  background: var(--badL) !important;
  border-color: var(--bad) !important;
  color: var(--ink) !important;
}
.option-item.is-wrong .option-badge {
  background: var(--bad);
  color: white;
  border-color: var(--bad);
}

/* TEST MODE SELECTION */
.option-item.test-selected {
  background: var(--priL);
  border-color: var(--pri);
}
.option-item.test-selected .option-badge {
  background: var(--pri);
  color: white;
}

/* FEEDBACK & EXPLANATION BOXES */
.feedback-box {
  border-radius: 10px;
  padding: 16px;
  margin-top: 16px;
  animation: fadeIn 0.2s ease-out;
}
.feedback-box.correct {
  background: var(--okL);
  border: 1px solid var(--okBorder);
  color: var(--ink);
}
.feedback-box.wrong {
  background: var(--badL);
  border: 1px solid var(--badBorder);
  color: var(--ink);
}
.feedback-title {
  font-weight: 800;
  font-size: 1.05rem;
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}
.explanation-card {
  background: var(--card-subtle);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 16px;
  margin-top: 14px;
}
.explanation-card h4 {
  margin: 0 0 8px 0;
  font-size: 0.95rem;
  color: var(--pri);
}
.step-solution {
  white-space: pre-line;
  font-size: 0.92rem;
  line-height: 1.6;
  margin-top: 8px;
}

/* QUESTION CONTROLS TOOLBAR */
.q-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid var(--line);
}
.q-nav-buttons {
  display: flex;
  align-items: center;
  gap: 8px;
}

/* TEST PALETTE */
.test-layout {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 20px;
}
@media (max-width: 860px) {
  .test-layout { grid-template-columns: 1fr; }
}
.test-palette-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 16px;
  box-shadow: var(--shadow);
  height: fit-content;
}
.palette-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 6px;
  margin-top: 12px;
  max-height: 380px;
  overflow-y: auto;
  padding: 4px;
}
.palette-btn {
  aspect-ratio: 1;
  border-radius: 6px;
  border: 1px solid var(--line);
  background: var(--bg);
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s;
}
.palette-btn.current { outline: 2px solid var(--pri); }
.palette-btn.answered { background: var(--ok); color: white; border-color: var(--ok); }
.palette-btn.marked { background: var(--purple); color: white; border-color: var(--purple); }

/* FORMULA BOOK */
.formula-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 16px;
}
.formula-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 18px;
  box-shadow: var(--shadow);
}
.formula-latex {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px;
  margin: 12px 0;
  text-align: center;
  overflow-x: auto;
}

/* ------------------------------------------------------------- */
/* WELCOME DASHBOARD STYLING */
/* ------------------------------------------------------------- */
.welcome-hero {
  background: linear-gradient(135deg, var(--priL) 0%, var(--card) 100%);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 32px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 24px;
  box-shadow: var(--shadow);
}
.welcome-avatar-lg {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  background: var(--pri);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.4rem;
  font-weight: 800;
  flex-shrink: 0;
  border: 4px solid var(--card);
  box-shadow: 0 4px 16px rgba(0,0,0,0.12);
  object-fit: cover;
}
.welcome-content h1 {
  margin: 0 0 6px 0;
  font-size: 1.8rem;
  font-weight: 800;
}
.welcome-quote {
  font-size: 1rem;
  color: var(--mut);
  line-height: 1.5;
  margin-bottom: 16px;
}
.level-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}
.level-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 20px;
  box-shadow: var(--shadow);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.level-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
}
.level-card-title {
  font-size: 1.15rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
}
.level-stat-row {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  font-size: 0.9rem;
  border-bottom: 1px solid var(--line);
}
.level-stat-row:last-child { border-bottom: none; }
.progress-bar-bg {
  width: 100%;
  height: 8px;
  background: var(--bg);
  border-radius: 99px;
  overflow: hidden;
  margin: 8px 0;
}
.progress-bar-fill {
  height: 100%;
  background: var(--pri);
  transition: width 0.3s;
}

/* ------------------------------------------------------------- */
/* CODING PRACTICE & COMPILER IDE STYLING */
/* ------------------------------------------------------------- */
.coding-ide-layout {
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 18px;
  height: calc(100vh - 120px);
  min-height: 650px;
}
@media (max-width: 960px) {
  .coding-ide-layout {
    grid-template-columns: 1fr;
    height: auto;
  }
}
.coding-desc-panel {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 22px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
  box-shadow: var(--shadow);
}
.ide-constraints-box {
  background: var(--bg);
  border: 1.5px solid var(--line);
  border-left: 4px solid var(--pri);
  border-radius: 8px;
  padding: 14px 18px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.95rem;
  line-height: 1.7;
  color: var(--ink);
  white-space: pre-wrap;
  word-break: break-word;
  overflow: visible;
  box-shadow: inset 0 1px 3px rgba(0,0,0,0.05);
}
.ide-sample-box {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px 14px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.92rem;
  line-height: 1.5;
  white-space: pre-wrap;
  min-height: 48px;
  overflow: visible;
  box-shadow: inset 0 1px 2px rgba(0,0,0,0.04);
}
.ide-hints-card {
  background: var(--card-subtle);
  border: 1px solid var(--line);
  border-radius: 8px;
  margin-top: 10px;
  overflow: hidden;
}
.ide-hints-toggle {
  width: 100%;
  padding: 12px 16px;
  background: transparent;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-weight: 700;
  font-size: 0.95rem;
  color: var(--pri);
  transition: background 0.15s;
}
.ide-hints-toggle:hover {
  background: rgba(59, 130, 246, 0.08);
}
.ide-hints-body {
  padding: 14px 18px;
  border-top: 1px solid var(--line);
  display: none;
  background: var(--card);
}
.ide-hints-body.open {
  display: block;
}
.ide-hint-item {
  padding: 8px 12px;
  margin-bottom: 8px;
  background: var(--bg);
  border-left: 3px solid var(--pri);
  border-radius: 4px;
  font-size: 0.9rem;
  line-height: 1.5;
}
.ide-hint-item:last-child {
  margin-bottom: 0;
}

.coding-editor-panel {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  box-shadow: var(--shadow);
}
.editor-topbar {
  padding: 10px 14px;
  border-bottom: 1px solid var(--line);
  background: var(--card-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}
.editor-container-wrapper {
  flex: 1;
  display: flex;
  position: relative;
  background: #1e1e1e;
  color: #d4d4d4;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.94rem;
  overflow: hidden;
  min-height: 240px;
}
.editor-gutter {
  width: 46px;
  background: #252526;
  color: #858585;
  text-align: right;
  padding: 14px 8px;
  user-select: none;
  font-size: 0.86rem;
  line-height: 1.6;
  border-right: 1px solid #333333;
}
.code-editor-surface {
  position: relative;
  flex: 1;
  height: 100%;
  overflow: hidden;
}
.highlight-layer {
  position: absolute;
  inset: 0;
  margin: 0;
  padding: 14px 16px;
  border: none;
  background: transparent;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.94rem;
  line-height: 1.6;
  white-space: pre;
  overflow: hidden;
  tab-size: 4;
  pointer-events: none;
  box-sizing: border-box;
}
.highlight-layer code {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  tab-size: 4;
}
.code-textarea {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  background: transparent;
  color: transparent;
  caret-color: #38bdf8;
  border: none;
  outline: none;
  resize: none;
  padding: 14px 16px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.94rem;
  line-height: 1.6;
  white-space: pre;
  overflow: auto;
  tab-size: 4;
  box-sizing: border-box;
  z-index: 2;
}
/* SYNTAX HIGHLIGHTING TOKEN STYLES */
.tok-kw { color: #c586c0 !important; font-weight: 700; } /* def, class, if, for, return, int, using */
.tok-dir { color: #e5c07b !important; font-weight: 700; } /* #include <iostream>, #define */
.tok-bi { color: #4ec9b0 !important; } /* print, cout, cin, endl, range, len */
.tok-str { color: #ce9178 !important; } /* "string", 'char' */
.tok-num { color: #b5cea8 !important; } /* 123, 4.56 */
.tok-cmt { color: #6a9955 !important; font-style: italic; } /* // comment, # comment */
.tok-ident { color: #d4d4d4 !important; }

/* CONSOLE PANEL & EXPANDED MODE */
.editor-console-panel {
  height: 320px;
  min-height: 220px;
  max-height: 85%;
  border-top: 2px solid var(--line);
  background: var(--card);
  display: flex;
  flex-direction: column;
  transition: height 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 -4px 14px rgba(0,0,0,0.1);
}
.editor-console-panel.expanded {
  height: 82% !important;
}
.console-topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--card-subtle);
  border-bottom: 1px solid var(--line);
  padding-right: 12px;
}
.console-tabs {
  display: flex;
  background: transparent;
}
.console-tab-btn {
  padding: 8px 16px;
  font-size: 0.85rem;
  font-weight: 600;
  border: none;
  background: transparent;
  cursor: pointer;
  color: var(--mut);
  border-bottom: 2px solid transparent;
  transition: all 0.15s;
}
.console-tab-btn.active {
  color: var(--pri);
  border-bottom-color: var(--pri);
  background: var(--card);
}
.console-expand-btn {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 4px 10px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  color: var(--pri);
  display: flex;
  align-items: center;
  gap: 5px;
  transition: all 0.15s;
}
.console-expand-btn:hover {
  background: var(--pri);
  color: white;
}
.console-output-content {
  padding: 10px 12px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.88rem;
  line-height: 1.5;
  background: var(--bg);
  border-radius: 6px;
  border: 1px solid var(--line);
  white-space: pre-wrap;
}
.verdict-banner {
  padding: 12px 16px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 0.95rem;
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.verdict-banner.accepted { background: var(--okL); color: var(--ok); border: 1.5px solid var(--okBorder); }
.verdict-banner.wrong { background: var(--badL); color: var(--bad); border: 1.5px solid var(--badBorder); }
.verdict-banner.error { background: var(--warnL); color: var(--warn); border: 1.5px solid var(--warn); }

/* CUSTOM INPUT & CUSTOM OUTPUT */
.custom-io-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  height: 100%;
}
@media (max-width: 768px) {
  .custom-io-container {
    grid-template-columns: 1fr;
  }
}
.custom-io-col {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.custom-io-col label {
  font-weight: 700;
  font-size: 0.85rem;
  color: var(--ink);
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.custom-io-textarea {
  flex: 1;
  min-height: 130px;
  background: var(--bg);
  border: 1.5px solid var(--line);
  border-radius: 8px;
  padding: 10px 12px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.9rem;
  line-height: 1.5;
  color: var(--ink);
  resize: vertical;
}
.custom-io-textarea:focus {
  border-color: var(--pri);
  outline: none;
}
.custom-stdout-box {
  flex: 1;
  min-height: 130px;
  margin: 0;
  background: #111827;
  color: #10b981;
  border: 1.5px solid var(--line);
  border-radius: 8px;
  padding: 10px 12px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.9rem;
  line-height: 1.5;
  white-space: pre-wrap;
  overflow-y: auto;
}
/* ------------------------------------------------------------- */
/* ADMIN PANEL TABBED SETTINGS */
/* ------------------------------------------------------------- */
.admin-tabs-nav {
  display: flex;
  gap: 6px;
  overflow-x: auto;
  border-bottom: 2px solid var(--line);
  margin-bottom: 20px;
  padding-bottom: 2px;
}
.admin-tab-btn {
  padding: 8px 16px;
  border: none;
  background: transparent;
  font-size: 0.92rem;
  font-weight: 700;
  color: var(--mut);
  cursor: pointer;
  border-bottom: 3px solid transparent;
  transition: all 0.15s;
  white-space: nowrap;
}
.admin-tab-btn:hover { color: var(--ink); }
.admin-tab-btn.active {
  color: var(--pri);
  border-bottom-color: var(--pri);
}
.admin-section { display: none; }
.admin-section.active { display: block; }

.settings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 18px;
}
.settings-group {
  background: var(--card-subtle);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 16px;
}
.settings-group h4 {
  margin: 0 0 12px 0;
  font-size: 0.95rem;
  color: var(--pri);
}

/* MODALS */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(3px);
  z-index: 500;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 16px;
}
.modal-backdrop.open { display: flex; }
.modal-dialog {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  max-width: 650px;
  width: 100%;
  max-height: 92vh;
  overflow-y: auto;
  padding: 24px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.25);
  animation: modalPop 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.modal-dialog.modal-lg {
  max-width: 900px;
}

@keyframes fadeIn { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }
@keyframes modalPop { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }

/* RESPONSIVE HELPERS */
@media (max-width: 640px) {
  header.topbar { padding: 8px 12px; }
  .brand-title span.badge { display: none; }
  main.container { padding: 0 10px 60px 10px; }
  .q-statement { font-size: 1.05rem; }
  .welcome-hero { flex-direction: column; text-align: center; }
}

/* SHUFFLE & QUESTION CONTROLS */
.q-shuffle-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
  background: var(--card-subtle);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 8px 12px;
  margin-bottom: 12px;
  font-size: 0.85rem;
}
.q-shuffle-btn-group {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}
.shuffle-active-badge {
  background: rgba(59, 130, 246, 0.15);
  color: var(--pri);
  border: 1px solid var(--pri);
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 600;
}

/* WHITE-BACKGROUND EXPLANATION THEME (MATCHING USER REFERENCE IMAGE) */
.white-bg-explanation {
  background: #ffffff !important;
  color: #1e293b !important;
  border: 1px solid #cbd5e1 !important;
  border-left: 5px solid #16a34a !important;
  border-radius: 8px !important;
  padding: 16px 20px !important;
  margin-top: 14px !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
}
.white-bg-explanation .answer-line {
  color: #16a34a !important;
  font-size: 1.15rem !important;
  font-weight: 700 !important;
  margin-bottom: 8px !important;
  display: flex;
  align-items: center;
  gap: 4px;
}
.white-bg-explanation .answer-circle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: 1.5px solid #16a34a;
  color: #16a34a;
  font-weight: 800;
  font-size: 0.95rem;
  margin: 0 4px;
}
.white-bg-explanation .expl-heading {
  color: #16a34a !important;
  font-size: 1.05rem !important;
  font-weight: 700 !important;
  margin: 10px 0 6px 0 !important;
}
.white-bg-explanation .expl-body {
  color: #334155 !important;
  font-size: 0.96rem !important;
  line-height: 1.65 !important;
  margin-bottom: 12px !important;
}
.white-bg-explanation .proc-heading {
  color: #0284c7 !important;
  font-size: 0.95rem !important;
  font-weight: 700 !important;
  margin: 14px 0 6px 0 !important;
}
.white-bg-explanation .proc-box {
  background: #f8fafc !important;
  color: #0f172a !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important;
  padding: 12px 14px !important;
  font-size: 0.92rem !important;
  line-height: 1.7 !important;
  white-space: pre-line !important;
}

/* CODING IDE TEST CASE TABLE & VERDICTS */
.ide-testcase-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.82rem;
  margin-top: 8px;
  background: var(--card-subtle);
  border-radius: 6px;
  overflow: hidden;
  border: 1px solid var(--line);
}
.ide-testcase-table th {
  background: var(--card);
  padding: 8px 10px;
  text-align: left;
  border-bottom: 1px solid var(--line);
  font-weight: 600;
  color: var(--mut);
}
.ide-testcase-table td {
  padding: 8px 10px;
  border-bottom: 1px solid var(--line);
  font-family: var(--font-mono, monospace);
  white-space: pre-wrap;
  word-break: break-all;
}
.ide-testcase-table tr.case-passed td {
  background: rgba(34, 197, 94, 0.05);
}
.ide-testcase-table tr.case-failed td {
  background: rgba(239, 68, 68, 0.05);
}

/* CODING PRACTICE SEARCH & FILTER BAR */
.coding-search-bar {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  align-items: center;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 12px 16px;
  margin-bottom: 18px;
}
.coding-search-input-wrap {
  flex: 1;
  min-width: 260px;
}

/* ------------------------------------------------------------- */
/* SYLLABUS NAVIGATOR 4-DROPDOWN SELECTORS (THREE-DOT MENU) */
/* ------------------------------------------------------------- */
.sidebar-dropdowns-container {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin: 14px 0;
  padding: 0 4px;
}
.sidebar-dropdown-card {
  background: var(--card-subtle);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px 12px;
}
.sidebar-dropdown-title {
  font-size: 0.82rem;
  font-weight: 700;
  color: var(--pri);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.sidebar-dropdown-select {
  width: 100%;
  padding: 8px 10px;
  border-radius: 6px;
  border: 1.5px solid var(--line);
  background: var(--card);
  color: var(--ink);
  font-size: 0.85rem;
  font-weight: 600;
  outline: none;
  cursor: pointer;
  transition: border-color 0.15s;
}
.sidebar-dropdown-select:focus {
  border-color: var(--pri);
}

/* ------------------------------------------------------------- */
/* PREPARATION CALENDAR & STUDY OF THE DAY STYLES */
/* ------------------------------------------------------------- */
.calendar-wrapper {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: var(--shadow);
  margin-bottom: 24px;
}
.calendar-header-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 14px;
  margin-bottom: 20px;
}
.calendar-month-title {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--ink);
  display: flex;
  align-items: center;
  gap: 10px;
}
.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 8px;
}
@media (max-width: 768px) {
  .calendar-grid {
    grid-template-columns: repeat(7, 1fr);
    gap: 4px;
  }
  .calendar-day-cell {
    min-height: 80px !important;
    padding: 4px !important;
  }
}
.calendar-weekday-header {
  text-align: center;
  font-weight: 700;
  font-size: 0.85rem;
  color: var(--mut);
  padding: 8px 0;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.calendar-day-cell {
  min-height: 110px;
  background: var(--card-subtle);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  transition: all 0.15s ease-in-out;
  position: relative;
}
.calendar-day-cell:hover {
  border-color: var(--pri);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
.calendar-day-cell.other-month {
  opacity: 0.35;
  cursor: default;
}
.calendar-day-cell.is-today {
  border: 2px solid var(--pri);
  background: var(--priL);
}
.calendar-day-num {
  font-weight: 800;
  font-size: 0.95rem;
  color: var(--ink);
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}
.today-badge-pill {
  font-size: 0.65rem;
  background: var(--pri);
  color: white;
  padding: 1px 5px;
  border-radius: 4px;
  font-weight: 700;
}
.calendar-task-badge {
  font-size: 0.72rem;
  padding: 2px 6px;
  border-radius: 4px;
  margin-top: 3px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 4px;
}
.calendar-task-badge.coding {
  background: rgba(59, 130, 246, 0.15);
  color: var(--pri);
  border-left: 3px solid var(--pri);
}
.calendar-task-badge.quant {
  background: rgba(22, 163, 74, 0.15);
  color: var(--ok);
  border-left: 3px solid var(--ok);
}
.calendar-task-badge.verbal {
  background: rgba(168, 85, 247, 0.15);
  color: var(--purple);
  border-left: 3px solid var(--purple);
}
.calendar-task-badge.done {
  text-decoration: line-through;
  opacity: 0.7;
}

/* TODAY'S GOALS WIDGET ON WELCOME DASHBOARD */
.today-goals-card {
  background: var(--card);
  border: 1.5px solid var(--line);
  border-radius: var(--radius);
  padding: 22px;
  box-shadow: var(--shadow);
  margin-bottom: 24px;
}
.today-goals-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
  margin-top: 14px;
}
.today-goal-item {
  background: var(--card-subtle);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

"""