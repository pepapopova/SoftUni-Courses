country = input()
type = input()
grade_hardness = 0
grade_execution = 0

if type == "ribbon":
    if country == "Russia":
        grade_hardness = 9.1
        grade_execution = 9.4
    elif country == "Bulgaria":
        grade_hardness = 9.6
        grade_execution = 9.4
    else:
        grade_hardness = 9.2
        grade_execution = 9.5
elif type == "hoop":
    if country == "Russia":
        grade_hardness = 9.3
        grade_execution = 9.8
    elif country == "Bulgaria":
        grade_hardness = 9.55
        grade_execution = 9.75
    else:
        grade_hardness = 9.45
        grade_execution = 9.35
elif type == "rope":
    if country == "Russia":
        grade_hardness = 9.6
        grade_execution = 9.0
    elif country == "Bulgaria":
        grade_hardness = 9.5
        grade_execution = 9.4
    else:
        grade_hardness = 9.7
        grade_execution = 9.15

total_grade = grade_hardness + grade_execution
percent_not_enough = 100 - (total_grade / 20 * 100)
print(f"The team of {country} get {total_grade:.3f} on {type}.")
print(f"{percent_not_enough:.2f}%")
