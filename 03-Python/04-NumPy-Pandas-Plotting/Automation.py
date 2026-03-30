# Automation sample in Python - Fourth Day
# This file loads sample records into a DataFrame and appends rows to a CSV under Data/

from pathlib import Path

import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
CSV_PATH = SCRIPT_DIR / "Data" / "api_example.csv"

SAMPLE_DATA = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "city": "Cairo"},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "city": "Alexandria"},
    {"id": 3, "name": "Carol", "email": "carol@example.com", "city": "Giza"},
]


def fetch_data():
    return SAMPLE_DATA


def run_once():
    data = fetch_data()
    df = pd.json_normalize(data)
    df["timestamp"] = pd.to_datetime("now")
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not CSV_PATH.exists():
        df.to_csv(CSV_PATH, index=False)
    else:
        df.to_csv(CSV_PATH, mode="a", header=False, index=False)
    print("Rows captured:", len(df))
    print("Saved to:", CSV_PATH)
    print(df.head())
    return df


run_once()
