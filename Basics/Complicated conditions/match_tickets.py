budget = float(input())
category = input()
group = int(input())
transport = 0

if group <= 4:
    transport = budget * 0.75
elif 4 < group <= 9:
    transport = budget * 0.6
elif 9 < group <= 24:
    transport = budget * 0.5
elif 24 < group <= 49:
    transport = budget * 0.4
elif group > 49:
    transport = budget * 0.25

money_left = budget - transport
ticket_price = 0
if category == "VIP":
    ticket_price = 499.99
else:
    ticket_price = 249.99

difference = abs(money_left - (group * ticket_price))
if money_left - (group * ticket_price) >= 0:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
