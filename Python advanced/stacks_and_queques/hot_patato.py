from collections import deque

names = input().split()
tosses = int(input())
kids = deque(names)

current_count = 0
while len(kids) > 1:
    current_count += 1
    kid = kids.popleft()
    if current_count < tosses:
        kids.append(kid)
    else:
        print(f"Removed {kid}")
        current_count = 0

print(f"Last is {''.join(kids)}")