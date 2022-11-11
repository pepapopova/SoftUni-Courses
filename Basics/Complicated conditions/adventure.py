budget = float(input())
season = input()
price = 0
stay = ""
country = ""

if budget <= 100:
    country = "Bulgaria"
    if season == "summer":
        stay = "Camp"
        price = 0.3 * budget
    elif season == "winter":
        stay = "Hotel"
        price = 0.7 * budget
elif budget <= 1000:
    country = "Balkans"
    if season == "summer":
        stay = "Camp"
        price = 0.4 * budget
    elif season == "winter":
        stay = "Hotel"
        price = 0.8 * budget
elif budget > 1000:
    country = "Europe"
    stay = "Hotel"
    price = 0.9 * budget

print(f"Somewhere in {country}")
print(f"{stay} - {price:.2f}")
