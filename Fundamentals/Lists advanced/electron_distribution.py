number_electrons = int(input())
filled_shell = []
position = 1
left_electrons = number_electrons

while True:

    shell_value = 2 * position ** 2
    if shell_value < left_electrons:
        filled_shell.append(shell_value)
        position += 1
        left_electrons -= shell_value
    else:
        filled_shell.append(left_electrons)
        break


print(filled_shell)