width = int(input())
length = int(input())
height = int(input())
room_size = width * length * height
command = input()
room_is_enough = True

while command != "Done":
    new_box = int(command)
    room_size -= new_box
    if room_size < 0:
        room_is_enough = False
        break
    command = input()

if room_is_enough:
    print(f"{room_size} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(room_size)} Cubic meters more.")