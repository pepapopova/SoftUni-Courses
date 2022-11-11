from collections import deque

def best_list_pureness(list, rotations):
    list = deque(list)
    highest_pureness = 0
    rotation = 0
    for index in range(len(list)):
        highest_pureness += (index * list[index])
    for num in range(1, int(rotations) + 1):
        list.appendleft(list.pop())
        new_pureness = 0
        for index in range(len(list)):
            new_pureness += (index * list[index])
        if new_pureness > highest_pureness:
            highest_pureness = new_pureness
            rotation = num
    return f"Best pureness {highest_pureness} after {rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

