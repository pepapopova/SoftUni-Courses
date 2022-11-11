students = int(input())
student_dict = {}

for student in range(students):
    name = input()
    grade = float(input())
    if name not in student_dict:
        student_dict[name] = []
    student_dict[name].append(grade)

for student in student_dict:
    student_dict[student] = sum(student_dict[student]) / len(student_dict[student])
    if student_dict[student] >= 4.5:
        print(f"{student} -> {student_dict[student]:.2f}")
