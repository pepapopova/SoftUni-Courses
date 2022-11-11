# to_do_list = ["o" for i in range(11)]
# command = input()
#
# while command != "End":
#     current_command = command.split("-")
#     priorrity = int(current_command[0])
#     note = current_command[1]
#     to_do_list[priorrity] = note
#     command = input()
#
# final_to_do = [num for num in to_do_list if num != "o"]
# print(final_to_do)

to_do_list = ["o"] * 11
command = input()

while command != "End":
    current_command = command.split("-")
    priority = int(current_command[0])
    note = current_command[1]
    to_do_list.pop(priority)
    to_do_list.insert(priority, note)
    command = input()

to_do_final = [num for num in to_do_list if num != "o"]
print(to_do_final)