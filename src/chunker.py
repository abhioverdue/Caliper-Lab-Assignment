import re

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_text(text, size=800, overlap=150):
    text = clean_text(text)
    words = text.split()

    chunks = []
    i = 0

    while i < len(words):
        chunk = words[i:i + size]
        chunks.append(" ".join(chunk))
        i += size - overlap

    return chunks


def load_chunks(path="data/10k_raw.txt"):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    return chunk_text(text)