import re

text = input()
links_list = []

while True:
    if not text:
        break
    matches = re.finditer(r'w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+', text)
    for match in matches:
        links_list.append(match.group())
    text = input()

print("\n".join(links_list))