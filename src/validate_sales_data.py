
import pandas as pd
from pathlib import Path

file_path = Path("data/raw/sales_data.csv")
df = pd.read_csv(file_path)

print("===== DATASET OVERVIEW =====")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nColumn names:")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE CHECKS =====")
print("Fully duplicated rows:", df.duplicated().sum())

key_columns = ["Date", "Store ID", "Product ID"]
if all(col in df.columns for col in key_columns):
    print(
        "Duplicate date-store-product records:",
        df.duplicated(subset=key_columns).sum()
    )

print("\n===== NUMERIC SUMMARY =====")
print(df.describe().round(2).to_string())

print("\n===== DATA VALIDATION =====")
for col in ["Price", "Units Sold", "Discount", "Competitor Pricing"]:
    if col in df.columns:
                    print(col + ": minimum=" + str(df[col].min()) + ", maximum=" + str(df[col].max()))
print("\nDataset validation completed.")
