
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# Load prepared dataset
data_path = Path("data/processed/causal_data.csv")
df = pd.read_csv(data_path)

# Define target and features
target = "Units Sold"

features = [
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

# Select required columns and remove rows with missing target
df = df[features + [target]].copy()
df = df.dropna(subset=[target])

X = df[features]
y = df[target]

# Define numerical and categorical features
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

# Preprocess numerical and categorical data
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore")),
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features),
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Build a faster baseline Random Forest model
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

# Train model
print("Training baseline model...", flush=True)
model.fit(X_train, y_train)

# Generate predictions
print("Evaluating model...", flush=True)
predictions = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("\nBASELINE MODEL RESULTS")
print("----------------------")
print(f"Training rows: {len(X_train):,}")
print(f"Testing rows: {len(X_test):,}")
print(f"MAE:  {mae:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"R²:   {r2:.3f}")

# Save predictions
output_path = Path("outputs/baseline_predictions.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

pd.DataFrame({
    "Actual Units Sold": y_test.to_numpy(),
    "Predicted Units Sold": predictions,
}).to_csv(output_path, index=False)

print(f"\nPredictions saved to: {output_path}")
