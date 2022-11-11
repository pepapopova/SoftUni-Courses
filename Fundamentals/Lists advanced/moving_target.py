data = list(map(int, input().split(" ")))
command = input()

while command != "End":
    current_command = command.split(" ")
    action = current_command[0]
    if action == "Shoot":
        index = int(current_command[1])
        if len(data) > index >= 0:
            data[index] -= int(current_command[2])
            if data[index] <= 0:
                data.pop(index)
    elif action == "Add":
        index = int(current_command[1])
        if len(data) > index >= 0:
            data.insert(index, current_command[2])
        else:
            print("Invalid placement!")
    elif action == "Strike":
        index = int(current_command[1])
        radius = int(current_command[2])
        if index - radius >= 0 and index + radius < len(data):
            data = data[0:(index - radius)] + data[(index + radius + 1)::]
        else:
            print("Strike missed!")

    command = input()

data_as_string = list(map(str, data))
print("|".join(data_as_string))