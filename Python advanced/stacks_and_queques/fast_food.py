from collections import deque

food_quantity = int(input())
food_orders = [int(x) for x in input().split()]

food_queue = deque(food_orders)

print(max(food_queue))
all_served = True

while food_queue:
    current_order = food_queue.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        food_queue.appendleft(current_order)
        all_served = False
        break

if all_served:
    print("Orders complete")
else:
    string_queue = [str(x) for x in food_queue]
    print(f'Orders left: {" ".join(string_queue)}')