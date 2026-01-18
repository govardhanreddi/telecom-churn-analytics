import pandas as pd
from sqlalchemy import create_engine

# ✅ Update these 4 values only
USER = "root"
PASSWORD = "Mgovi@123"
HOST = "127.0.0.1"
DB = "telecom_churn"

# MySQL connection (PyMySQL)
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB}")

# Test query
df = pd.read_sql("SELECT COUNT(*) AS rows_loaded FROM stg_telco_raw;", engine)
print(df)

# Load the modeled fact table (recommended for analysis)
fact = pd.read_sql("SELECT * FROM fact_customer_finance LIMIT 10;", engine)
print(fact.head())
