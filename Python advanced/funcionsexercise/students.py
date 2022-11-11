text = input()
courses = {}

while ":" in text:
    data = text.split(":")
    name = data[0]
    id = data[1]
    course = data[2]
    # name, id, course = data[0], data[1], data[2]
    if course not in courses:
        courses[course] = {}
    courses[course][id] = name

    text = input()

text = text.replace("_", " ")
# course = " ".join(text.split("_")

for id in courses[text]:
    print(f"{courses[text][id]} - {id}")

# for key, value in courses.items():
#     if key == course:
#         for id, name in value.items():
#             print(f"{name} - {id}")