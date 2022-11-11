count = int(input())
elements = set()

# for _ in range(count):
#     current_elements = input().split()
#     for el in current_elements:
#         elements.add(el)

for _ in range(count):
    current_set = set(input().split())
    elements = elements.union(current_set)

for element in elements:
    print(element)