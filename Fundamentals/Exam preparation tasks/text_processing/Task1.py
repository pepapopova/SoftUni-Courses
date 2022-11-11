string = input()

command = input()

while command != "Done":
    current_command = command.split(" ")
    if current_command[0] == "TakeOdd":
        string = string[1::2]
        print(string)
    elif current_command[0] == "Cut":
        index = int(current_command[1])
        length = int(current_command[2])
        to_be_removed = string[index:index+length]
        string = string.replace(to_be_removed, "", 1)
        print(string)
    elif current_command[0] == "Substitute":
        substring = current_command[1]
        substitute = current_command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {string}")