char_list = input().split(", ")
my_dict = {char: ord(char) for char in char_list}

print(my_dict)