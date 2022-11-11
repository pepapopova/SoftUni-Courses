import re

places = input()

# matches = re.finditer('(?<=(=))[A-Z][a-zA-Z]{2,}(?=(=))|(?<=(/))[A-Z][a-zA-Z]{3,}(?=(/))', places)

# destinations = []
# points = 0
# for match in matches:
#     destinations.append(match.group())
#     points += len(match.group())
# # destinations = " ".join(matches)
# print(f"Destinations: {', '.join(destinations)}")
# print(f"Travel Points: {points}")

matches = re.finditer(r'([=/])([A-Z][a-zA-Z]{2,})\1', places)
destinations = []
points = 0
# for match in matches:
#     destinations.append(match.group()[1:len(match.group()) -1])
#     points += len(match.group()[1:len(match.group()) -1])

for match in matches:
    destinations.append(match.group(2))
    points += len(match.group(2))
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")