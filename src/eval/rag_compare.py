import json

from utils.llm import call_llm
from src.eval.rag_baseline import naive_retrieve


def answer_with_llm(context, question):

    prompt = f"""
Answer the question using only the context.

Context:
{context}

Question:
{question}

Return only the answer.
"""

    return call_llm(prompt)


def run_rag_comparison(chunks, dataset, n=20):

    results = []

    for qa in dataset[:n]:

        q = qa["question"]

        context = naive_retrieve(chunks, q)
        rag_answer = answer_with_llm(context, q)

        results.append({
            "question": q,
            "gold_answer": qa["answer"],
            "rag_answer": rag_answer,
            "context": context
        })

    with open("output/rag_comparison.json", "w") as f:
        json.dump(results, f, indent=2)

    print("[OK] RAG comparison saved")