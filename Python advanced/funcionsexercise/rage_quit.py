rage_message = input()
new_message = ''
multiplier = ''
unique_values = ''
current_message = ''
index = -1

for char in rage_message:
    index += 1
    if not char.isdigit():
        if len(multiplier) > 0:
            current_message *= int(multiplier)
            new_message += current_message
            current_message = char.upper()
            multiplier = ''
        else:
            current_message += char.upper()
    elif char.isdigit():
        if len(rage_message) - 1 == index:
            multiplier += char
            current_message *= int(multiplier)
            new_message += current_message
            current_message = ''
        else:
            multiplier += char

for char in new_message:
    if char not in unique_values:
        unique_values += char

print(f"Unique symbols used: {len(unique_values)}")
print(new_message)