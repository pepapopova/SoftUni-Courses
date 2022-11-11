student_name = input()
degree_count = 0
average_grade = 0
failed_degree = 0
graduates = True

while True:
    grade = float(input())
    degree_count += 1
    if grade >= 4:
        average_grade += grade
    else:
        failed_degree += 1
        if failed_degree > 1:
            degree_count -= 1
            graduates = False
            break
    if degree_count == 12:
        break
average_grade /= degree_count

if graduates:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {degree_count} grade")


