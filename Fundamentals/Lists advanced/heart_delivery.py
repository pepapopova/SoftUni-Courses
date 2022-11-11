def cupid_walk(data):
    command = input()
    position = 0
    while command != "Love!":
        current_command = command.split(" ")
        jump_lenght = int(current_command[1])
        position += jump_lenght
        if position >= len(data):
            position = 0
        if data[position] <= 0:
            print(f"Place {position} already had Valentine's day.")
            data[position] = 0
        else:
            data[position] -= 2
            if data[position] <= 0:
                print(f"Place {position} has Valentine's day.")
        command = input()
    print(f"Cupid's last position was {position}.")
    failed_places = len(list(filter(lambda x: x != 0, data)))
    if failed_places > 0:
        print(f"Cupid has failed {failed_places} places.")
    else:
        print("Mission was successful.")



neighbourhood = list(map(int, input().split("@")))
cupid_walk(neighbourhood)