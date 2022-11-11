def even_odd(*args):
    command = args[-1]
    filtered_list = []
    parity = 0 if command == 'even' else 1
    for el in args[:-1]:
        if el % 2 == parity:
            filtered_list.append(el)
    return filtered_list

# def even_odd(*args):
#     command = args[-1]
#     filtered_list = []
#     for el in args[:-1]:
#         filtered_list.append(el)
#     if command == "even":
#         filtered_list = [x for x in filtered_list if x % 2 == 0]
#     else:
#         filtered_list = [x for x in filtered_list if x % 2 != 0]
#     return filtered_list

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))