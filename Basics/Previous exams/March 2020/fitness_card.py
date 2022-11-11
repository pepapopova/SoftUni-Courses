budget = float(input())
gender = input()
age = int(input())
sport = input()
cost = 0

if gender == "m":
    if sport == "Gym":
        cost = 42
    elif sport == "Boxing":
        cost = 41
    elif sport == "Yoga":
        cost = 45
    elif sport == "Zumba":
        cost = 34
    elif sport == "Dances":
        cost = 51
    else:
        cost = 39
else:
    if sport == "Gym":
        cost = 35
    elif sport == "Boxing":
        cost = 37
    elif sport == "Yoga":
        cost = 42
    elif sport == "Zumba":
        cost = 31
    elif sport == "Dances":
        cost = 53
    else:
        cost = 37

if age <= 19:
    cost *= 0.8

if budget >= cost:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    diff = cost - budget
    print(f"You don't have enough money! You need ${diff:.2f} more.")