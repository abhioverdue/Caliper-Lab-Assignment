
# QA GENERATION PROMPT


QA_GENERATION_PROMPT = """
You are an expert financial analyst generating a high-quality dataset.

Given a 10-K section, generate 6 question-answer pairs.

Requirements:
- 2 factual extraction questions
- 2 numeric reasoning questions
- 1 comparison question
- 1 inference question

Rules:
- Answers must be strictly grounded in the text
- Keep answers short and precise
- Include evidence sentence for each QA pair

Return ONLY valid JSON:

[
  {
    "question": "...",
    "answer": "...",
    "type": "fact|numeric|comparison|inference",
    "difficulty": "easy|medium|hard",
    "evidence": "exact sentence from text"
  }
]

TEXT:
{chunk}
"""


# VERIFICATION PROMPT


VERIFICATION_PROMPT = """
You are a strict financial QA verifier.

Your job is to ensure the answer is fully supported by the passage.

Return ONLY JSON:
{
  "valid": true/false,
  "reason": "short explanation"
}

Rules:
- If answer is even slightly unsupported → mark false
- No assumptions allowed

PASSAGE:
{passage}

QUESTION:
{q}

ANSWER:
{a}
"""