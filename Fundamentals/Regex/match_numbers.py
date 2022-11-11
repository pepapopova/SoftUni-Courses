import re

names = input()
matches = re.finditer(r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))', names)
# for match in matches:[
#     print(match.group(), end=" ")

output = []
for match in matches:
    output.append(match.group())
print(" ".join(output))