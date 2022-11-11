#while cycle - 100/100 correct
purchased_food = int(input())
purchased_food *= 1000
command = input()
food_is_enough = True
while command != "Adopted":
    eaten_food = int(command)
    purchased_food -= eaten_food
    command = input()

if purchased_food < 0:
    food_is_enough = False

if food_is_enough:
    print(f"Food is enough! Leftovers: {purchased_food} grams.")
else:
    print(f"Food is not enough. You need {abs(purchased_food)} grams more.")