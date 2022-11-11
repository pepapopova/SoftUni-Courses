import re

n = int(input())
numbers_list = []

for command in range(n):
    current_command = input()
    matches0 = re.match(r'^!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]$', current_command)
    if not matches0:
        print("The message is invalid")
    matches = re.finditer(r'^!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]$', current_command)
    for match in matches:
        message = match.group(2)
        for char in message:
            numbers_list.append(str(ord(char)))
        print(f"{match.group(1)}: {' '.join(numbers_list)}")
