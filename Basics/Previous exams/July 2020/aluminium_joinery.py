number_joinery = int(input())
type = input()
delivery_type = input()
order_is_valid = True

if type == "90X130":
    price = 110
    if 30 < number_joinery <= 60:
        price *= 0.95
    elif number_joinery > 60:
        price *= 0.92
elif type == "100X150":
    price = 140
    if 40 < number_joinery <= 80:
        price *= 0.94
    elif number_joinery > 80:
        price *= 0.90
elif type == "130X180":
    price = 190
    if 20 < number_joinery <= 50:
        price *= 0.93
    elif number_joinery > 50:
        price *= 0.88
elif type == "200X300":
    price = 250
    if 25 < number_joinery <= 50:
        price *= 0.91
    elif number_joinery > 50:
        price *= 0.86

price *= number_joinery

if delivery_type == "With delivery":
    price += 60

if number_joinery > 99:
    price *= 0.96
if number_joinery < 10:
    order_is_valid = False

if order_is_valid:
    print(f"{price:.2f} BGN")
else:
    print("Invalid order")



