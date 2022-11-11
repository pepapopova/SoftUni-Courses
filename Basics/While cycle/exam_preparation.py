max_fails = int(input())
count_tasks = 0
bad_grades = 0
task_name = input()
failed = False
average_grade = 0

while task_name != "Enough":
    result = int(input())
    if result <= 4:
        bad_grades += 1
        if bad_grades == max_fails:
            failed = True
            break
    count_tasks += 1
    average_grade += result
    last_problem = task_name
    task_name = input()

average_grade /= count_tasks
if failed:
    print(f"You need a break, {max_fails} poor grades.")
else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_tasks}")
    print(f"Last problem: {last_problem}")