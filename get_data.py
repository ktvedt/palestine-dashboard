#!/usr/bin/env python3
"""
Download the latest casualty data for Gaza from Tech For Palestine.

Fetches the unminified JSON dataset from the API and writes it to
`casualties_daily.json` in the repository root.
"""

import requests

DATA_URL = "https://data.techforpalestine.org/api/v2/casualties_daily.json"
OUTPUT_PATH = "casualties_daily.json"

def download_data(url: str = DATA_URL, output_path: str = OUTPUT_PATH) -> None:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    download_data()