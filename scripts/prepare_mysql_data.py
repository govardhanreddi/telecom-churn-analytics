"""Create a snake_case CSV suitable for the supplied MySQL schema."""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).parents[1]
SOURCE = ROOT / "data" / "raw" / "telco.csv"
OUTPUT = ROOT / "data" / "processed" / "telco_clean.csv"


def snake_case(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    return re.sub(r"_+", "_", cleaned)


def main() -> None:
    frame = pd.read_csv(SOURCE)
    frame.columns = [snake_case(column) for column in frame.columns]
    frame["churn_flag"] = frame["churn_label"].astype(str).str.casefold().eq("yes").astype(int)
    frame.to_csv(OUTPUT, index=False)
    print(f"Wrote {len(frame):,} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
