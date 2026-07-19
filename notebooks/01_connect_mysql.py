"""Secure MySQL connectivity check and example analytics query."""

from __future__ import annotations

import pandas as pd

from telecom_churn.database import create_mysql_engine


def main() -> None:
    engine = create_mysql_engine()
    row_count = pd.read_sql("SELECT COUNT(*) AS customers FROM customer_churn;", engine)
    print(row_count.to_string(index=False))

    contract_summary = pd.read_sql(
        """
        SELECT contract, customers, churned_customers, churn_rate
        FROM vw_churn_by_contract
        ORDER BY churn_rate DESC;
        """,
        engine,
    )
    print(contract_summary.to_string(index=False))


if __name__ == "__main__":
    main()
