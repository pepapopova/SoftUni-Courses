import math

number_people = int(input())
entrance_fee = float(input())
price_sunbed = float(input())
price_umbrella = float(input())

total_entrance = number_people * entrance_fee
total_sunbed = math.ceil(0.75 * number_people) * price_sunbed
total_umbrella = math.ceil(number_people / 2) * price_umbrella
total =total_entrance + total_umbrella + total_sunbed

print(f"{total:.2f} lv.")