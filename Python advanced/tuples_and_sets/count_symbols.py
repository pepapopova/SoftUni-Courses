text = input()
dict = {}

for char in text:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

for key, value in sorted(dict.items()):
    print(f"{key}: {value} time/s")