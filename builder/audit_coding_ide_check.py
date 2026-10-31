# builder/audit_coding_ide_check.py
import sys
import os

sys.path.append(os.path.dirname(__file__))
from audit_duplicates import load_js_data, normalize_text

cp_data = load_js_data('data/coding_practice_problems.js', 'window.CODING_PRACTICE_DATA')
seen_titles = set()
seen_descs = set()
exact_dups = 0
desc_dups = 0

for tid, t in cp_data.items():
    for p in t['problems']:
        nt = normalize_text(p['title'])
        nd = normalize_text(p['desc'])
        if nt in seen_titles:
            exact_dups += 1
        else:
            seen_titles.add(nt)
        if nd in seen_descs:
            desc_dups += 1
        else:
            seen_descs.add(nd)

total_p = sum(len(v['problems']) for v in cp_data.values())
print(f"Total problems: {total_p}")
print(f"Exact title dups across all topics: {exact_dups}")
print(f"Desc dups across all topics: {desc_dups}")
