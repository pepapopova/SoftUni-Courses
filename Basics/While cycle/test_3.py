failed_trshold = int(input())
failed_times = 0
solved_problems_count = 0
grades_sum = 0
last_problem = ""
has_failed = True

while failed_times < failed_trshold:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problems_count += 1
    last_problem = problem_name

if has_failed:
    print(f"You need a break, {failed_trshold} poor grades.")
else:
    average_grade = grades_sum / solved_problems_count
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")