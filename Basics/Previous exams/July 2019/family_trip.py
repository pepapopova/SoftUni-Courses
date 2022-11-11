budget = float(input())
number_nights = int(input())
price_for_night = float(input())
additional_expenses = int(input())

if number_nights > 7:
    price_for_night *= 0.95

total_cost = number_nights * price_for_night
additional_cost = budget * (additional_expenses / 100)
total_cost += additional_cost
diff = abs(budget - total_cost)
if total_cost <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")