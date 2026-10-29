
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

DATA_PATH = Path("data/processed/causal_data.csv")
OUTPUT_PATH = Path("outputs/baseline_predictions.csv")

TARGET = "Units Sold"

FEATURES = [
    "Price",
    "Discount",
    "Promotion",
    "Competitor Pricing",
    "Store ID",
    "Product ID",
    "Category",
    "Region",
    "Inventory Level",
    "Weather Condition",
    "Seasonality",
    "Month",
    "DayOfWeek",
]

NUMERIC_FEATURES = [
    "Price",
    "Discount",
    "Promotion",
    "Competitor Pricing",
    "Inventory Level",
    "Month",
    "DayOfWeek",
]

CATEGORICAL_FEATURES = [
    "Store ID",
    "Product ID",
    "Category",
    "Region",
    "Weather Condition",
    "Seasonality",
]


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH, parse_dates=["Date"])

    required = ["Date", TARGET] + FEATURES
    missing = [column for column in required if column not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.dropna(subset=["Date", TARGET]).copy()
    df = df.sort_values("Date").reset_index(drop=True)

    # Train on earlier dates; test on later dates.
    unique_dates = sorted(df["Date"].unique())

    if len(unique_dates) < 2:
        raise ValueError("At least two distinct dates are required.")

    split_index = int(len(unique_dates) * 0.8)
    split_index = max(1, min(split_index, len(unique_dates) - 1))
    test_start_date = unique_dates[split_index]

    train_df = df[df["Date"] < test_start_date].copy()
    test_df = df[df["Date"] >= test_start_date].copy()

    if train_df.empty or test_df.empty:
        raise ValueError("Chronological split produced an empty dataset.")

    X_train = train_df[FEATURES]
    y_train = train_df[TARGET]
    X_test = test_df[FEATURES]
    y_test = test_df[TARGET]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
    ])

    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, NUMERIC_FEATURES),
        ("cat", categorical_pipeline, CATEGORICAL_FEATURES),
    ])

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(
            n_estimators=30,
            max_depth=12,
            min_samples_leaf=5,
            random_state=42,
            n_jobs=2,
        )),
    ])

    print("Training chronological baseline...", flush=True)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    print("\nCHRONOLOGICAL BASELINE RESULTS")
    print("--------------------------------")
    print(f"Training rows: {len(train_df):,}")
    print(f"Testing rows:  {len(test_df):,}")
    print(f"Training ends: {train_df['Date'].max().date()}")
    print(f"Testing starts: {test_df['Date'].min().date()}")
    print(f"MAE:  {mae:.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"R²:   {r2:.3f}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    pd.DataFrame({
        "Date": test_df["Date"].to_numpy(),
        "Actual Units Sold": y_test.to_numpy(),
        "Predicted Units Sold": predictions,
    }).to_csv(OUTPUT_PATH, index=False)

    print(f"\nPredictions saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
