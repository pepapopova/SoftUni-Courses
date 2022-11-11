destination = input()
current_sum = 0
saved_sum = 0

while destination != "End":
    min_budget = float(input())
    while saved_sum < min_budget:
        current_sum = float(input())
        saved_sum += current_sum
    print(f"Going to {destination}!")
    saved_sum = 0
    destination = input()