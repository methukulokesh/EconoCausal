
from pathlib import Path

import numpy as np
import pandas as pd

DATA_PATH = Path("data/processed/causal_data.csv")
OUTPUT_PATH = Path("outputs/feature_leakage_audit.csv")

TARGET = "Units Sold"

# Variables requiring careful review before causal modeling.
SUSPICIOUS_FEATURES = [
    "Demand",
    "Demand Forecast",
    "Units Ordered",
    "Inventory Level",
]

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}\n"
            "Check that data/processed/causal_data.csv exists."
        )

    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])

    if TARGET not in df.columns:
        raise ValueError(f"Target column '{TARGET}' is missing.")

    print("=" * 60)
    print("ECONOCAUSAL — FEATURE LEAKAGE AUDIT")
    print("=" * 60)

    print(f"Dataset rows: {len(df):,}")
    print(f"Dataset columns: {len(df.columns)}")
    print(f"Target: {TARGET}")

    # Check duplicate records and missing values.
    print("\n1. DATA QUALITY")
    print("Duplicate rows:", int(df.duplicated().sum()))
    print("Missing target values:", int(df[TARGET].isna().sum()))

    # Summarize numeric relationships with the target.
    numeric_df = df.select_dtypes(include=np.number)
    correlations = numeric_df.corr()[TARGET].drop(TARGET)

    print("\n2. NUMERIC FEATURE CORRELATIONS WITH UNITS SOLD")
    print(correlations.sort_values(key=abs, ascending=False).round(3))

    # Flag variables for investigation, not automatic deletion.
    print("\n3. FEATURES REQUIRING LEAKAGE REVIEW")

    rows = []

    for feature in SUSPICIOUS_FEATURES:
        if feature not in df.columns:
            print(f"{feature}: not available")
            continue

        corr = (
            df[feature].corr(df[TARGET])
            if pd.api.types.is_numeric_dtype(df[feature])
            else np.nan
        )

        print(
            f"{feature}: available; "
            f"correlation with Units Sold = "
            f"{corr:.3f}" if pd.notna(corr)
            else f"{feature}: available; numeric correlation unavailable"
        )

        rows.append({
            "Feature": feature,
            "Available": True,
            "Correlation with Units Sold": corr,
            "Review Required": True,
            "Reason": (
                "Check when and how this variable is measured. "
                "It may contain future information or be affected "
                "by pricing or sales."
            ),
        })

    # Price is the treatment, not an ordinary control, in this project.
    rows.append({
        "Feature": "Price",
        "Available": "Price" in df.columns,
        "Correlation with Units Sold": (
            df["Price"].corr(df[TARGET])
            if "Price" in df.columns else np.nan
        ),
        "Review Required": True,
        "Reason": (
            "Treatment variable: estimate its effect rather than "
            "automatically treating it as a control."
        ),
    })

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUTPUT_PATH, index=False)

    print(f"\nAudit summary saved to: {OUTPUT_PATH}")
    print("\nIMPORTANT:")
    print(
        "Correlation alone cannot prove data leakage. "
        "Confirm each variable's timing and how it was generated "
        "before selecting features for causal estimation."
    )
    print("\nFEATURE LEAKAGE AUDIT COMPLETED.")


if __name__ == "__main__":
    main()
