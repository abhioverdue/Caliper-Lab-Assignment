import os
import requests

HEADERS = {
    "User-Agent": "CaliperProject/1.0 (student research project)",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*",
    "Connection": "keep-alive"
}


def convert_to_txt_url(url):
    """
    Convert SEC link → machine-friendly .txt endpoint
    """

    # extract identifiers
    base = "https://www.sec.gov/Archives/edgar/data/0000320193/000032019325000079/"
    txt_file = "0000320193-25-000079.txt"

    return base + txt_file


def fetch_filing(out_path="data/filing.txt"):
    url = convert_to_txt_url(None)

    print(f"[INFO] Fetching TXT filing: {url}")

    r = requests.get(url, headers=HEADERS, timeout=30)

    if r.status_code != 200:
        raise Exception(f"Failed: {r.status_code}")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(r.text)

    print(f"[SUCCESS] Saved → {out_path}")


if __name__ == "__main__":
    fetch_filing()