"""Reusable customer-churn analysis functions."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {
    "Customer ID",
    "Churn Label",
    "Customer Status",
    "Contract",
    "Internet Type",
    "Payment Method",
    "Monthly Charge",
    "Total Revenue",
    "Tenure in Months",
    "Churn Category",
}


def load_telco_data(path: str | Path) -> pd.DataFrame:
    """Load the telecom CSV and validate the fields used in this analysis."""
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset not found: {csv_path}")
    frame = pd.read_csv(csv_path)
    missing = REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
    if frame["Customer ID"].duplicated().any():
        raise ValueError("Customer ID must be unique")

    result = frame.copy()
    result["churn_flag"] = result["Churn Label"].astype(str).str.casefold().eq("yes")
    return result


def calculate_overview(frame: pd.DataFrame) -> dict[str, int | float]:
    """Calculate portfolio-level metrics from a validated dataframe."""
    if "churn_flag" not in frame:
        frame = frame.assign(
            churn_flag=frame["Churn Label"].astype(str).str.casefold().eq("yes")
        )
    return {
        "customers": int(len(frame)),
        "churned_customers": int(frame["churn_flag"].sum()),
        "churn_rate": float(frame["churn_flag"].mean()),
        "total_revenue": float(frame["Total Revenue"].sum()),
        "average_monthly_charge": float(frame["Monthly Charge"].mean()),
        "average_tenure_months": float(frame["Tenure in Months"].mean()),
    }


def segment_churn(frame: pd.DataFrame, dimension: str) -> pd.DataFrame:
    """Return customer count, churn count and churn rate by a dimension."""
    if dimension not in frame.columns:
        raise ValueError(f"Unknown dimension: {dimension}")
    if "churn_flag" not in frame:
        frame = frame.assign(
            churn_flag=frame["Churn Label"].astype(str).str.casefold().eq("yes")
        )

    summary = (
        frame.groupby(dimension, dropna=False)
        .agg(
            customers=("Customer ID", "count"),
            churned_customers=("churn_flag", "sum"),
        )
        .reset_index()
    )
    summary["churn_rate"] = summary["churned_customers"] / summary["customers"]
    return summary.sort_values("churn_rate", ascending=False).reset_index(drop=True)


def churn_categories(frame: pd.DataFrame) -> pd.DataFrame:
    """Count churned customers by recorded churn category."""
    if "churn_flag" not in frame:
        frame = frame.assign(
            churn_flag=frame["Churn Label"].astype(str).str.casefold().eq("yes")
        )
    result = (
        frame.loc[frame["churn_flag"], "Churn Category"]
        .fillna("Not recorded")
        .value_counts()
        .rename_axis("churn_category")
        .reset_index(name="churned_customers")
    )
    result["share_of_churn"] = result["churned_customers"] / result[
        "churned_customers"
    ].sum()
    return result
