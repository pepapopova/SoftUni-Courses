import re

string = input()
matches = re.findall(r'\b_[A-Za-z0-9]+\b', string)
digits_list = []
for match in matches:
    digits_list.append(match[1:])

print(",".join(digits_list))
