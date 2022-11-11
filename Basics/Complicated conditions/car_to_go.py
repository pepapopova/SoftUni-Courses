budget = float(input())
season = input()
clase = ""
type = ""

if budget <= 100:
    clase = "Economy class"
    if season == "Summer":
        type = "Cabrio"
        budget *= 0.35
    elif season == "Winter":
        type = "Jeep"
        budget *= 0.65
elif 100 < budget <= 500:
    clase = "Compact class"
    if season == "Summer":
        type = "Cabrio"
        budget *= 0.45
    elif season == "Winter":
        type = "Jeep"
        budget *= 0.80
elif budget > 500:
    clase = "Luxury class"
    type = "Jeep"
    budget *= 0.90

print(clase)
print(f"{type} - {budget:.2f}")