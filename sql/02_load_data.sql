USE telecom_churn;

-- First run: python scripts/prepare_mysql_data.py
-- Replace the path below with the absolute path to data/processed/telco_clean.csv.
-- MySQL may require LOCAL INFILE to be enabled for both client and server.

LOAD DATA LOCAL INFILE '/absolute/path/to/data/processed/telco_clean.csv'
INTO TABLE customer_churn
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

SELECT COUNT(*) AS rows_loaded FROM customer_churn;
