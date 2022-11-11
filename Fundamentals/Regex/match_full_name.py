import re

names = input()
matches = re.findall(r'\b[A-Z][a-z]{1,}\s[A-Z][a-z]{1,}\b', names)
print(" ".join(matches))