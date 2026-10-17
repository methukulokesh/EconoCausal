
import pandas as pd

# Load the retail dataset
df = pd.read_csv("data/raw/retail_store_inventory.csv")

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check price changes for each product at each store
price_changes = (
    df.groupby(["Store ID", "Product ID"])["Price"]
    .nunique()
    .reset_index(name="unique_prices")
)

# Count product-store combinations with changing prices
changing_prices = price_changes[
    price_changes["unique_prices"] > 1
]

print("Total product-store combinations:", len(price_changes))
print("Combinations with changing prices:", len(changing_prices))

print("\nSample combinations with changing prices:")
print(changing_prices.head(10))
