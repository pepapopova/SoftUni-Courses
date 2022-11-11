number_plays = int(input())
result = 0
invalid_numbers = 0
number_lower_10 = 0
number_lower_20 = 0
number_lower_30 = 0
number_lower_40 = 0
number_40_50 = 0

for n in range(number_plays):
    number = int(input())
    if number < 0 or number > 50:
        result /= 2
        invalid_numbers += 1
    elif number < 10:
        result += 0.2 * number
        number_lower_10 += 1
    elif number < 20:
        result += 0.3 * number
        number_lower_20 += 1
    elif number < 30:
        result += 0.4 * number
        number_lower_30 += 1
    elif number < 40:
        result += 50
        number_lower_40 += 1
    elif number <= 50:
        result += 100
        number_40_50 += 1

percent_invalid = invalid_numbers / number_plays * 100
percent_lower_10 = number_lower_10 / number_plays * 100
percent_lower_20 = number_lower_20 / number_plays * 100
percent_lower_30 = number_lower_30 / number_plays * 100
percent_lower_40 = number_lower_40 / number_plays * 100
percent_40_to_50 = number_40_50 / number_plays * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {percent_lower_10:.2f}%")
print(f"From 10 to 19: {percent_lower_20:.2f}%")
print(f"From 20 to 29: {percent_lower_30:.2f}%")
print(f"From 30 to 39: {percent_lower_40:.2f}%")
print(f"From 40 to 50: {percent_40_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")