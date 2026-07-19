"""Generate reproducible CSV, JSON and PNG outputs from the raw dataset."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt

from telecom_churn.analysis import (
    calculate_overview,
    churn_categories,
    load_telco_data,
    segment_churn,
)

ROOT = Path(__file__).parents[1]
DATA = ROOT / "data" / "raw" / "telco.csv"
REPORTS = ROOT / "reports"
ASSETS = ROOT / "assets"


def _save_bar_chart(frame, label_column: str, value_column: str, title: str, output: Path) -> None:
    figure, axis = plt.subplots(figsize=(8, 4.5))
    axis.bar(frame[label_column].astype(str), frame[value_column])
    axis.set_title(title)
    axis.set_ylabel(value_column.replace("_", " ").title())
    axis.tick_params(axis="x", rotation=25)
    figure.tight_layout()
    figure.savefig(output, dpi=160)
    plt.close(figure)


def main() -> None:
    REPORTS.mkdir(exist_ok=True)
    ASSETS.mkdir(exist_ok=True)
    frame = load_telco_data(DATA)

    overview = calculate_overview(frame)
    (REPORTS / "overview_metrics.json").write_text(
        json.dumps(overview, indent=2), encoding="utf-8"
    )

    contract = segment_churn(frame, "Contract")
    internet = segment_churn(frame, "Internet Type")
    payment = segment_churn(frame, "Payment Method")
    categories = churn_categories(frame)

    contract.to_csv(REPORTS / "churn_by_contract.csv", index=False)
    internet.to_csv(REPORTS / "churn_by_internet_type.csv", index=False)
    payment.to_csv(REPORTS / "churn_by_payment_method.csv", index=False)
    categories.to_csv(REPORTS / "churn_categories.csv", index=False)

    _save_bar_chart(
        contract,
        "Contract",
        "churn_rate",
        "Customer churn rate by contract",
        ASSETS / "churn_by_contract.png",
    )
    _save_bar_chart(
        categories,
        "churn_category",
        "churned_customers",
        "Recorded reasons for churn",
        ASSETS / "churn_categories.png",
    )
    print(f"Reports written to {REPORTS}")


if __name__ == "__main__":
    main()
