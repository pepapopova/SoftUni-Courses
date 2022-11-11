items_list = input().split(" ")
search_items = input().split(" ")
my_dict = {}

for item, quantity in zip(items_list[0::2], items_list[1::2]):
    my_dict[item] = int(quantity)

for item in search_items:
    if item in my_dict:
        print(f"We have {my_dict[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")

