import pandas as pd
import pytest

from telecom_churn.analysis import calculate_overview, segment_churn


def sample_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Customer ID": ["A", "B", "C"],
            "Churn Label": ["Yes", "No", "Yes"],
            "Contract": ["Monthly", "Annual", "Monthly"],
            "Total Revenue": [100.0, 200.0, 300.0],
            "Monthly Charge": [10.0, 20.0, 30.0],
            "Tenure in Months": [1, 10, 2],
        }
    )


def test_calculate_overview() -> None:
    metrics = calculate_overview(sample_frame())
    assert metrics["customers"] == 3
    assert metrics["churned_customers"] == 2
    assert metrics["churn_rate"] == pytest.approx(2 / 3)
    assert metrics["total_revenue"] == 600.0


def test_segment_churn_orders_highest_rate_first() -> None:
    result = segment_churn(sample_frame(), "Contract")
    assert result.iloc[0]["Contract"] == "Monthly"
    assert result.iloc[0]["churn_rate"] == 1.0


def test_segment_churn_rejects_unknown_dimension() -> None:
    with pytest.raises(ValueError, match="Unknown dimension"):
        segment_churn(sample_frame(), "Unknown")
