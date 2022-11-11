type_flowers = input()
number_flowers = int(input())
budget = int(input())
price = 0

if type_flowers == "Roses":
    price = 5
    if number_flowers > 80:
        price *= 0.9
elif type_flowers == "Dahlias":
    price = 3.8
    if number_flowers > 90:
        price *= 0.85
elif type_flowers == "Tulips":
    price = 2.8
    if number_flowers > 80:
        price *= 0.85
elif type_flowers == "Narcissus":
    price = 3
    if number_flowers < 120:
        price *= 1.15
else:
    price = 2.5
    if number_flowers < 80:
        price *= 1.2

total_price = number_flowers * price
difference = abs(total_price - budget)
if budget >= total_price:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {difference:.2f}"
          f" leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")