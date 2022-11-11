import sys

command = input()
max_number = - sys.maxsize

while command != "Stop":
    if int(command) > max_number:
        max_number = int(command)
    command = input()

print(max_number)
