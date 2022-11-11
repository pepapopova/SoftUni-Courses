sequence_of_numbers = list(map(int, input().split(", ")))
max_value = 10
new_list = []
while len(sequence_of_numbers) > 0:
    filtered_nums = list(filter(lambda x: x <= max_value, sequence_of_numbers))
    print(f"Group of {max_value}'s: {filtered_nums}")
    for el in filtered_nums:
        if el in sequence_of_numbers:
            sequence_of_numbers.remove(el)
    new_list = []
    max_value += 10


# for nums in sequence_of_numbers:
#     if nums < max_value:
#         new_list.append(nums)
#         sequence_of_numbers.remove(nums)
#         print(f"Group of {max_value}'s: {new_list}.")
#         max_value += 10
#         new_list.clear()

