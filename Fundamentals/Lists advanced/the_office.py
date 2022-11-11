employee_happiness = list(map(int, input().split(" ")))
factor = int(input())

mapped_happiness = list(map(lambda x: x * factor, employee_happiness))

filtered = list(filter(lambda x: x >= (sum(mapped_happiness) / len(mapped_happiness)), mapped_happiness))

if len(filtered) >= len(mapped_happiness)/2:
    print(f"Score: {len(filtered)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employee_happiness)}. Employees are not happy!")

