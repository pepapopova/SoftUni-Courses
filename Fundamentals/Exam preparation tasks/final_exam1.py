string = input()

command = input()

while command != "End":
    current_command = command.split(" ")
    if current_command[0] == "Translate":
        char = current_command[1]
        replacement = current_command[2]
        string = string.replace(char, replacement)
        print(string)
    elif current_command[0] == "Includes":
        substring = current_command[1]
        if substring in string:
            print('True')
        else:
            print('False')
    elif current_command[0] == "Start":
        start_substring = current_command[1]
        if start_substring == string[:len(start_substring)]:
            print('True')
        else:
            print('False')
    if current_command[0] == "Lowercase":
        string = string.lower()
        print(string)
    elif current_command[0] == "FindIndex":
        char1 = current_command[1]
        list_chars = [index for index, char in enumerate(string) if char == char1]
        print(list_chars[-1])
    elif current_command[0] == "Remove":
        start_index = int(current_command[1])
        count = int(current_command[2])
        print_string = string[start_index:start_index+count]
        print(string.replace(print_string, ""))
    command = input()

