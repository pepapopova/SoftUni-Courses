number_locations = int(input())
daily_mined = 0

for n in range(number_locations):
    average_daily_mine = float(input())
    number_days = int(input())
    for day in range(number_days):
        daily_mine = float(input())
        daily_mined += daily_mine
    daily_mined /= number_days
    if daily_mined >= average_daily_mine:
        print(f"Good job! Average gold per day: {daily_mined:.2f}.")
    else:
        diff = average_daily_mine - daily_mined
        print(f"You need {diff:.2f} gold.")
    daily_mined = 0