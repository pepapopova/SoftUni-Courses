command = input()
new_word = ""

for i in range(len(command)):
    new_word = new_word + command[i] + command[i]

print(new_word)