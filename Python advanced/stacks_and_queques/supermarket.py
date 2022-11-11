from collections import deque

customers = deque()

while True:
    current_customer = input()
    if current_customer == "End":
        print(f"{len(customers)} people remaining.")
        break
    elif current_customer == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(current_customer)
