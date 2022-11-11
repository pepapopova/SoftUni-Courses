def shopping_cart(*args):
    shop_cart = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }
    result = []
    for command in args:
        if command == "Stop":
            break
        product, material = command
        if product == "Soup" and len(shop_cart[product]) < 3:
            if material not in shop_cart[product]:
                shop_cart[product].append(material)
        elif product == "Dessert" and len(shop_cart[product]) < 2:
            if material not in shop_cart[product]:
                shop_cart[product].append(material)
        elif product == "Pizza" and len(shop_cart[product]) < 4:
            if material not in shop_cart[product]:
                shop_cart[product].append(material)

    for product, material in sorted(shop_cart.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{product}:")
        for mat in sorted(material):
            result.append(f" - {mat}")
    if shop_cart["Dessert"] or shop_cart["Soup"] or shop_cart["Pizza"]:
        return '\n'.join(result)
    else:
        return "No products in the cart!"


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
#
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
