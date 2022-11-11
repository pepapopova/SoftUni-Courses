import math

number_tournaments = int(input())
starting_points = int(input())
tour_points = 0
count_winner = 0

for x in range(number_tournaments):
    position = input()
    if position == "W":
        tour_points += 2000
        count_winner +=1
    elif position == "F":
        tour_points += 1200
    elif position == "SF":
        tour_points += 720

total_points = starting_points + tour_points
average_tour_points = math.floor(tour_points / number_tournaments)
winner_percent = count_winner / number_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_tour_points}")
print(f"{winner_percent:.2f}%")