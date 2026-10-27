
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# 1. Load and sort the dataset chronologically
data_path = Path("data/processed/causal_data.csv")

df = pd.read_csv(data_path, parse_dates=["Date"])
df = df.dropna(subset=["Date", "Units Sold"])
df = df.sort_values("Date").reset_index(drop=True)

target = "Units Sold"

numeric_features = [
    "Price",
    "Discount",
    "Promotion",
    "Competitor Pricing",
    "Inventory Level",
    "Month",
    "DayOfWeek",
]

categorical_features = [
    "Store ID",
    "Product ID",
    "Category",
    "Region",
    "Weather Condition",
    "Seasonality",
]

features = numeric_features + categorical_features

# Verify required columns exist
required_columns = features + [target]
missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

# 2. Split earlier dates for training and later dates for testing
split_index = int(len(df) * 0.8)

train = df.iloc[:split_index].copy()
test = df.iloc[split_index:].copy()

X_train = train[features]
y_train = train[target]
X_test = test[features]
y_test = test[target]

# 3. Prepare numerical and categorical features
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features),
])

# 4. Compare a simple baseline with a smaller Random Forest
models = {
    "Dummy baseline": DummyRegressor(strategy="mean"),
    "Random Forest": RandomForestRegressor(
        n_estimators=30,
        max_depth=12,
        min_samples_leaf=5,
        random_state=42,
        n_jobs=-1,
    ),
}

results = []

print("CHRONOLOGICAL MODEL EVALUATION")
print("=" * 35)
print(
    f"Training dates: {train['Date'].min().date()} "
    f"to {train['Date'].max().date()}"
)
print(
    f"Testing dates:  {test['Date'].min().date()} "
    f"to {test['Date'].max().date()}"
)
print(f"Training rows: {len(train):,}")
print(f"Testing rows:  {len(test):,}")

# 5. Train and evaluate each model
for name, regressor in models.items():
    print(f"\nTraining {name}...", flush=True)

    model = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", regressor),
    ])

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    results.append({
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2,
    })

    print(f"MAE:  {mae:.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"R2:   {r2:.3f}")

# 6. Save the comparison results
output_path = Path("outputs/temporal_baseline_results.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

pd.DataFrame(results).to_csv(output_path, index=False)

print(f"\nResults saved to: {output_path}")
print("\nEvaluation completed.")
