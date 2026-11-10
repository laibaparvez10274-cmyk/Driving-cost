"""
Petrol Cost Estimator for Drivers
Run: python app.py
Uses only Python's standard library.
"""

import csv
from datetime import datetime
from pathlib import Path

HISTORY_FILE = Path(__file__).with_name("trip_history.csv")


def estimate_trip(distance_km, mileage_km_per_litre, petrol_price,
                  traffic="normal", ac_on=False):
    """Return estimated fuel use and trip cost.

    Traffic/AC adjustments are simple estimates, not exact vehicle measurements.
    """
    traffic_adjustments = {
        "low": 0.00,
        "normal": 0.05,
        "heavy": 0.10,
    }

    if distance_km <= 0:
        raise ValueError("Distance must be greater than zero.")
    if mileage_km_per_litre <= 0:
        raise ValueError("Mileage must be greater than zero.")
    if petrol_price <= 0:
        raise ValueError("Petrol price must be greater than zero.")
    if traffic not in traffic_adjustments:
        raise ValueError("Traffic must be low, normal, or heavy.")

    # Reduce effective mileage to estimate extra fuel use in traffic/with AC.
    reduction = traffic_adjustments[traffic]
    if ac_on:
        reduction += 0.05
    effective_mileage = mileage_km_per_litre * (1 - reduction)

    fuel_litres = distance_km / effective_mileage
    total_cost = fuel_litres * petrol_price
    cost_per_km = total_cost / distance_km

    return {
        "effective_mileage": effective_mileage,
        "fuel_litres": fuel_litres,
        "total_cost": total_cost,
        "cost_per_km": cost_per_km,
    }


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number, for example 12 or 263.50.")


def get_choice(prompt, choices):
    choices_text = "/".join(choices)
    while True:
        value = input(f"{prompt} ({choices_text}): ").strip().lower()
        if value in choices:
            return value
        print(f"Please choose one of: {choices_text}")


def save_trip(trip):
    file_exists = HISTORY_FILE.exists()
    with HISTORY_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "date", "distance_km", "mileage_km_per_litre", "petrol_price",
            "traffic", "ac_on", "fuel_litres", "total_cost", "cost_per_km"
        ])
        if not file_exists:
            writer.writeheader()
        writer.writerow(trip)


def calculate_trip():
    print("\n--- ENTER TRIP DETAILS ---")
    distance = get_positive_number("Trip distance (KM): ")
    mileage = get_positive_number("Vehicle mileage (KM per litre): ")
    petrol_price = get_positive_number("Petrol price (Rs per litre): ")
    traffic = get_choice("Traffic level", ["low", "normal", "heavy"])
    ac_choice = get_choice("Is AC being used?", ["yes", "no"])
    ac_on = ac_choice == "yes"

    result = estimate_trip(distance, mileage, petrol_price, traffic, ac_on)

    print("\n========== TRIP ESTIMATE ==========")
    print(f"Distance:              {distance:.2f} KM")
    print(f"Original mileage:      {mileage:.2f} KM/L")
    print(f"Estimated mileage:     {result['effective_mileage']:.2f} KM/L")
    print(f"Petrol required:       {result['fuel_litres']:.2f} litres")
    print(f"Petrol price:          Rs. {petrol_price:,.2f}/litre")
    print(f"Estimated total cost:  Rs. {result['total_cost']:,.2f}")
    print(f"Estimated cost per KM: Rs. {result['cost_per_km']:,.2f}")
    print("===================================\n")
    print("Note: This is an estimate. Actual consumption varies by vehicle,")
    print("road, driving style, load, weather and fuel quality.")

    trip = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "distance_km": round(distance, 2),
        "mileage_km_per_litre": round(mileage, 2),
        "petrol_price": round(petrol_price, 2),
        "traffic": traffic,
        "ac_on": "Yes" if ac_on else "No",
        "fuel_litres": round(result["fuel_litres"], 2),
        "total_cost": round(result["total_cost"], 2),
        "cost_per_km": round(result["cost_per_km"], 2),
    }
    save_trip(trip)
    print("Trip saved in trip_history.csv")


def show_history():
    if not HISTORY_FILE.exists():
        print("\nNo saved trips yet. Calculate a trip first.\n")
        return

    print("\n================ SAVED TRIPS ================")
    with HISTORY_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No saved trips yet.")
        return

    total_distance = sum(float(row["distance_km"]) for row in rows)
    total_cost = sum(float(row["total_cost"]) for row in rows)
    total_fuel = sum(float(row["fuel_litres"]) for row in rows)

    for number, row in enumerate(rows, start=1):
        print(
            f"{number}. {row['date']} | {row['distance_km']} KM | "
            f"{row['fuel_litres']} L | Rs. {float(row['total_cost']):,.2f}"
        )

    print("---------------------------------------------")
    print(f"Total trips:       {len(rows)}")
    print(f"Total distance:    {total_distance:.2f} KM")
    print(f"Total petrol:      {total_fuel:.2f} litres")
    print(f"Total estimated cost: Rs. {total_cost:,.2f}\n")


def main():
    print("==========================================")
    print("       PETROL COST ESTIMATOR")
    print("==========================================")

    while True:
        print("\n1. Calculate a trip")
        print("2. View saved trip history")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            calculate_trip()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("\nThank you for using Petrol Cost Estimator!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
