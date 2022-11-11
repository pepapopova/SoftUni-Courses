command = input()
my_dict = {}

while command != "stop":
    resource = command
    quantity = int(input())
    if resource not in my_dict:
        my_dict[resource] = quantity
    else:
        my_dict[resource] += quantity
    command = input()

for resource, quantity in my_dict.items():
    print(f"{resource} -> {quantity}")