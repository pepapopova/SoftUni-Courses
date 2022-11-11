import math

average_speed = float(input())
liters_per_100 = float(input())

total_distance = 384400 * 2
time = math.ceil(total_distance / average_speed)
total_time = time + 3
gas = (total_distance * liters_per_100) / 100

print(total_time)
print(int(gas))

