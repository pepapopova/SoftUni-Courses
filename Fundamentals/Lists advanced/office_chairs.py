number_rooms = int(input())
free_chairs = 0
condition = True

for room in range(1, number_rooms + 1):
    information = input().split(" ")
    chairs = int(len(information[0]))
    number_visitors = int(information[1])
    diff = abs(chairs - number_visitors)
    if chairs < number_visitors:
        print(f"{diff} more chairs needed in room {room}")
        condition = False
    else:
        free_chairs += diff

if condition:
    print(f"Game On, {free_chairs} free chairs left")


