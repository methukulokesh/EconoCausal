
from pathlib import Path
import pandas as pd

file_path = Path("data/processed/causal_data.csv")
df = pd.read_csv(file_path, parse_dates=["Date"])

print("DATASET SHAPE:", df.shape)
print("\nPRICE SUMMARY:")
print(df["Price"].describe().round(2))

print("\nUNIQUE VALUES:")
for col in [
    "Price", "Discount", "Promotion",
    "Competitor Pricing", "Store ID", "Product ID"
]:
    if col in df.columns:
        print(f"{col}: {df[col].nunique()}")

print("\nPRICE VARIATION WITHIN EACH PRODUCT-STORE:")
price_variation = (
    df.groupby(["Store ID", "Product ID"])["Price"]
    .nunique()
)

print("Product-store combinations:", len(price_variation))
print("Combinations with changing prices:",
      (price_variation > 1).sum())
print("Combinations with fixed prices:",
      (price_variation == 1).sum())

print("\nAVERAGE SALES BY PROMOTION:")
print(df.groupby("Promotion")["Units Sold"].mean().round(2))

print("\nAVERAGE SALES BY DISCOUNT:")
print(df.groupby("Discount")["Units Sold"].mean().round(2))

print("\nCHECK COMPLETED.")
