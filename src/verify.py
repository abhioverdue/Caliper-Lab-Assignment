def verify(chunk, qa):
    """
    Lightweight rule-based verifier
    """

    answer = qa.get("answer", "").lower()
    chunk = chunk.lower()

    if len(answer.strip()) < 2:
        return False

    # basic keyword overlap check
    overlap = 0
    for word in answer.split():
        if word in chunk:
            overlap += 1

    return overlap >= 1