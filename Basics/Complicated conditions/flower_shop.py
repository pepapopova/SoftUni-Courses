number_hrisantems = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
holiday = input()
price_bouquet = 0

if season == "Spring" or season == "Summer":
    price_bouquet = number_hrisantems * 2 + number_roses * 4.1 + number_tulips * 2.5
elif season == "Autumn" or season == "Winter":
    price_bouquet = number_hrisantems * 3.75 + number_roses * 4.5 + number_tulips * 4.15

if holiday == "Y":
    price_bouquet *= 1.15
    if number_tulips > 7 and season == "Spring":
        price_bouquet *= 0.95
    if number_roses > 10 and season == "Winter":
        price_bouquet *= 0.9
    if number_tulips + number_roses + number_hrisantems > 20:
        price_bouquet *= 0.8
else:
    if number_tulips > 7 and season == "Spring":
        price_bouquet *= 0.95
    if number_roses > 10 and season == "Winter":
        price_bouquet *= 0.9
    if number_tulips + number_roses + number_hrisantems > 20:
        price_bouquet *= 0.8

price_bouquet +=2
print(f"{price_bouquet:.2f}")

