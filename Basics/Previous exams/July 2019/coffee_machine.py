drink = input()
sugar_preference = input()
number_drinks = int(input())

if drink == "Espresso":
    if sugar_preference == "Without":
        price = 0.9
        price *= 0.65
    elif sugar_preference == "Normal":
        price = 1
    else:
        price = 1.2
elif drink == "Cappuccino":
    if sugar_preference == "Without":
        price = 1
        price *= 0.65
    elif sugar_preference == "Normal":
        price = 1.2
    else:
        price = 1.6
else:
    if sugar_preference == "Without":
        price = 0.5
        price *= 0.65
    elif sugar_preference == "Normal":
        price = 0.6
    else:
        price = 0.7

if drink == "Espresso" and number_drinks >= 5:
    price *= 0.75

total_cost = price * number_drinks
if total_cost > 15:
    total_cost *= 0.8

print(f"You bought {number_drinks} cups of {drink} for {total_cost:.2f} lv.")