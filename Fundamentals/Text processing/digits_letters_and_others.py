string = input()
digits = ""
chars = ""
all_others = ""

for char in string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        chars += char
    else:
        all_others += char

print(digits)
print(chars)
print(all_others)
