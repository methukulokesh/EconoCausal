
import pandas as pd
from pathlib import Path

file_path = Path("data/raw/retail_store_inventory.csv")
df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nPrice summary:")
print(df["Price"].describe())

print("\nUnique prices per product:")
print(df.groupby("Product ID")["Price"].nunique().describe())
