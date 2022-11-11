items_list = input().split(" ")
my_dict = {}

# for item, number in zip(items_list[0::2], items_list[1::2]):
#     my_dict[item] = int(number)


for i in range(0, len(items_list), 2):
    key = items_list[i]
    value = items_list[i + 1]
    my_dict[key] = int(value)

print(my_dict)

