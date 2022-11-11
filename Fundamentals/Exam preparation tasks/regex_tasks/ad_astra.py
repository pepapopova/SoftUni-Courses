import re

food_string = input()

matches = re.finditer(r'([\||#])([a-zA-Z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1', food_string)
total_calories = 0
new_list = []
for match in matches:
    total_calories += int(match.group(4))
    new_list.append([match.group(2), match.group(3), match.group(4)])
days_to_last = total_calories // 2000
print(f"You have food to last you for: {days_to_last} days!")

for m in new_list:
    print(f"Item: {m[0]}, Best before: {m[1]}, Nutrition: {m[2]}")
