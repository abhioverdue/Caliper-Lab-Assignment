import json
import os
from tqdm import tqdm

from src.chunker import load_chunks
from src.generate_qa import generate_qa
from src.verify import verify
from src.scorer import score_qa


def run_pipeline():

    chunks = load_chunks()

    dataset = []
    rejected = []

    for chunk in tqdm(chunks):

        qa_list = generate_qa(chunk)

        for qa in qa_list:

            qa["score"] = score_qa(qa)

            if qa["score"] >= 1:
                dataset.append(qa)
            else:
                rejected.append(qa)

        if len(dataset) >= 120:
            break

    # save dataset
    import os

    os.makedirs("output", exist_ok=True)
    with open("output/qa_dataset.jsonl", "w") as f:
        for d in dataset[:100]:
            f.write(json.dumps(d) + "\n")

    with open("output/rejected.jsonl", "w") as f:
        for r in rejected:
            f.write(json.dumps(r) + "\n")

    print(f"[DONE] Accepted: {len(dataset)} | Rejected: {len(rejected)}")


if __name__ == "__main__":
    run_pipeline()