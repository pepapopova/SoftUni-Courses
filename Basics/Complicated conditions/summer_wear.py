degree = int(input())
time = input()
outfit = ''
shoes = ''

if time == "Morning":
    if 10 <= degree <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degree <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degree >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time == "Afternoon":
    if 10 <= degree <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degree <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degree >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
else:
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {degree} degrees, get your {outfit} and {shoes}.")