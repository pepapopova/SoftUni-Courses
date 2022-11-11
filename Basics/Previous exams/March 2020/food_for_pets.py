days = int(input())
total_food = float(input())
total_eaten_biscuits = 0
dog_food = 0
cat_food = 0
counter = 0
day_food = 0
for day in range(days):
    eaten_food_dog = int(input())
    eaten_food_cat = int(input())
    counter += 1
    dog_food += eaten_food_dog
    cat_food += eaten_food_cat
    day_food = eaten_food_dog + eaten_food_cat
    if counter % 3 == 0:
        total_eaten_biscuits += day_food * 0.1

print(f"Total eaten biscuits: {int(total_eaten_biscuits)}gr.")
total_eaten_food = dog_food + cat_food
percent_eaten_food = total_eaten_food / total_food * 100
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
percent_dog_eaten_food = dog_food / total_eaten_food * 100
print(f"{percent_dog_eaten_food:.2f}% eaten from the dog.")
percent_cat_eaten_food = cat_food / total_eaten_food * 100
print(f"{percent_cat_eaten_food:.2f}% eaten from the cat.")