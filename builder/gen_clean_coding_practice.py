# builder/gen_clean_coding_practice.py
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Import topic specs from gen_coding_practice
from gen_coding_practice import TOPIC_SPECS

print("Generating 100% Unique Coding Practice Problems (1,540 Problems across 29 Topics)...")

# Problem definition generator with rich, genuine problem statements
def create_coding_problem(pid, tid, tname, grp, title, diff, source, desc, inp_fmt, out_fmt, constr, sample_in, sample_out, approach, time_c, space_c, code_py, code_c, code_cpp, code_java, code_js, code_sql, test_cases):
    return {
        "id": pid,
        "topic_id": tid,
        "topic_name": tname,
        "group": grp,
        "title": title,
        "difficulty": diff,
        "source": source,
        "desc": desc,
        "input_format": inp_fmt,
        "output_format": out_fmt,
        "constraints": constr,
        "sample_input": sample_in,
        "expected_output": sample_out,
        "solution": {
            "approach": approach,
            "time_complexity": time_c,
            "space_complexity": space_c,
            "code_python": code_py
        },
        "starter_code": {
            "python": code_py.split('# Test')[0].strip(),
            "c": code_c,
            "cpp": code_cpp,
            "java": code_java,
            "javascript": code_js,
            "sql": code_sql
        },
        "test_cases": test_cases
    }

