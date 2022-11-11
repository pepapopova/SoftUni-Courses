movie_name = input()
type_hall = input()
tickets_sold = int(input())
price = 0

if movie_name == "A Star Is Born":
    if type_hall == "normal":
        price = 7.5
    elif type_hall == "luxury":
        price = 10.5
    else:
        price = 13.5
elif movie_name == "Bohemian Rhapsody":
    if type_hall == "normal":
        price = 7.35
    elif type_hall == "luxury":
        price = 9.45
    else:
        price = 12.75
elif movie_name == "Green Book":
    if type_hall == "normal":
        price = 8.15
    elif type_hall == "luxury":
        price = 10.25
    else:
        price = 13.25
else:
    if type_hall == "normal":
        price = 8.75
    elif type_hall == "luxury":
        price = 11.55
    else:
        price = 13.95

price *= tickets_sold

print(f"{movie_name} -> {price:.2f} lv.")