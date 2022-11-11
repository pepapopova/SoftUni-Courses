month = input()
nights = int(input())
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if 7 < nights <= 14:
        price_studio *= 0.95
    elif nights > 14:
        price_studio *= 0.7
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if nights > 14:
        price_studio *= 0.8
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77

if nights > 14:
    price_apartment *= 0.9

price_ap_whole_stay = price_apartment * nights
price_studio_whole_stay = price_studio * nights

print(f"Apartment: {price_ap_whole_stay:.2f} lv.")
print(f"Studio: {price_studio_whole_stay:.2f} lv.")
