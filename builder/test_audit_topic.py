# builder/test_audit_topic.py
import json
import os
import re
import sys
from collections import defaultdict

sys.path.append(os.path.dirname(__file__))
from audit_duplicates import load_js_data, normalize_text, template_fingerprint

vl = load_js_data('data/verbal_logical_questions.js', 'window.VERBAL_LOGICAL_DATA')
print("Loaded verbal logical topics:", len(vl))

def audit_single_topic(qlist):
    retained = []
    duplicates = []
    seen_exact = set()
    seen_template = set()

    for q in qlist:
        norm = normalize_text(q['q'])
        tmpl = template_fingerprint(q['q'])

        is_dup = False
        dup_reason = ""

        if norm in seen_exact:
            is_dup = True
            dup_reason = "exact_text"
        elif tmpl in seen_template:
            is_dup = True
            dup_reason = "template_clone"

        if is_dup:
            duplicates.append((q['id'], dup_reason, q['q']))
        else:
            seen_exact.add(norm)
            seen_template.add(tmpl)
            retained.append(q)

    return retained, duplicates

t_sample = 'verbal_parts_speech'
retained, dups = audit_single_topic(vl[t_sample])
print(f"Topic {t_sample}: original={len(vl[t_sample])}, retained unique={len(retained)}, duplicates={len(dups)}")
print("Sample duplicates found:")
for d in dups[:5]:
    print(f"  [{d[1]}] {d[0]}: {d[2][:70]}...")
