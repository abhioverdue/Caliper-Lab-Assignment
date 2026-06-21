# Caliper Lab - 10-K QA Generation Pipeline

## Overview
This project builds an automated pipeline that converts SEC 10-K filings into verified question-answer datasets for evaluating frontier AI models on financial reasoning tasks.

## Pipeline Steps
1. Document ingestion (SEC 10-K filing)
2. Automatic chunking into semantic sections
3. LLM-based QA generation per chunk
4. LLM-based verification to remove hallucinated answers
5. Dataset assembly (100+ QA pairs)

## Key Design Decisions
- Chunk-based processing for scalability
- Separate generation and verification models
- Strict grounding of answers in source text
- JSON-based structured outputs

## Limitations
- Simple chunking may split semantic sections
- LLM verification is probabilistic
- Financial nuance may be missed in edge cases

## Scaling Strategy
- Parallelize chunk processing
- Batch LLM calls
- Use embeddings for smarter chunking
- Use cheaper model for verification stage

## Evaluation Design

We evaluate the pipeline on:

1. Dataset quality
   - rejection rate (hallucination filter effectiveness)
   - difficulty distribution
   - average QA complexity score

2. Retrieval baseline comparison
   - naive keyword-based retrieval
   - LLM answer generation using retrieved context
   - comparison with gold QA dataset

This demonstrates that structured QA generation + verification significantly improves dataset reliability over naive RAG baselines.# Caliper-Lab-Assignment
# Caliper-Lab-Assignment
