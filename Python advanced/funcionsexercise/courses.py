command = input()
courses_dict = {}

while command != "end":
    current_course = command.split(" : ")
    course = current_course[0]
    name = current_course[1]

    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(name)
    command = input()

for course, student in courses_dict.items():
    print(f"{course}: {len(courses_dict[course])}")
    for name in courses_dict[course]:
        print(f" -- {name}")