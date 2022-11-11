command = input()
names_dict = {}
language_dict = {}

while command != "exam finished":
    result = command.split("-")
    username = result[0]
    language = result[1]
    if language == "banned":
        names_dict.pop(username)
    elif username not in names_dict:
        names_dict[username] = {}
        names_dict[username][language] = int(result[2])
    elif language not in names_dict[username][language]:
        names_dict[username][language] = int(result[2])
    else:
        if names_dict[username][language] < int(result[2]):
            names_dict[username][language] = int(result[2])
    if language not in language_dict:
        language_dict[language] = 1
    else:
        language_dict[language] += 1

    command = input()

print("Results:")
for name, score in names_dict.items():
    print(f"{name} | {score}")

print("Submissions:")
for language, count in language_dict.items():
    print(f"{language} - {count}")