season = input()
group_type = input()
number_students = int(input())
nights = int(input())

price_per_night = 0
sport = ""

if season == "Winter":
    if group_type == "girls":
        price_per_night = 9.6
        sport = "Gymnastics"
    elif group_type == "boys":
        price_per_night = 9.6
        sport = "Judo"
    else:
        price_per_night = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "girls":
        price_per_night = 7.20
        sport = "Athletics"
    elif group_type == "boys":
        price_per_night = 7.2
        sport = "Tennis"
    else:
        price_per_night = 9.5
        sport = "Cycling"
else:
    if group_type == "girls":
        price_per_night = 15
        sport = "Volleyball"
    elif group_type == "boys":
        price_per_night = 15
        sport = "Football"
    else:
        price_per_night = 20
        sport = "Swimming"

if number_students >= 50:
    price_per_night *= 0.5
elif 50 > number_students >= 20:
    price_per_night *= 0.85
elif 20 > number_students >= 10:
    price_per_night *= 0.95

total_price = price_per_night * nights * number_students
print(f"{sport} {total_price:.2f} lv.")