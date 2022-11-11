values_list = input().split(" ")
absolute_list = []

for value in values_list:
    current_value = abs(float(value))
    absolute_list.append(current_value)

print(absolute_list)