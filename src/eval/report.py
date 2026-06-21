import json
from src.eval.metrics import compute_metrics


def load_jsonl(path):
    data = []
    with open(path, "r") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def generate_report():

    dataset = load_jsonl("output/qa_dataset.jsonl")
    rejected = load_jsonl("output/rejected.jsonl")

    report = compute_metrics(dataset, rejected)

    with open("output/eval_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    generate_report()