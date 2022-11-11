command = input()
my_dict = {}
while command != "Lumpawaroo":
    if "|" in command:
        current_command = command.split(" | ")
        force_side = current_command[0]
        force_user = current_command[1]
        if force_user not in [x for v in my_dict.values() for x in v]:
            if force_side not in my_dict:
                my_dict[force_side] = []
            my_dict[force_side].append(force_user)
    elif "->" in command:
        current_command = command.split(" -> ")
        force_side = current_command[1]
        force_user = current_command[0]
        if force_user in [x for v in my_dict.values() for x in v]:
            for current_side in my_dict:
                if force_user in my_dict[current_side]:
                    if len(my_dict[current_side]) > 1:
                        my_dict[current_side].pop(force_user)
                        break
                    else:
                        del my_dict[current_side]
                        break
            if force_side not in my_dict:
                my_dict[force_side] = []
            my_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        else:
            if force_side not in my_dict:
                my_dict[force_side] = [force_user]
            else:
                my_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    command = input()

for side, user in my_dict.items():
    if len(my_dict[side]) > 0:
        print(f"Side: {side}, Members: {len(my_dict[force_side])}")
        for u in my_dict[side]:
            print(f"! {''.join(u)}")


