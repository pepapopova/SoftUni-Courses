string = input().split(", ")
substring = input()
new_list = []

for word in string:
    if word in substring:
        new_list.append(word)
# new_list = [x for x in string if x in substring]

print(new_list)