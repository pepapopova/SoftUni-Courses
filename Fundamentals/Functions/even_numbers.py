# sequence = input().split(" ")
#
#
# def even_numbers(list):
#     new_list = []
#     for num in list:
#         current_num = int(num)
#         if current_num % 2 == 0:
#             new_list.append(current_num)
#     print(new_list)
#
#
# even_numbers(sequence)

# sequence = map(int, list(input().split(" ")))
#
#
# def even_numbers(list):
#     new_list = []
#     for num in list:
#         if num % 2 == 0:
#             new_list.append(num)
#     print(new_list)
#
#
# even_numbers(sequence)

result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(" ")))))
print(result)