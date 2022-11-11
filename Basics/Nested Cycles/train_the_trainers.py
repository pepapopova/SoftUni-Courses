average_grade = 0
total_grade = 0
jury_number = int(input())
command = input()
counter_diff_presentations = 0
while command != "Finish":
    presentation = command
    for person in range(jury_number):
        current_grade = float(input())
        average_grade += current_grade
        total_grade += current_grade
    average_grade /= jury_number
    print(f"{presentation} - {average_grade:.2f}.")
    average_grade = 0
    counter_diff_presentations += 1
    command = input()
total_grade /= counter_diff_presentations * jury_number
print(f"Student's final assessment is {total_grade:.2f}.")