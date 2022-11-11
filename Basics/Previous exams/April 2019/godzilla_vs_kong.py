budget = float(input())
number_statists = int(input())
price_attire = float(input())
decor = 0.10 * budget
if number_statists > 150:
    price_attire *= 0.9

total_cost = number_statists * price_attire + decor
diff = abs(budget - total_cost)
if total_cost <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")


