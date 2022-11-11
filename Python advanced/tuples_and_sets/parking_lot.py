number_of_commands = int(input())
parked_cars = set()

for _ in range(number_of_commands):
    direction, car_number = input().split(", ")
    if direction == "IN":
        parked_cars.add(car_number)
    else:
        parked_cars.remove(car_number)

if len(parked_cars):
    # for num in parked_cars:
    #     print(num)
    [print(car_number) for car_number in parked_cars]
else:
    print("Parking Lot is Empty")