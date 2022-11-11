days = int(input())
wins_day = 0
loses_day = 0
wins = 0
loses = 0
loses = 0
total_prize = 0
day_money = 0
tournament_is_won = True
for n in range(days):
    command = input()
    while command != "Finish":
        sport = command
        result = input()
        if result == "win":
            wins_day +=1
            day_money += 20
        elif result == "lose":
            loses_day += 1
        command = input()
    if wins_day > loses_day:
        day_money *= 1.1
    total_prize += day_money
    day_money = 0
    wins += wins_day
    wins_day = 0
    loses += loses_day
    loses_day = 0

if wins > loses:
    total_prize *= 1.2
    print(f"You won the tournament! Total raised money: {total_prize:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_prize:.2f}")




