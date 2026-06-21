import re

def generate_qa(chunk):

    qa_list = []
    text = chunk.lower()


    # 1. NUMERIC EXTRACTION

    numbers = re.findall(r"\$?\d+(?:\.\d+)?%?", chunk)
    # -------------------------
# HARD: multi-signal chunks
# -------------------------
    has_money = "$" in chunk
    has_percent = "%" in chunk
    has_risk = "risk" in chunk.lower()
    has_number_density = len(re.findall(r"\d+", chunk)) > 5

    if (has_risk and has_percent) or (has_money and has_number_density):
         qa_list.append({
        "question": "What combined financial and risk-related patterns are described in this section?",
        "answer": "This section contains financial metrics and risk-related quantitative information",
        "type": "comparison",
        "difficulty": "hard",
        "evidence": chunk[:200]
    })
    if numbers:
        qa_list.append({
            "question": "What numerical values are mentioned in this section?",
            "answer": ", ".join(numbers[:5]),
            "type": "fact",
            "difficulty": "easy",
            "evidence": chunk[:200]
        })


    # 2. REVENUE QA

    if "revenue" in text:
        qa_list.append({
            "question": "What financial topic is discussed in this section?",
            "answer": "Revenue or financial performance",
            "type": "fact",
            "difficulty": "easy",
            "evidence": chunk[:200]
        })


    # 3. RISK QA

    if "risk" in text:
        qa_list.append({
            "question": "What category of information is discussed?",
            "answer": "Business and operational risks",
            "type": "inference",
            "difficulty": "medium",
            "evidence": chunk[:200]
        })


    # 4. PERCENTAGE QA

    if "%" in chunk:
        qa_list.append({
            "question": "What percentage values are mentioned in this section?",
            "answer": ", ".join([x for x in numbers if "%" in x][:3]) or "Percentage metrics present",
            "type": "inference",
            "difficulty": "medium",
            "evidence": chunk[:200]
        })


    # 5. REVENUE + MONEY (more meaningful signal)

    if "revenue" in text and "$" in chunk:
        qa_list.append({
            "question": "What financial figures are associated with revenue in this section?",
            "answer": "Revenue-related monetary values are reported",
            "type": "comparison",
            "difficulty": "hard",
            "evidence": chunk[:200]
        })


    # 6. FALLBACK (ONLY ONCE)

    if not qa_list:
        qa_list.append({
            "question": "What is this section mainly about?",
            "answer": "Financial disclosure content",
            "type": "fact",
            "difficulty": "easy",
            "evidence": chunk[:200]
        })
    if "risk" in text and "%" in chunk:
        qa_list.append({
        "question": "What quantified risks or changes are described in this section?",
        "answer": "Risk-related percentage changes are discussed",
        "type": "comparison",
        "difficulty": "hard",
        "evidence": chunk[:200]
    })

    # LIMIT OUTPUT PER CHUNK

    return qa_list[:3]