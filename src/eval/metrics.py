from collections import Counter

def compute_metrics(dataset, rejected):

    total = len(dataset) + len(rejected)

    difficulty_dist = Counter([
        d.get("difficulty", "unknown") for d in dataset
    ])

    avg_score = sum([
        d.get("score", 0) for d in dataset
    ]) / max(len(dataset), 1)

    rejection_rate = len(rejected) / max(total, 1)

    return {
        "total_samples": total,
        "accepted": len(dataset),
        "rejected": len(rejected),
        "rejection_rate": rejection_rate,
        "avg_score": avg_score,
        "difficulty_distribution": dict(difficulty_dist)
    }