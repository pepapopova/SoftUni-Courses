import math

days_away = int(input())
food_left = int(input())
food_deer1 = float(input())
food_deer2 = float(input())
food_deer3 = float(input())

total_food_needed = (food_deer1 + food_deer2 + food_deer3) * days_away
diff = abs(food_left - total_food_needed)
if food_left >= total_food_needed:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")