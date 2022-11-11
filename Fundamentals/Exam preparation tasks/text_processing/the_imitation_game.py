message = input()

command = input()

while command != "Decode":
    current_command = command.split("|")
    if current_command[0] == "Move":
        index = int(current_command[1])
        message = message[index:] + message[:index]
    elif current_command[0] == "Insert":
        index = int(current_command[1])
        value = current_command[2]
        message = message[:index] + value + message[index:]
    elif current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        message = message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {message}")