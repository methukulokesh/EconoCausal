
import pandas as pd
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
