string = input()
my_dict = {}

for char in string:
    if char != " ":
        if char not in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1

for char, occurences in my_dict.items():
    print(f"{char} -> {occurences}")

