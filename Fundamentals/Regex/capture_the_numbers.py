import re
numbers = []
text = input()
while True:
    if not text:
        break
    matches = re.findall(r'\d+', text)
    for match in matches:
        numbers.append(match)
    text = input()

print(" ".join(numbers))