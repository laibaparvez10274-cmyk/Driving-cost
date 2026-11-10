"""Optional ML demonstration.

This model is trained on synthetic data from make_data.py. It demonstrates
the ML workflow; it is not a reliable real-world petrol-cost predictor.
The formula in app.py is the main estimator.
"""
from pathlib import Path

try:
    import pandas as pd
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error, r2_score
except ImportError:
    print("Optional packages missing. Run: pip install -r requirements.txt")
    raise SystemExit(1)

DATA_FILE = Path(__file__).with_name("driver_data.csv")


def main():
    if not DATA_FILE.exists():
        print("Dataset not found. First run: python make_data.py")
        return

    df = pd.read_csv(DATA_FILE)
    # Convert traffic text into numeric columns for the model.
    df = pd.get_dummies(df, columns=["traffic_level"], dtype=int)

    feature_columns = [
        "distance_km", "base_mileage_km_per_litre", "ac_on",
        "traffic_level_low", "traffic_level_normal", "traffic_level_heavy"
    ]
    X = df[feature_columns]
    y = df["total_cost"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("Optional model trained successfully.")
    print(f"Mean Absolute Error: Rs. {mean_absolute_error(y_test, predictions):.2f}")
    print(f"R2 score: {r2_score(y_test, predictions):.3f}")
    print("Reminder: these scores use synthetic sample data, not real road tests.")


if __name__ == "__main__":
    main()
