command = input()
phonebook_dict = {}

while True:
    if command.isdigit():
        break
    phonebook = command.split("-")
    name = phonebook[0]
    phone = phonebook[1]
    phonebook_dict[name] = phone
    command = input()

number = int(command)
for n in range(number):
    search_name = input()
    if search_name in phonebook_dict:
            print(f"{search_name} -> {phonebook_dict[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")