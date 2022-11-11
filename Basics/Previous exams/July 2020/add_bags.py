#90/100 - there is so mistake - only correct outputs here
price_luggage_over_20 = float(input())
luggage_weight = float(input())
days_to_flight = int(input())
number_luggage = int(input())

if luggage_weight < 10:
    fee = 0.2 * price_luggage_over_20
    if days_to_flight < 7:
        fee *= 1.4
    elif 7 <= days_to_flight <= 30:
        fee *= 1.15
    else:
        fee *= 1.1
elif luggage_weight <= 20:
    fee = 0.5 * price_luggage_over_20
    if days_to_flight < 7:
        fee *= 1.4
    elif 7 <= days_to_flight <= 30:
        fee *= 1.15
    else:
        fee *= 1.1
elif luggage_weight > 20:
    fee = price_luggage_over_20
    if days_to_flight < 7:
        fee *= 1.4
    elif 7 <= days_to_flight <= 30:
        fee *= 1.15
    else:
        fee *= 1.1

total_price = number_luggage * fee
print(f"The total price of bags is: {total_price:.2f} lv.")

