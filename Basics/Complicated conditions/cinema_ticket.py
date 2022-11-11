day = input()
price = 0
if day in 'Monday Tuesday Friday':
    price = 12
elif day in 'Wednesday Thursday':
    price = 14
elif day == "Saturday" or day == "Sunday":
    price = 16

print(price)
