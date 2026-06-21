import numpy as np

def naive_retrieve(chunks, question):

    q_words = set(question.lower().split())

    scores = []

    for c in chunks:
        c_words = set(c.lower().split())
        scores.append(len(q_words.intersection(c_words)))

    return chunks[int(np.argmax(scores))]