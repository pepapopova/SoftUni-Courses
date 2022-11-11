months = int(input())
water = 20
internet = 15
total_electricity = 0
total_others = 0

for m in range(months):
    electricity = float(input())
    total_electricity += electricity
    others = 1.2 * (electricity + water + internet)
    total_others += others

total_water = water * months
total_internet = internet * months
average_expenses = (total_internet + total_water + total_others + total_electricity) / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average_expenses:.2f} lv")
