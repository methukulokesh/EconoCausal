
from pathlib import Path
import pandas as pd

# Load prepared dataset
df = pd.read_csv(
    "data/processed/causal_data.csv",
    parse_dates=["Date"]
)

# Compare price and sales across promotion status
print("AVERAGE PRICE AND SALES BY PROMOTION")
print(
    df.groupby("Promotion")
    .agg(
        average_price=("Price", "mean"),
        average_sales=("Units Sold", "mean"),
        records=("Units Sold", "size")
    )
    .round(2)
)

# Compare price and sales across discount levels
print("\nAVERAGE PRICE AND SALES BY DISCOUNT")
print(
    df.groupby("Discount")
    .agg(
        average_price=("Price", "mean"),
        average_sales=("Units Sold", "mean"),
        records=("Units Sold", "size")
    )
    .round(2)
)

# Check whether prices vary within each product-store pair
price_counts = (
    df.groupby(["Store ID", "Product ID"])["Price"]
    .nunique()
)

print("\nPRODUCT-STORE PRICE VARIATION")
print("Total combinations:", len(price_counts))
print("Changing prices:", int((price_counts > 1).sum()))
print("Fixed prices:", int((price_counts == 1).sum()))

print("\nAnalysis completed.")
