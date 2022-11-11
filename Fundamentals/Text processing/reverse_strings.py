command = input()


while command != "end":
    # reverse_text = ""
    # for char in reversed(command): -решение 1
    #     reverse_text += char

    # reverse_text = "".join(reversed(command))
    # print(f"{command} = {reverse_text}") -решение 2
    reversed_command = command[::-1]
    print(f"{command} = {reversed_command}")
    command = input()


