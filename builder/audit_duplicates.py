# builder/audit_duplicates.py
import json
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

def load_js_data(filepath, var_name):
    print(f"Loading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    idx = text.find(var_name)
    if idx == -1:
        raise ValueError(f"Variable {var_name} not found in {filepath}")
    eq = text.find('=', idx)
    raw = text[eq+1:].strip()
    if raw.endswith(';'):
        raw = raw[:-1].strip()
    return json.loads(raw)

def normalize_text(text):
    if not text:
        return ""
    # Strip brackets like [Parts of Speech Basic #1]
    t = re.sub(r'^\s*\[[^\]]+\]\s*', '', text)
    # Lowercase, strip punctuation and extra spaces
    t = t.lower()
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def template_fingerprint(text):
    # Mask numbers, single-letter variables, quotes
    t = normalize_text(text)
    t = re.sub(r'\b\d+\b', '<NUM>', t)
    t = re.sub(r'\b[a-z]\b', '<VAR>', t)
    return t

def run_audit():
    # 1. Audit Coding Practice IDE Problems
    print("\n================ AUDITING CODING IDE BANK ================")
    cp_data = load_js_data('data/coding_practice_problems.js', 'window.CODING_PRACTICE_DATA')
    print(f"Loaded {len(cp_data)} Coding IDE topics.")

    cp_total_problems = 0
    cp_exact_dups = 0
    cp_semantic_dups = 0
    cp_dup_details = []

    for tid, topic in cp_data.items():
        seen_titles = {}
        seen_descs = {}
        topic_exact = 0
        topic_sem = 0
        problems = topic.get('problems', [])
        cp_total_problems += len(problems)

        for p in problems:
            norm_title = normalize_text(p['title'])
            norm_desc = normalize_text(p.get('desc', ''))[:100]

            if norm_title in seen_titles:
                topic_exact += 1
                cp_dup_details.append({
                    'topic': topic['title'],
                    'type': 'exact_title',
                    'p1': seen_titles[norm_title]['id'],
                    'p2': p['id'],
                    'title': p['title']
                })
            else:
                seen_titles[norm_title] = p

            if norm_desc and norm_desc in seen_descs and norm_title != normalize_text(seen_descs[norm_desc]['title']):
                topic_sem += 1
                cp_dup_details.append({
                    'topic': topic['title'],
                    'type': 'similar_desc',
                    'p1': seen_descs[norm_desc]['id'],
                    'p2': p['id'],
                    'title': p['title']
                })
            else:
                seen_descs[norm_desc] = p

        cp_exact_dups += topic_exact
        cp_semantic_dups += topic_sem
        if topic_exact > 0 or topic_sem > 0:
            print(f"Topic '{topic['title']}': {len(problems)} probs | Exact: {topic_exact} | Similar: {topic_sem}")

    print(f"CODING IDE TOTAL: {cp_total_problems} problems | Exact dups: {cp_exact_dups} | Semantic/Template dups: {cp_semantic_dups}")

    # 2. Audit MCQ Question Bank
    print("\n================ AUDITING MCQ QUESTION BANK ================")
    mcq_files = [
        ('data/coding_part1.js', 'window.CODING_P1'),
        ('data/coding_part2.js', 'window.CODING_P2'),
        ('data/quant_questions.js', 'window.QUANT_DATA'),
        ('data/verbal_logical_questions.js', 'window.VERBAL_LOGICAL_DATA')
    ]

    mcq_bank = {}
    for path, var_name in mcq_files:
        data = load_js_data(path, var_name)
        mcq_bank.update(data)

    print(f"Loaded {len(mcq_bank)} MCQ topics total.")

    mcq_total_qs = 0
    mcq_exact_dups = 0
    mcq_template_dups = 0
    topics_with_dups = {}

    for tid, qlist in mcq_bank.items():
        mcq_total_qs += len(qlist)
        seen_exact = {}
        seen_template = {}
        t_exact = 0
        t_template = 0

        for q in qlist:
            norm_q = normalize_text(q['q'])
            tmpl_q = template_fingerprint(q['q'])

            if norm_q in seen_exact:
                t_exact += 1
            else:
                seen_exact[norm_q] = q

            if tmpl_q in seen_template:
                t_template += 1
            else:
                seen_template[tmpl_q] = q

        if t_exact > 0 or t_template > 0:
            topics_with_dups[tid] = {
                'total': len(qlist),
                'exact_dups': t_exact,
                'unique_exact': len(seen_exact),
                'template_dups': t_template,
                'unique_template': len(seen_template)
            }
            mcq_exact_dups += t_exact
            mcq_template_dups += t_template

    print(f"MCQ TOTAL: {mcq_total_qs} questions across {len(mcq_bank)} topics.")
    print(f"MCQ Exact Duplicates: {mcq_exact_dups}")
    print(f"MCQ Template / Near Duplicates: {mcq_template_dups}")
    print(f"Topics with duplicates: {len(topics_with_dups)} of {len(mcq_bank)}")

    # Print sample topics with high duplicates
    sorted_topics = sorted(topics_with_dups.items(), key=lambda x: x[1]['exact_dups'], reverse=True)
    print("\nTop 15 topics by exact duplicate count:")
    for tid, stats in sorted_topics[:15]:
        print(f"  {tid}: total={stats['total']}, exact_dups={stats['exact_dups']}, unique_exact={stats['unique_exact']}, tmpl_dups={stats['template_dups']}")

if __name__ == '__main__':
    run_audit()
