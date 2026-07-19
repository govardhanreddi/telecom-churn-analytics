USE telecom_churn;

CREATE OR REPLACE VIEW vw_churn_overview AS
SELECT
    COUNT(*) AS customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(AVG(churn_flag), 4) AS churn_rate,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(AVG(monthly_charge), 2) AS average_monthly_charge,
    ROUND(AVG(tenure_in_months), 2) AS average_tenure_months
FROM customer_churn;

CREATE OR REPLACE VIEW vw_churn_by_contract AS
SELECT
    contract,
    COUNT(*) AS customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(AVG(churn_flag), 4) AS churn_rate
FROM customer_churn
GROUP BY contract;

CREATE OR REPLACE VIEW vw_churn_by_internet_type AS
SELECT
    COALESCE(internet_type, 'No internet type') AS internet_type,
    COUNT(*) AS customers,
    SUM(churn_flag) AS churned_customers,
    ROUND(AVG(churn_flag), 4) AS churn_rate
FROM customer_churn
GROUP BY COALESCE(internet_type, 'No internet type');

CREATE OR REPLACE VIEW vw_churn_categories AS
SELECT
    churn_category,
    COUNT(*) AS churned_customers
FROM customer_churn
WHERE churn_flag = 1
GROUP BY churn_category;
