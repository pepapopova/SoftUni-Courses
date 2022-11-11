number_wagons = int(input())
train = [0 for i in range(number_wagons)]
# train = [0] * number_wagons
command = input()

while command != "End":
    to_do = command.split(" ")
    command = to_do[0]
    if command == "add":
        num_passengers = int(to_do[1])
        train[-1] += num_passengers
    elif command == "insert":
        position = int(to_do[1])
        num_passengers = int(to_do[2])
        train[position] += num_passengers
    elif command == "leave":
        position = int(to_do[1])
        num_passengers = int(to_do[2])
        train[position] -= num_passengers

    command = input()
#
print(train)