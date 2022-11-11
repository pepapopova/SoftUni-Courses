budget = float(input())
season = input()
price = 0
location = ""
stay = ""

if budget <= 1000:
    stay = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = 0.65 * budget
    else:
        location = "Morocco"
        price = 0.45 * budget
elif 1000 < budget <= 3000:
    stay = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = 0.8 * budget
    else:
        location = "Morocco"
        price = 0.6 * budget
elif budget > 3000:
    stay = "Hotel"
    price = budget * 0.9
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

print(f"{location} - {stay} - {price:.2f}")
