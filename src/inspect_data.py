import pandas as pd
from pathlib import Path

# Load dataset
file_path = Path("data/raw/retail_store_inventory.csv")
df = pd.read_csv(file_path)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("===== DATASET OVERVIEW =====")
print("Shape:", df.shape)
print("Date range:", df["Date"].min(), "to", df["Date"].max())

print("\n===== CATEGORY DISTRIBUTION =====")
print(df["Category"].value_counts())

print("\n===== SALES SUMMARY =====")
print(df["Units Sold"].describe())

print("\n===== PRICE SUMMARY =====")
print(df["Price"].describe())

print("\n===== AVERAGE PRICE BY CATEGORY =====")
print(df.groupby("Category")["Price"].mean().round(2))

print("\n===== AVERAGE UNITS SOLD BY CATEGORY =====")
print(df.groupby("Category")["Units Sold"].mean().round(2))

print("\n===== MONTHLY UNITS SOLD =====")
monthly_sales = (
    df.set_index("Date")
    .resample("ME")["Units Sold"]
    .sum()
)
print(monthly_sales.head(12))
