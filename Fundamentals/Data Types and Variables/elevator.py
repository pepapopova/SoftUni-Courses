import math

persons = int(input())
capacity = int(input())

courses = persons // capacity
# courses = math.ceil(persons/capacity)
if persons % capacity != 0:
    courses += 1

print(courses)