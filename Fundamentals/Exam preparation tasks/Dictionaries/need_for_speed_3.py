number_of_cars = int(input())
cars_dict = {}
for n in range(number_of_cars):
    current_car = input().split("|")
    car = current_car[0]
    mileage = int(current_car[1])
    fuel = int(current_car[2])
    cars_dict[car] = {}
    cars_dict[car]['Mileage'] = mileage
    cars_dict[car]['Fuel'] = fuel

command = input()

while command != "Stop":
    current_command = command.split(" : ")
    chosen_car = current_command[1]

    if current_command[0] == "Drive":
        distance = int(current_command[2])
        fuel_needed = int(current_command[3])
        if cars_dict[chosen_car]['Fuel'] < fuel_needed:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[chosen_car]['Mileage'] += distance
            cars_dict[chosen_car]['Fuel'] -= fuel_needed
            print(f"{chosen_car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        if cars_dict[chosen_car]['Mileage'] > 100000:
            del cars_dict[chosen_car]
            print(f"Time to sell the {chosen_car}!")
    elif current_command[0] == "Refuel":
        refill_fuel = int(current_command[2])
        if cars_dict[chosen_car]['Fuel'] + refill_fuel > 75:
            refill_fuel = 75 - cars_dict[chosen_car]['Fuel']
            cars_dict[chosen_car]['Fuel'] = 75
        else:
            cars_dict[chosen_car]['Fuel'] += refill_fuel
        print(f"{chosen_car} refueled with {refill_fuel} liters")
    elif current_command[0] == "Revert":
        decrease_value = int(current_command[2])
        cars_dict[chosen_car]['Mileage'] -= decrease_value
        if cars_dict[chosen_car]['Mileage'] < 10000:
            cars_dict[chosen_car]['Mileage'] = 10000
        else:
            print(f"{chosen_car} mileage decreased by {decrease_value} kilometers")
    command = input()

for car in cars_dict:
    print(f"{car} -> Mileage: {cars_dict[car]['Mileage']} kms, Fuel in the tank: {cars_dict[car]['Fuel']} lt.")