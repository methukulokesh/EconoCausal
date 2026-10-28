
from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/processed/causal_data.csv")
OUTPUT_PATH = Path("outputs/feature_timing_audit.csv")

FEATURES_TO_REVIEW = {
    "Price": (
        "Treatment",
        "Target intervention; not an ordinary control variable.",
    ),
    "Units Sold": (
        "Outcome",
        "Target variable; never include as an input feature.",
    ),
    "Demand": (
        "High risk",
        "Correlation with sales is high. Verify its definition and timing.",
    ),
    "Units Ordered": (
        "Needs investigation",
        "May reflect earlier demand or ordering decisions.",
    ),
    "Inventory Level": (
        "Needs investigation",
        "Verify whether measured before or after the pricing decision.",
    ),
    "Discount": (
        "Needs investigation",
        "May be part of the pricing intervention or a confounder.",
    ),
    "Promotion": (
        "Needs investigation",
        "Verify whether promotions influence both price and sales.",
    ),
    "Competitor Pricing": (
        "Potential control",
        "Verify it was measured before the outcome period.",
    ),
    "Store ID": (
        "Potential control",
        "Store identifier; consider store-level differences.",
    ),
    "Product ID": (
        "Potential control",
        "Product identifier; consider product-level differences.",
    ),
    "Date": (
        "Potential control",
        "Can help account for time patterns.",
    ),
    "Demand Forecast": (
        "Unavailable if absent",
        "Verify whether a genuine forecast exists in the source data.",
    ),
}

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
    rows = []

    for feature, (classification, reason) in FEATURES_TO_REVIEW.items():
        available = feature in df.columns

        rows.append({
            "Feature": feature,
            "Available": available,
            "Review Classification": (
                classification if available else "Missing from dataset"
            ),
            "Reason": reason,
        })

    report = pd.DataFrame(rows)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(OUTPUT_PATH, index=False)

    print("FEATURE TIMING AUDIT")
    print("=" * 60)
    print(report.to_string(index=False))
    print(f"\nSaved report: {OUTPUT_PATH}")
    print(
        "\nImportant: these are preliminary review labels. "
        "The dataset alone does not establish when each variable "
        "was measured or whether it is a valid causal control."
    )
    print("\nAUDIT COMPLETED.")

if __name__ == "__main__":
    main()
