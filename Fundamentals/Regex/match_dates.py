import re

names = input()
matches = re.findall(r'\b(\d{2})([-/.])([A-Z][a-z]{2})\2(\d{4}\b)', names)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

# import re
#
# names = input()
# matches = re.finditer(r'\b(?P<date>\d{2})(?P<separator>[-/.])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4}\b)', names)
# for match in matches:
#     print(f"Day: {match.group('date')}, Month: {match.group('month')}, Year: {match.group('year')}")