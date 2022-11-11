from collections import deque

petrol_pumps = int(input())
pumps = deque()



for _ in range(petrol_pumps):
    pumps.append([int(x) for x in input().split()])

for attempt in range(petrol_pumps):
    total_petrol = 0
    failed = False
    for petrol, distance in pumps:
        total_petrol = total_petrol + petrol - distance
        if total_petrol < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
