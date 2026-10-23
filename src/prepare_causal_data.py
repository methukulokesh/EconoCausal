
from pathlib import Path

import pandas as pd

# Load the complete dataset
input_path = Path("data/raw/sales_data.csv")
output_path = Path("data/processed/causal_data.csv")

df = pd.read_csv(input_path)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Keep rows with valid dates and required values
required_columns = [
    "Date",
    "Store ID",
    "Product ID",
    "Price",
    "Discount",
    "Promotion",
    "Competitor Pricing",
    "Units Sold",
]

df = df.dropna(subset=required_columns).copy()

# Add time-related features
df["Month"] = df["Date"].dt.month
df["DayOfWeek"] = df["Date"].dt.dayofweek

# Save the prepared dataset
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("Causal dataset preparation completed.")
print("Dataset shape:", df.shape)
print("Saved to:", output_path)
print("Missing values in required columns:")
print(df[required_columns].isnull().sum())
