town = input()
packet_type = input()
vip_discount = input()
days = int(input())
everything_is_correct = True

if town == "Bansko" or town == "Borovets":
    if packet_type == "withEquipment":
        price = 100
        if vip_discount == "yes":
            price *= 0.9
    elif packet_type == "noEquipment":
        price = 80
        if vip_discount == "yes":
            price *= 0.95
    else:
        everything_is_correct = False
elif town == "Varna" or town == "Burgas":
    if packet_type == "withBreakfast":
        price = 130
        if vip_discount == "yes":
            price *= 0.88
    elif packet_type == "noBreakfast":
        price = 100
        if vip_discount == "yes":
            price *= 0.93
    else:
        everything_is_correct = False
else:
    everything_is_correct = False



if days < 1:
    print("Days must be positive number!")
else:
    if everything_is_correct:
        if days > 7:
            days -= 1
        total_price = price * days
        print(f"The price is {total_price:.2f}lv! Have a nice time!")

    else:
        print("Invalid input!")