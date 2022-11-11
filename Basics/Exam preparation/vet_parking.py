number_days = int(input())
number_hours = int(input())
total_spend_for_the_day = 0
total = 0

for day in range(1, number_days + 1):
    for hour in range(1, number_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            cost = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            cost = 1.25
        else:
            cost = 1
        total_spend_for_the_day += cost
    total += total_spend_for_the_day
    print(f"Day: {day} - {total_spend_for_the_day:.2f} leva")
    total_spend_for_the_day = 0

print(f"Total: {total:.2f} leva")

