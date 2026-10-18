
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
file_path = Path("data/raw/retail_store_inventory.csv")
df = pd.read_csv(file_path)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.dropna(subset=["Date"])

# Group data by date
daily_sales = df.groupby("Date")["Units Sold"].sum()
daily_price = df.groupby("Date")["Price"].mean()

# Create output folder
figures_dir = Path("outputs/figures")
figures_dir.mkdir(parents=True, exist_ok=True)

# Plot daily sales trend
plt.figure(figsize=(12, 5))
daily_sales.plot()
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Units Sold")
plt.tight_layout()
plt.savefig(figures_dir / "daily_sales_trend.png", dpi=300)
plt.close()

# Plot daily average price trend
plt.figure(figsize=(12, 5))
daily_price.plot()
plt.title("Daily Average Price Trend")
plt.xlabel("Date")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig(figures_dir / "daily_average_price_trend.png", dpi=300)
plt.close()

# Calculate correlation between daily price and sales
correlation = daily_price.corr(daily_sales)

print("Daily sales and price trend analysis completed.")
print(f"Daily price-sales correlation: {correlation:.4f}")
print("Charts saved in outputs/figures/")
