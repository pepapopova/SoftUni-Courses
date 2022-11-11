import math

number_balls = int(input())
total_points = 0
red_balls_count = 0
orange_balls_count = 0
yellow_balls_count = 0
white_balls_count = 0
black_balls_count = 0
other_colors_picked = 0

for ball in range(number_balls):
    ball_color = input()
    if ball_color == "red":
        red_balls_count += 1
        total_points += 5
    elif ball_color == "orange":
        orange_balls_count += 1
        total_points += 10
    elif ball_color == "yellow":
        yellow_balls_count += 1
        total_points += 15
    elif ball_color == "white":
        white_balls_count += 1
        total_points += 20
    elif ball_color == "black":
        black_balls_count += 1
        total_points /= 2
        total_points = math.floor(total_points)
    else:
        other_colors_picked += 1

print(f"Total points: {total_points}")
print(f"Points from red balls: {red_balls_count}")
print(f"Points from orange balls: {orange_balls_count}")
print(f"Points from yellow balls: {yellow_balls_count}")
print(f"Points from white balls: {white_balls_count}")
print(f"Other colors picked: {other_colors_picked}")
print(f"Divides from black balls: {black_balls_count}")