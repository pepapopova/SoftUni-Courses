fruit = input()
size_set = input()
number_set = int(input())
price = 0

if fruit == "Watermelon" and size_set == "small":
    price = 56 * number_set * 2
elif fruit == "Watermelon" and size_set == "big":
    price = 28.70 * number_set * 5
elif fruit == "Mango" and size_set == "small":
    price = 36.66 * number_set * 2
elif fruit == "Mango" and size_set == "big":
    price = 19.60 * number_set * 5
elif fruit == "Pineapple" and size_set == "small":
    price = 42.10 * number_set * 2
elif fruit == "Pineapple" and size_set == "big":
    price = 24.80 * number_set * 5
elif fruit == "Raspberry" and size_set == "small":
    price = 20 * number_set * 2
elif fruit == "Raspberry" and size_set == "big":
    price = 15.20 * number_set * 5

if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.50

print(f"{price:.2f} lv.")