import re

n = int(input())

for data in range(n):
    name_data = input()
    regex1 = re.findall(r'\b@[A-za-z]\|\b', name_data)
    print(regex1)
    age = re.findall(r'\b#[\d]\*\b', name_data)
    print(age)