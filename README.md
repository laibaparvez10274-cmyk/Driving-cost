# Petrol Cost Estimator for Drivers

A beginner-friendly Python program that estimates how much petrol a driver needs
for a trip and how much the trip may cost in Pakistani Rupees (PKR).

## Features
- Enter trip distance in kilometres.
- Enter your vehicle's mileage in kilometres per litre (KM/L).
- Enter petrol price in rupees per litre.
- Select low, normal, or heavy traffic.
- Select whether the AC is being used.
- View estimated fuel required, total cost, and cost per kilometre.
- Save trips automatically in `trip_history.csv`.
- View previous trips and total spending.

## Requirements
- Python 3.9 or newer
- VS Code (optional, but recommended)

The main program uses Python's standard library. No packages need to be installed.

## How to run in VS Code
1. Extract `driver_project.zip`.
2. Open the extracted `driver_project` folder in VS Code.
3. Open `app.py`.
4. Open Terminal > New Terminal.
5. Run:

   ```bash
   python app.py
   ```

   On some Windows installations, use:

   ```bash
   py app.py
   ```

6. Choose option 1 and enter your trip details.

## Example
- Distance: 100 KM
- Mileage: 15 KM/L
- Petrol price: Rs. 263/L
- Traffic: low
- AC: no

Estimated petrol: 6.67 litres
Estimated cost: Rs. 1,753.33
Estimated cost per KM: Rs. 17.53

(The displayed answer may differ slightly due to the exact values entered.)

## How the calculation works
Fuel required = Distance / Effective mileage

Trip cost = Fuel required x Petrol price per litre

Cost per kilometre = Trip cost / Distance

The traffic and AC options apply simple estimated mileage reductions:
- Low traffic: 0%
- Normal traffic: 5%
- Heavy traffic: 10%
- AC on: an additional 5%

These are illustrative assumptions, not measured values. For a more accurate
estimate, use the vehicle's actual mileage under similar driving conditions.

## Project files
- `app.py` - main runnable program.
- `trip_history.csv` - created automatically when the first trip is saved.
- `make_data.py` - optional synthetic sample dataset generator.
- `train_model.py` - optional machine-learning demonstration using that dataset.
- `requirements.txt` - packages for the optional ML demonstration.
