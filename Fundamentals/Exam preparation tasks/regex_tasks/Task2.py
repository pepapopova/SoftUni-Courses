import re

string = input()
valid_words = []
matches_list = []
count = 0

matches = re.finditer(r'(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1', string)

for match in matches:
    matches_list.append(match.group())
    if match.group(2) == match.group(3)[::-1]:
        count += 1
        valid_words.append(f'{match.group(2)} <=> {match.group(3)}')

if len(matches_list) <= 0:
    print("No word pairs found!")

if len(matches_list) > 0:
    print(f"{len(matches_list)} word pairs found!")
    if count > 0:
        print("The mirror words are:")
        print(", ".join(valid_words))
    else:
        print("No mirror words!")
else:
    print("No mirror words!")
