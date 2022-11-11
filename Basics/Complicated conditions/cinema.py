type_movie = input()
rows = int(input())
columns = int(input())
price = 0

if type_movie == "Premiere":
    price = 12
elif type_movie == "Normal":
    price = 7.5
else:
    price = 5

total_seats = rows * columns
total_revenue = total_seats * price
print(f'{total_revenue:.2f} leva')