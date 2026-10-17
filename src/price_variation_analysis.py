
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/retail_store_inventory.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Check price changes for each store and product
price_changes = (
    df.groupby(["Store ID", "Product ID"])["Price"]
    .agg(unique_prices="nunique", min_price="min", max_price="max")
    .reset_index()
)

changing_prices = price_changes[
    price_changes["unique_prices"] > 1
].copy()

print("Total product-store combinations:", len(price_changes))
print("Combinations with changing prices:", len(changing_prices))
print("\nSample combinations with changing prices:")
print(changing_prices.head(10).to_string(index=False))

# Create chart
plt.figure(figsize=(10, 6))
plt.hist(price_changes["unique_prices"], bins=20, edgecolor="black")
plt.title("Number of Unique Prices per Store-Product Combination")
plt.xlabel("Number of Unique Prices")
plt.ylabel("Number of Store-Product Combinations")
plt.tight_layout()
plt.savefig(
    "outputs/figures/unique_prices_per_product_store.png",
    dpi=300
)
plt.show()

print("\nChart saved to outputs/figures/unique_prices_per_product_store.png")
