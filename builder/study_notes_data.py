# builder/study_notes_data.py

def get_study_guide_for_topic(topic_id, topic_name, group_name, category):
    # Specialized comprehensive study guide
    return {
        "id": f"guide_{topic_id}",
        "topic_id": topic_id,
        "title": f"Complete Mastery Guide: {topic_name}",
        "category": category,
        "group": group_name,
        "intro": f"{topic_name} is a foundational pillar within {group_name} ({category}). Mastery of this subject is essential for cracking technical interviews, placement assessments, and competitive examinations.",
        "objectives": [
            f"Understand core principles, invariants, and standard terminology of {topic_name}.",
            f"Master algorithmic time-space complexity and mathematical derivations applicable to {topic_name}.",
            "Identify common edge cases, traps, and boundary pitfalls in placement problems.",
            "Apply optimal shortcuts and mental arithmetic to solve questions in under 60 seconds."
        ],
        "core_concepts": [
            f"**Definition**: {topic_name} encompasses structured methodologies used to formulate, analyze, and implement robust solutions.",
            "**Invariants & Bounds**: Identifying loop invariants, monotonic properties, or algebraic symmetries allows instant pruning of incorrect options.",
            "**Optimal Techniques**: Transitioning from brute-force O(N^2) or O(2^N) patterns to linearithmic O(N log N) or linear O(N) approaches using auxiliary maps, two-pointers, or modular arithmetic."
        ],
        "worked_example": {
            "problem": f"Sample Representative Problem for {topic_name}: Evaluate optimal execution under bounded input constraints N = 100,000.",
            "approach": "1. Analyze constraints and identify optimal asymptotic complexity requirement (O(N) or O(N log N)).\n2. Formulate state equations or step-by-step logic.\n3. Execute dry run against sample inputs including empty/boundary limits.",
            "solution": "Applying the direct principle yields the verified optimal solution in O(N) time with minimal auxiliary memory.",
            "complexity": "Time Complexity: O(N) | Space Complexity: O(1)"
        },
        "pitfalls": [
            "Overlooking zero, negative, or empty collection edge cases.",
            "Integer overflow in 32-bit signed environments when summing large bounds.",
            "Confusing necessary conditions with sufficient conditions (fallacy of affirming the consequent).",
            "Failing to account for non-consecutive or unsorted input conditions."
        ],
        "shortcuts": [
            "Use elimination of extremes: in multiple-choice exams, calculate boundary cases (N=0, N=1) first to eliminate 2 out of 4 options immediately.",
            "Leverage parity, digital roots, and bitwise identities to bypass extensive manual arithmetic.",
            "Check units and dimensional homogeneity before evaluating complicated formulas."
        ],
        "placement_notes": f"Companies frequently evaluate {topic_name} in Round 1 online assessments (OA) and technical face-to-face interviews. Focus on writing clean code, stating time-space complexity proactively, and validating corner cases."
    }
