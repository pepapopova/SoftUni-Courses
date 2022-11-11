number_students = int(input())
count_weak = 0
count_good = 0
count_very_good = 0
count_excellent = 0
total_grade = 0

for student in range(number_students):
    exam_grade = float(input())
    total_grade += exam_grade
    if exam_grade < 3:
        count_weak += 1
    elif 3 <= exam_grade <= 3.99:
        count_good += 1
    elif 4 <= exam_grade <= 4.99:
        count_very_good += 1
    elif exam_grade >= 5:
        count_excellent += 1


excellent_students_percent = count_excellent / number_students * 100
very_good_students_percent = count_very_good / number_students * 100
good_students_percent = count_good / number_students * 100
weak_students_percent = count_weak / number_students * 100
print(f"Top students: {excellent_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {very_good_students_percent:.2f}%")
print(f"Between 3.00 and 3.99: {good_students_percent:.2f}%")
print(f"Fail: {weak_students_percent:.2f}%")
average = total_grade / number_students
print(f"Average: {average:.2f}")

