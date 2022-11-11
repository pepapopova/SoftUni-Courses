command = input()
products_dict = {}

while command != "buy":
    current_command = command.split(" ")
    product = current_command[0]
    price = float(current_command[1])
    quantity = int(current_command[2])

    if product not in products_dict:
        products_dict[product] = {}
        products_dict[product]['price'] = price
        products_dict[product]['quantity'] = quantity
    else:
        products_dict[product]['price'] = price
        products_dict[product]['quantity'] += quantity

    command = input()


for item in products_dict:
    total_sum = products_dict[item]['quantity'] * products_dict[item]['price']
    print(f"{item} -> {total_sum:.2f}")