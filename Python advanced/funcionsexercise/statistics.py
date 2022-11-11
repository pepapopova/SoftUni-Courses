command = input()
my_dict = {}

while command != "statistics":
    current_product = command.split(": ")
    product = current_product[0]
    quantity = int(current_product[1])

    if product not in my_dict:
        my_dict[product] = quantity
    else:
        my_dict[product] += quantity

    command = input()

print("Products in stock:")
# using dic comprehension - [print(f" - {product}: {quantity}") for product,quantity in my_dict]
for product, quantity in my_dict.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")