from string import ascii_lowercase
data = input().split()
current_sum = 0
total_sum = 0
digit = ''

for string in data:
    current_sum = 0
    digit = ''
    for char in string:
        if char.isdigit():
            digit += char
    if string[0].isupper():
        index = ascii_lowercase.index(string[0].lower()) + 1
        current_sum += int(digit) / index
    elif string[0].islower():
        index = ascii_lowercase.index(string[0]) + 1
        current_sum += int(digit) * index
    if string[-1].isupper():
        index = ascii_lowercase.index(string[-1].lower()) + 1
        current_sum -= index
    elif string[-1].islower():
        index = ascii_lowercase.index(string[-1]) + 1
        current_sum += index
    total_sum += current_sum
print(f"{total_sum:.2f}")