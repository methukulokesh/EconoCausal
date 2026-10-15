
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load dataset
file_path = Path("data/raw/retail_store_inventory.csv")
df = pd.read_csv(file_path)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Create output folder
output_dir = Path("outputs")
output_dir.mkdir(parents=True, exist_ok=True)

# Prepare EDA report
report = [
    f"Dataset shape: {df.shape}",
    f"Date range: {df['Date'].min()} to {df['Date'].max()}",
    f"Missing values:\n{df.isnull().sum().to_string()}",
    f"Duplicate rows: {df.duplicated().sum()}",
    f"Category distribution:\n{df['Category'].value_counts().to_string()}",
    f"Sales summary:\n{df['Units Sold'].describe().to_string()}",
    f"Price summary:\n{df['Price'].describe().to_string()}",
    f"Average price by category:\n{df.groupby('Category')['Price'].mean().round(2).to_string()}",
    f"Average units sold by category:\n{df.groupby('Category')['Units Sold'].mean().round(2).to_string()}",
]

# Save report
report_path = output_dir / "eda_report.txt"
report_path.write_text("\n\n".join(report), encoding="utf-8")

print("EDA report saved to:", report_path)
print("EDA analysis completed successfully!")
# Create visualizations
figures_dir = output_dir / "figures"
figures_dir.mkdir(parents=True, exist_ok=True)

# 1. Price distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=30, edgecolor="black")
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(figures_dir / "price_distribution.png")
plt.close()

# 2. Average price by category
df.groupby("Category")["Price"].mean().plot(kind="bar")
plt.title("Average Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(figures_dir / "average_price_by_category.png")
plt.close()

# 3. Average units sold by category
df.groupby("Category")["Units Sold"].mean().plot(kind="bar")
plt.title("Average Units Sold by Category")
plt.xlabel("Category")
plt.ylabel("Average Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(figures_dir / "average_units_sold_by_category.png")
plt.close()

print("Charts saved to:", figures_dir)