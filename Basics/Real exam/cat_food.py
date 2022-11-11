number_cats = int(input())
total_food = 0
counter_small_cats = 0
counter_big_cats = 0
counter_huge_cats = 0

for n in range(number_cats):
    daily_food = float(input())
    if 100 <= daily_food < 200:
        counter_small_cats += 1
    elif 200 <= daily_food < 300:
        counter_big_cats += 1
    elif 300 <= daily_food < 400:
        counter_huge_cats += 1
    total_food += daily_food

print(f"Group 1: {counter_small_cats} cats.")
print(f"Group 2: {counter_big_cats} cats.")
print(f"Group 3: {counter_huge_cats} cats.")
total_food /= 1000
total_food_price = total_food * 12.45
print(f"Price for food per day: {total_food_price:.2f} lv.")