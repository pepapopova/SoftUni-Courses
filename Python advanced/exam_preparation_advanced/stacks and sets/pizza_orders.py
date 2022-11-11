from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = deque([int(x) for x in input().split(", ")])
completed_pizzas = 0

while pizza_orders and employees:
    current_order = pizza_orders.popleft()
    if current_order > 10:
        continue
    if current_order <= 0:
        continue
    current_employee = employees.pop()
    if current_order <= current_employee:
        completed_pizzas += current_order
    else:
        completed_pizzas += current_employee
        current_order -= current_employee
        while current_order and employees:
            current_employee = employees.pop()
            if current_order <= current_employee:
                completed_pizzas += current_order
                break
            current_order -= current_employee
        if not employees:
            pizza_orders.appendleft(current_order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {completed_pizzas}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")

if not employees and pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")