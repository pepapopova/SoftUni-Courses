string = input()

list = string.split(" ")
new_list = []

for element in list:
    current_num = int(element)
    opposite_num = -current_num
    new_list.append(opposite_num)

print(new_list)

# nums = input().split(' ')
# new_list = []
#
# for num in nums:
#     new_list.append(-int(num))
#
# print(new_list)
