days_stay = int(input())
type_room = input()
feedback = input()
room_for_one_person = 18
apartment = 25
president_apartment = 35
night = days_stay - 1
price = 0

if type_room == "apartment":
    if night < 10:
        price = apartment * 0.7
    elif 10 <= night <= 15:
        price = apartment * 0.65
    elif night > 15:
        price = apartment * 0.5
elif type_room == "president apartment":
    if days_stay < 10:
        price = president_apartment * 0.9
    elif 10 <= days_stay <= 15:
        price = president_apartment * 0.85
    elif days_stay > 15:
        price = president_apartment * 0.8
else:
    price = room_for_one_person

if feedback == "positive":
    price *= 1.25
elif feedback == "negative":
    price *= 0.9
total_price = price * night
print(f"{total_price:.2f}")