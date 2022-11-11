name = input()
year_grade = 0
counter = 0
fail_counter = 0
while counter <= 11:
    grades = float(input())
    if grades < 4:
        fail_counter += 1

    if fail_counter < 2:
        year_grade += grades
        counter += 1
    else:
        break

if fail_counter < 2:
    year_grade = year_grade / counter
    print(f'{name} graduated. Average grade: {year_grade:.2f}')
else:
    print(f'{name} has been excluded at {counter} grade')
