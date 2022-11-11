command1 = input()
command2 = input()

for i in range(len(command1)):
    if command1[i] != command2[i]:
        replacement = command2[i]
        word = command1[:i] + replacement + command1[i + 1:]
        command1 = word
        print(command1)