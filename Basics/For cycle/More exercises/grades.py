number_students = int(input())
top_students = 0
good_students = 0
medium_students = 0
weak_students = 0
total_rate = 0

for n in range(number_students):
    rate = float(input())
    if 2 <= rate <= 2.99:
        weak_students += 1
        total_rate += rate
    elif 3 <= rate <= 3.99:
        medium_students += 1
        total_rate += rate
    elif 4 <= rate <= 4.99:
        good_students += 1
        total_rate += rate
    elif rate >= 5:
        top_students += 1
        total_rate += rate

percent_top = top_students / number_students * 100
percent_good = good_students / number_students * 100
percent_medium = medium_students / number_students * 100
percent_weak = weak_students / number_students * 100
average_grade = total_rate / number_students

print(f"Top students: {percent_top:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_medium:.2f}%")
print(f"Fail: {percent_weak:.2f}%")
print(f"Average: {average_grade:.2f}")


