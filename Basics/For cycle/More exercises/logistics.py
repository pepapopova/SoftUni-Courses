number_loads = int(input())
price_bus_per_ton = 200
price_truck_per_ton = 175
price_train_per_ton = 120
total_load = 0
bus_load = 0
truck_load = 0
train_load = 0

for load in range(number_loads):
    current_load = int(input())
    total_load +=current_load
    if current_load <= 3:
        bus_load += current_load
    elif current_load <= 11:
        truck_load += current_load
    else:
        train_load += current_load

average_price = (bus_load * price_bus_per_ton + truck_load * price_truck_per_ton + train_load * price_train_per_ton) / total_load
percent_bus = bus_load / total_load * 100
percent_truck = truck_load / total_load * 100
percent_train = train_load / total_load * 100

print(f"{average_price:.2f}")
print(f"{percent_bus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")