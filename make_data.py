"""Create a sample dataset for the optional ML demonstration.

The rows are synthetic examples, not real vehicle test measurements.
Run: python make_data.py
"""
import csv
import random
from pathlib import Path

OUTPUT_FILE = Path(__file__).with_name("driver_data.csv")


def main():
    random.seed(42)
    columns = [
        "distance_km", "base_mileage_km_per_litre",
        "traffic_level", "ac_on", "fuel_litres", "total_cost"
    ]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

        for _ in range(500):
            distance = random.randint(5, 500)
            mileage = random.uniform(8, 22)
            traffic = random.choice(["low", "normal", "heavy"])
            ac_on = random.randint(0, 1)

            reduction = {"low": 0.00, "normal": 0.05, "heavy": 0.10}[traffic]
            if ac_on:
                reduction += 0.05

            effective_mileage = mileage * (1 - reduction)
            fuel = distance / effective_mileage
            petrol_price = 263  # Sample price only; update for your assignment.
            cost = fuel * petrol_price

            writer.writerow({
                "distance_km": distance,
                "base_mileage_km_per_litre": round(mileage, 2),
                "traffic_level": traffic,
                "ac_on": ac_on,
                "fuel_litres": round(fuel, 2),
                "total_cost": round(cost, 2),
            })

    print(f"Created {OUTPUT_FILE.name} with 500 synthetic sample rows.")


if __name__ == "__main__":
    main()
