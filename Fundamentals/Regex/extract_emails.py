import re

string = input()
matches = re.finditer(r'( |^)[a-zA-Z0-9]+([\.\-_][a-zA-Z0-9]+)*@[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+', string)
for match in matches:
    print(match.group(), end="\n")