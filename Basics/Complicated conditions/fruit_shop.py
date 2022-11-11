fruit = input()
day = input()
quantity = float(input())
price = 0
condition = True

if day in 'Monday Tuesday Wednesday Thursday Friday':
    if fruit == "banana":
        price = 2.5
    elif fruit == "apple":
        price = 1.2
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.7
    elif fruit == "pineapple":
        price = 5.5
    elif fruit == "grapes":
        price = 3.85
    else:
        condition = False

elif day in 'Saturday Sunday':
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.0
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        condition = False
else:
    condition = False

if condition:
    total_price = price * quantity
    print(f"{total_price:.2f}")
else:
    print("error")
