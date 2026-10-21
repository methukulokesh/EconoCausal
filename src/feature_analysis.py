
import pandas as pd
from pathlib import Path

# Load the validated sales dataset
file_path = Path("data/raw/sales_data.csv")
df = pd.read_csv(file_path)

print("DATASET SHAPE:", df.shape)

# Check how key variables relate to sales
numeric_columns = [
    "Price",
    "Discount",
    "Competitor Pricing",
    "Units Sold",
    "Demand",
]

available_columns = [col for col in numeric_columns if col in df.columns]

print("\nCORRELATION WITH UNITS SOLD")
print(
    df[available_columns]
    .corr(numeric_only=True)["Units Sold"]
    .sort_values(ascending=False)
    .round(3)
)

# Compare average sales for promotion and non-promotion records
if "Promotion" in df.columns:
    print("\nAVERAGE UNITS SOLD BY PROMOTION")
    print(df.groupby("Promotion")["Units Sold"].agg(
        ["count", "mean", "median"]
    ).round(2))

# Compare average sales by discount level
if "Discount" in df.columns:
    df["Discount Group"] = pd.cut(
        df["Discount"],
        bins=[-1, 0, 5, 10, 15, 25],
        labels=["0", "1-5", "6-10", "11-15", "16-25"]
    )

    print("\nAVERAGE UNITS SOLD BY DISCOUNT GROUP")
    print(df.groupby(
        "Discount Group", observed=False
    )["Units Sold"].agg(["count", "mean"]).round(2))

print("\nFeature analysis completed.")
print("\n=== CAUSAL ANALYSIS READINESS ===")

print("\nMissing values:")
print(df.isnull().sum().to_string())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nNumeric correlations with Units Sold:")
print(
    df.select_dtypes(include="number")
    .corr(numeric_only=True)["Units Sold"]
    .sort_values(ascending=False)
    .round(3)
    .to_string()
)