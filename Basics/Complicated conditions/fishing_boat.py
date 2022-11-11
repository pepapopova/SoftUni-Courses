budget = int(input())
season = input()
number_fishermen = int(input())
boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Winter":
    boat_price = 2600
else:
    boat_price = 4200

if number_fishermen <= 6:
    boat_price *= 0.9
elif 6 < number_fishermen <= 11:
    boat_price *= 0.85
elif number_fishermen > 11:
    boat_price *= 0.75

if number_fishermen % 2 == 0 and season != "Autumn":
    boat_price *= 0.95

difference = abs(boat_price - budget)

if budget >= boat_price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")