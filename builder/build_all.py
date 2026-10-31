# builder/build_all.py
import os
import sys
import json
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding='utf-8')

from catalog import get_all_topics
from gen_coding import generate_topic_coding
from gen_quant import generate_topic_quant
from gen_verbal_logical import generate_topic_verbal_logical
from formula_data import FORMULA_ENTRIES
from study_notes_data import get_study_guide_for_topic

print("=================================================================")
print("STARTING FULL QUESTION BANK GENERATION (327 TOPICS / 32,900 Qs)")
print("=================================================================")

t0 = time.time()
all_topics = get_all_topics()
assert len(all_topics) == 327, f"Expected 327 topics, got {len(all_topics)}"

topic_catalog_map = {}
study_guides_map = {}

coding_questions = {}
quant_questions = {}
verbal_logical_questions = {}

total_questions_count = 0
total_hard = 0
total_med = 0
total_easy = 0

for idx, t in enumerate(all_topics):
    tid = t["id"]
    tname = t["title"]
    grp = t["group"]
    cat = t["category"]
    req = t["required"]
    diff_req = t["diff"]
    
    # 1. Generate questions
    if cat == "Coding Questions":
        qs = generate_topic_coding(tid, tname, grp, req)
        coding_questions[tid] = qs
    elif cat == "Quantitative Aptitude":
        qs = generate_topic_quant(tid, tname, grp)
        quant_questions[tid] = qs
    else:
        qs = generate_topic_verbal_logical(tid, tname, grp)
        verbal_logical_questions[tid] = qs

    # 2. Strict validation
    assert len(qs) == req, f"Topic {tid}: length {len(qs)} != {req}"
    c_easy = sum(1 for q in qs if q["difficulty"] == "Easy")
    c_med = sum(1 for q in qs if q["difficulty"] == "Medium")
    c_hard = sum(1 for q in qs if q["difficulty"] == "Hard")
    
    assert c_easy == diff_req["Easy"], f"Topic {tid}: Easy count {c_easy} != {diff_req['Easy']}"
    assert c_med == diff_req["Medium"], f"Topic {tid}: Medium count {c_med} != {diff_req['Medium']}"
    assert c_hard == diff_req["Hard"], f"Topic {tid}: Hard count {c_hard} != {diff_req['Hard']}"
    
    total_easy += c_easy
    total_med += c_med
    total_hard += c_hard
    total_questions_count += len(qs)

    for q in qs:
        assert len(q["o"]) == 4, f"Question {q['id']} options != 4"
        assert len(set(q["o"])) == 4, f"Question {q['id']} duplicate options"
        assert q["a"] in (0, 1, 2, 3), f"Question {q['id']} invalid answer {q['a']}"
        assert len(q["h"]) > 0, f"Question {q['id']} empty hint"
        assert len(q["e"]) > 0, f"Question {q['id']} empty explanation"
        assert len(q["step"]) > 0, f"Question {q['id']} empty step"
        assert len(q["tech"]) > 0, f"Question {q['id']} empty tech"

    # 3. Catalog and Study Guide
    topic_catalog_map[tid] = {
        "id": tid,
        "title": tname,
        "category": cat,
        "group": grp,
        "count": req,
        "diff": {"Hard": c_hard, "Easy": c_easy, "Medium": c_med},
        "published": True
    }
    study_guides_map[tid] = get_study_guide_for_topic(tid, tname, grp, cat)

    if (idx + 1) % 50 == 0 or (idx + 1) == len(all_topics):
        print(f"  Processed {idx + 1:3d} / 327 topics ({total_questions_count:5d} questions verified)...")

t1 = time.time()
print(f"\nSUCCESS: All {len(all_topics)} topics and {total_questions_count} questions generated & verified in {t1 - t0:.2f} seconds!")
print(f"Summary: Hard = {total_hard} (75%), Easy = {total_easy} (15%), Medium = {total_med} (10%)")

# Output directory: f:/placement/1round ready2/data
out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
os.makedirs(out_dir, exist_ok=True)

print("\nWriting partitioned JavaScript data files...")

# Write Catalog & Study Guides & Formulas
catalog_file = os.path.join(out_dir, "catalog_and_meta.js")
with open(catalog_file, "w", encoding="utf-8") as f:
    f.write("// PlacementPrep Master Catalog, Study Guides & Formula Book\n")
    f.write("window.PREP_CATALOG = " + json.dumps(topic_catalog_map, ensure_ascii=False) + ";\n")
    f.write("window.PREP_STUDY_GUIDES = " + json.dumps(study_guides_map, ensure_ascii=False) + ";\n")
    f.write("window.PREP_FORMULAS = " + json.dumps(FORMULA_ENTRIES, ensure_ascii=False) + ";\n")
print(f"  [OK] catalog_and_meta.js ({os.path.getsize(catalog_file) / (1024*1024):.2f} MB)")

# Split Coding into two parts
coding_keys = list(coding_questions.keys())
half_c = len(coding_keys) // 2
coding_p1 = {k: coding_questions[k] for k in coding_keys[:half_c]}
coding_p2 = {k: coding_questions[k] for k in coding_keys[half_c:]}

coding_p1_file = os.path.join(out_dir, "coding_part1.js")
with open(coding_p1_file, "w", encoding="utf-8") as f:
    f.write("// Coding Questions Part 1 (Topics 1 to " + str(half_c) + ")\n")
    f.write("window.CODING_P1 = " + json.dumps(coding_p1, ensure_ascii=False) + ";\n")
print(f"  [OK] coding_part1.js ({os.path.getsize(coding_p1_file) / (1024*1024):.2f} MB)")

coding_p2_file = os.path.join(out_dir, "coding_part2.js")
with open(coding_p2_file, "w", encoding="utf-8") as f:
    f.write("// Coding Questions Part 2 (Topics " + str(half_c + 1) + " to " + str(len(coding_keys)) + ")\n")
    f.write("window.CODING_P2 = " + json.dumps(coding_p2, ensure_ascii=False) + ";\n")
print(f"  [OK] coding_part2.js ({os.path.getsize(coding_p2_file) / (1024*1024):.2f} MB)")

# Write Quant questions
quant_file = os.path.join(out_dir, "quant_questions.js")
with open(quant_file, "w", encoding="utf-8") as f:
    f.write("// Quantitative Aptitude Questions (All 74 Topics)\n")
    f.write("window.QUANT_DATA = " + json.dumps(quant_questions, ensure_ascii=False) + ";\n")
print(f"  [OK] quant_questions.js ({os.path.getsize(quant_file) / (1024*1024):.2f} MB)")

# Write Verbal & Logical questions
verbal_file = os.path.join(out_dir, "verbal_logical_questions.js")
with open(verbal_file, "w", encoding="utf-8") as f:
    f.write("// Verbal Ability and Logical Reasoning Questions (All 87 Topics)\n")
    f.write("window.VERBAL_LOGICAL_DATA = " + json.dumps(verbal_logical_questions, ensure_ascii=False) + ";\n")
print(f"  [OK] verbal_logical_questions.js ({os.path.getsize(verbal_file) / (1024*1024):.2f} MB)")

print("\nAll data files generated and saved successfully!")
