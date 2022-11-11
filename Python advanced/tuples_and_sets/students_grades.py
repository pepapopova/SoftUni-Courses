number_students = int(input())
student_book = {}

for student in range(number_students):
    data = input().split()
    name = data[0]
    grade = float(data[1])
    if name not in student_book:
        student_book[name] = []
        student_book[name].append(grade)
    else:
        student_book[name].append(grade)

for student, grade in student_book.items():
    average_grade = sum(student_book[student])/len(student_book[student])
    string_grades = ' '.join(f"{x:.2f}" for x in grade)
    print(f"{student} -> {string_grades} (avg: {average_grade:.2f})")