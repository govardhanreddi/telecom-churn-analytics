# Power BI dashboard

The existing GitHub repository contains `telecom_churn.pbix`. Keep that file when applying this polished package.

Recommended dashboard pages:

1. **Executive overview** — customers, churned customers, churn rate, total revenue, average monthly charge.
2. **Contract and service risk** — churn by contract, internet type and payment method.
3. **Churn drivers** — churn category, churn reason, satisfaction score and tenure bands.
4. **Customer geography** — churn and revenue by city using latitude/longitude.

Use the generated files in `reports/` or connect Power BI to the `customer_churn` MySQL table/views.

Before publishing screenshots, verify that the displayed filters and totals match `reports/overview_metrics.json`.
