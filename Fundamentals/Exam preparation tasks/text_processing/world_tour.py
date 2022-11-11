import re

stops = input()
# stops = input().replace('-', '::')
# stops = stops.split("::")
command = input().split(":")

while command[0] != "Travel":
    if command[0] == "Add Stop":
        index = int(command[1])
        stop = command[2]
        if -1 < index < len(stops):
            stops = stops[:index] + stop + stops[index:]
    elif command[0] == "Remove Stop":
        index1 = int(command[1])
        index2 = int(command[2])
        if -1 < index1 < len(stops) and -1 < index2 < len(stops):
            stops = stops[:index1] + stops[index2 + 1:]
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        stops = stops.replace(old_string, new_string)
    print(stops)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")