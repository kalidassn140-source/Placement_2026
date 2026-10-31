# builder/q_helper.py

def make_question(qid, category, group, topic_id, topic_name, diff, q_text, options, correct_idx, hint, explanation, step, tech, formula="", code=""):
    assert len(options) == 4, f"Options count must be 4 in {qid}, got {len(options)}"
    assert len(set(options)) == 4, f"Options must be distinct in {qid}: {options}"
    assert correct_idx in (0, 1, 2, 3), f"Correct index must be 0-3 in {qid}, got {correct_idx}"
    assert diff in ("Easy", "Medium", "Hard"), f"Invalid difficulty {diff} in {qid}"
    assert len(q_text.strip()) > 0, f"Empty question in {qid}"
    assert len(hint.strip()) > 0, f"Empty hint in {qid}"
    assert len(explanation.strip()) > 0, f"Empty explanation in {qid}"
    assert len(step.strip()) > 0, f"Empty step in {qid}"
    assert len(tech.strip()) > 0, f"Empty tech in {qid}"

    return {
        "id": qid,
        "category": category,
        "group": group,
        "topic_id": topic_id,
        "topic": topic_name,
        "difficulty": diff,
        "q": q_text,
        "o": options,
        "a": correct_idx,
        "h": hint,
        "e": explanation,
        "step": step,
        "tech": tech,
        "formula": formula,
        "code": code
    }
