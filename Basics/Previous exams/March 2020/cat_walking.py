minutes_walk = int(input())
number_walks = int(input())
taken_calories = int(input())

total_burnt_calories = minutes_walk * number_walks * 5
if total_burnt_calories >= taken_calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burnt_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burnt_calories}.")