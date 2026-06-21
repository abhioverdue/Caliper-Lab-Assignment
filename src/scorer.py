def score_qa(qa):

    score = 1

    if qa["type"] == "fact":
        score += 0

    if qa["type"] == "inference":
        score += 1

    if qa["type"] == "comparison":
        score += 2

    if "%" in qa["answer"] or "$" in qa["answer"]:
        score += 1

    return score