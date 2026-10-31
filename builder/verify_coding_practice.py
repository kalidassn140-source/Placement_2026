# builder/verify_coding_practice.py
import re
import json

with open("f:/placement/1round ready2/data/coding_practice_problems.js", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(r"window\.CODING_PRACTICE_DATA\s*=\s*(.+?);\s*$", content, re.DOTALL)
assert match, "Could not extract window.CODING_PRACTICE_DATA"

cp_data = json.loads(match.group(1))

print(f"Total Coding Practice Topics: {len(cp_data)}")
total_probs = 0
total_lc = 0
total_placement = 0

for tid, topic in cp_data.items():
    probs = topic["problems"]
    total_probs += len(probs)
    for p in probs:
        assert len(p["test_cases"]) > 0, f"No test cases in {p['id']}"
        assert "starter_code" in p, f"Missing starter code in {p['id']}"
        assert all(lang in p["starter_code"] for lang in ["c", "cpp", "python", "java", "javascript", "sql"]), f"Missing language starter in {p['id']}"
        assert len(p["sample_input"]) > 0, f"Missing sample input in {p['id']}"
        assert len(p["expected_output"]) > 0, f"Missing expected output in {p['id']}"
        if "LeetCode" in p["source"]:
            total_lc += 1
        else:
            total_placement += 1

print(f"Total Coding Problems: {total_probs}")
print(f"LeetCode Classic: {total_lc} ({total_lc/total_probs*100:.1f}%)")
print(f"Placement Challenges: {total_placement} ({total_placement/total_probs*100:.1f}%)")
print("Coding Practice Integrity Test Passed!")
