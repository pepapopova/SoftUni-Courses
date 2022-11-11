names_list = input().split(", ")

# names_list.sort()
# sorted_list = sorted(names_list, key= lambda name: -len(name))
# print(sorted_list)

sorted_list = sorted(names_list, key=lambda name: (-len(name), name))
print(sorted_list)