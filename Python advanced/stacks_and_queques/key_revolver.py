from collections import deque

bullet_price = int(input())
size_barrel = int(input())

bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
bullets_cost = 0
game_over = False

while bullets and locks:
    for shoot in range(size_barrel):
        if not bullets or not locks:
            game_over = True
            break
        current_bullet = bullets.pop()
        current_lock = locks.popleft()
        if current_bullet <= current_lock:
            print("Bang!")
        else:
            print("Ping!")
            locks.appendleft(current_lock)
        bullets_cost += bullet_price
    else:
        print("Reloading!")
    if game_over:
        break

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - bullets_cost}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
