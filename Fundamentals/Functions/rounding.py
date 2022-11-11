given_list = input().split(" ")


def rounded_numbers(some_list):
    new_list = []
    for num in some_list:
        current_num = float(num)
        rounded_num = round(current_num)
        new_list.append(rounded_num)
    return new_list


print(rounded_numbers(given_list))

