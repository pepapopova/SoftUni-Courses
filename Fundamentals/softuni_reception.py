employees = 3
efficiency_emp1 = int(input())
efficiency_emp2 = int(input())
efficiency_emp3 = int(input())
waiting_students = int(input())
total_efficiency = efficiency_emp1 + efficiency_emp2 + efficiency_emp3
hour = 1


while True:
    if waiting_students == 0:
        print(f"Time needed: 0h.")
        break
    if hour % 4 != 0:
        waiting_students -= total_efficiency
    if waiting_students <= 0:
        print(f"Time needed: {hour}h.")
        break
    hour += 1