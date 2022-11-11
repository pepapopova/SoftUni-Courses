sequence = input().split(" ")
n = len(sequence)
new_string = ""

for string in sequence:
    n = len(string)
    new_string += string * n

print(new_string)
