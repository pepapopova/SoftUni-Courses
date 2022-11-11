concealed_message = input()

command = input()

while command != "Reveal":
    current_command = command.split(":|:")
    if current_command[0] == "InsertSpace":
        index = int(current_command[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif current_command[0] == "Reverse":
        substring = current_command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message = concealed_message + substring[::-1]
            print(concealed_message)
        else:
            print("error")
    if current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")