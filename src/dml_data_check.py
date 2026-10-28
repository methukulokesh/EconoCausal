
from pathlib import Path
import pandas as pd

data_path = Path("data/processed/causal_data.csv")
df = pd.read_csv(data_path, parse_dates=["Date"])

print("DATASET SHAPE:", df.shape)
print("\nCOLUMNS:")
print(df.columns.tolist())

# Check required variables
required = [
    "Price",
    "Units Sold",
    "Discount",
    "Promotion",
    "Competitor Pricing",
    "Store ID",
    "Product ID",
    "Date",
]

print("\nREQUIRED VARIABLE CHECK:")
for col in required:
    if col in df.columns:
        print(f"{col}: available")
    else:
        print(f"{col}: MISSING")

# Check missing values
print("\nMISSING VALUES:")
print(df[required].isnull().sum()
      if all(col in df.columns for col in required)
      else "Some required columns are missing.")

# Check whether price and sales vary
print("\nPRICE SUMMARY:")
print(df["Price"].describe().round(2))

print("\nUNITS SOLD SUMMARY:")
print(df["Units Sold"].describe().round(2))

print("\nUNIQUE PRICES:", df["Price"].nunique())
print("UNIQUE SALES VALUES:", df["Units Sold"].nunique())

# Check zero-sales records
print("\nZERO-SALES ROWS:", (df["Units Sold"] == 0).sum())

# Check whether important potential confounders exist
possible_controls = [
    "Weather Condition",
    "Seasonality",
    "Demand",
    "Inventory Level",
    "Category",
    "Region",
]

print("\nADDITIONAL CONTROL VARIABLES:")
for col in possible_controls:
    print(f"{col}: {'available' if col in df.columns else 'missing'}")

print("\nDATA CHECK COMPLETED.")

print("\nCHECKING DEMAND AND INVENTORY RELATIONSHIPS:")

for col in ["Demand", "Inventory Level", "Demand Forecast"]:
    if col in df.columns:
        print(f"\n{col} vs Units Sold:")
        print(
            df[[col, "Units Sold"]]
            .corr(numeric_only=True)
            .round(3)
        )

print("\nCORRELATION OF PRICE WITH NUMERIC VARIABLES:")
numeric_cols = [
    col for col in [
        "Price", "Discount", "Competitor Pricing",
        "Demand", "Inventory Level", "Units Sold"
    ]
    if col in df.columns
]

print(df[numeric_cols].corr().round(3))

print("\nPRICE VS COMPETITOR PRICING CHECK:")

print(
    "Overall correlation:",
    round(df["Price"].corr(df["Competitor Pricing"]), 4)
)

print("\nPrice minus competitor price:")
df["Price Difference"] = (
    df["Price"] - df["Competitor Pricing"]
)
print(df["Price Difference"].describe().round(2))

print("\nPrice relationship by category:")
print(
    df.groupby("Category")
    .apply(
        lambda group: group["Price"].corr(
            group["Competitor Pricing"]
        ),
        include_groups=False
    )
    .round(3)
)

print("\nWITHIN-PRODUCT PRICE VARIATION:")

product_price = (
    df.groupby("Product ID")["Price"]
    .agg(["count", "nunique", "mean", "std"])
)

print("Number of products:", len(product_price))
print(
    "Products with changing prices:",
    int((product_price["nunique"] > 1).sum())
)
print(
    "Products with fixed prices:",
    int((product_price["nunique"] == 1).sum())
)

print("\nSAMPLE PRODUCTS WITH PRICE VARIATION:")
print(
    product_price[product_price["nunique"] > 1]
    .head(10)
    .round(2)
)
