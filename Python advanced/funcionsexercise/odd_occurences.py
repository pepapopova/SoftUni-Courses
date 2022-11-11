sequence = input().split(" ")
my_dict = {}

for word in sequence:
    if word.lower() not in my_dict:
        my_dict[word.lower()] = 1
    else:
        my_dict[word.lower()] += 1

for word in my_dict:
    if my_dict[word] % 2 != 0:
        print(word, end= " ")

# for key, value in my_dict.items():
#     if value % 2 != 0:
#         print(word, end = "")
