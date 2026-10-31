# builder/verify_acceptance.py
import os
import sys
import json
import re

print("Running Automated Acceptance Tests on Placement Learning Platform...")

workspace_dir = "f:/placement/1round ready2"
data_dir = os.path.join(workspace_dir, "data")
html_path = os.path.join(workspace_dir, "index.html")

assert os.path.exists(html_path), "index.html does not exist!"
for fname in ["catalog_and_meta.js", "coding_part1.js", "coding_part2.js", "quant_questions.js", "verbal_logical_questions.js"]:
    fpath = os.path.join(data_dir, fname)
    assert os.path.exists(fpath), f"Missing data file: {fname}"

# Verify HTML file
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Check: No Submit button in practice mode
assert "practice-submit" not in html_content.lower(), "Found practice submit button!"
# Check KaTeX inclusion
assert "katex.min.css" in html_content, "KaTeX CSS missing"
assert "katex.min.js" in html_content, "KaTeX JS missing"

# Check Three-dot button
assert 'id="three-dot-toggle"' in html_content, "Three-dot toggle missing"

# Load JS data objects by regex or evaluation
print("Loading and verifying data files...")

def load_js_object(filepath, var_name):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    pattern = rf"window\.{var_name}\s*=\s*(.+?);\s*(?:\n|window\.|$)"
    match = re.search(pattern, content, re.DOTALL)
    assert match, f"Could not extract window.{var_name} from {filepath}"
    return json.loads(match.group(1))

catalog = load_js_object(os.path.join(data_dir, "catalog_and_meta.js"), "PREP_CATALOG")
study_guides = load_js_object(os.path.join(data_dir, "catalog_and_meta.js"), "PREP_STUDY_GUIDES")
formulas = load_js_object(os.path.join(data_dir, "catalog_and_meta.js"), "PREP_FORMULAS")

coding_p1 = load_js_object(os.path.join(data_dir, "coding_part1.js"), "CODING_P1")
coding_p2 = load_js_object(os.path.join(data_dir, "coding_part2.js"), "CODING_P2")
quant = load_js_object(os.path.join(data_dir, "quant_questions.js"), "QUANT_DATA")
verbal_logical = load_js_object(os.path.join(data_dir, "verbal_logical_questions.js"), "VERBAL_LOGICAL_DATA")

all_questions = {}
all_questions.update(coding_p1)
all_questions.update(coding_p2)
all_questions.update(quant)
all_questions.update(verbal_logical)

print(f"Total topics loaded: {len(all_questions)}")
assert len(all_questions) == 327, f"Expected 327 topics, found {len(all_questions)}"
assert len(catalog) == 327, f"Catalog size {len(catalog)} != 327"
assert len(study_guides) == 327, f"Study guides count {len(study_guides)} != 327"
assert len(formulas) >= 10, f"Expected at least 10 formula book entries, found {len(formulas)}"

total_q = 0
total_hard = 0
total_med = 0
total_easy = 0

for tid, qs in all_questions.items():
    cat_entry = catalog[tid]
    req = 200 if tid in ("coding_py_data_handling", "coding_py_stats_math") else 100
    assert len(qs) == req, f"Topic {tid}: Expected {req} questions, got {len(qs)}"

    c_hard = sum(1 for q in qs if q["difficulty"] == "Hard")
    c_easy = sum(1 for q in qs if q["difficulty"] == "Easy")
    c_med = sum(1 for q in qs if q["difficulty"] == "Medium")

    req_hard = 150 if req == 200 else 75
    req_easy = 30 if req == 200 else 15
    req_med = 20 if req == 200 else 10

    assert c_hard == req_hard, f"Topic {tid}: Hard count mismatch {c_hard} != {req_hard}"
    assert c_easy == req_easy, f"Topic {tid}: Easy count mismatch {c_easy} != {req_easy}"
    assert c_med == req_med, f"Topic {tid}: Medium count mismatch {c_med} != {req_med}"

    total_q += len(qs)
    total_hard += c_hard
    total_easy += c_easy
    total_med += c_med

    # Validate individual questions
    for q in qs:
        assert len(q["o"]) == 4, f"{q['id']}: options != 4"
        assert len(set(q["o"])) == 4, f"{q['id']}: options not unique"
        assert q["a"] in (0, 1, 2, 3), f"{q['id']}: invalid answer {q['a']}"
        assert len(q["h"].strip()) > 0, f"{q['id']}: empty hint"
        assert len(q["e"].strip()) > 0, f"{q['id']}: empty explanation"
        assert len(q["step"].strip()) > 0, f"{q['id']}: empty step-by-step solution"
        assert len(q["tech"].strip()) > 0, f"{q['id']}: empty technique"

print(f"\nALL 327 TOPICS PASSED INTEGRITY AUDIT!")
print(f"Total verified questions: {total_q}")
print(f"Difficulty counts: Hard = {total_hard} ({total_hard/total_q*100:.1f}%), Easy = {total_easy} ({total_easy/total_q*100:.1f}%), Medium = {total_med} ({total_med/total_q*100:.1f}%)")
print("\nALL ACCEPTANCE CRITERIA VERIFIED SUCCESSFULLY (100% PASS).")
