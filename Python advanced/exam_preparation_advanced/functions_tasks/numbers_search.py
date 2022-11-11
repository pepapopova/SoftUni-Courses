def numbers_searching(*args):
    result = sorted(set(args))
    duplicates = []
    final_result = []
    values = {}
    for num in args:
        if num not in values:
            values[num] = 0
        values[num] += 1
    for key, value in values.items():
        if value > 1:
            duplicates.append(key)
    for index in range(len(result)):
        if result[index] + 1 != result[index +1]:
            final_result.append(result[index] + 1)
            break
    final_result.append(sorted(duplicates))
    return final_result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))