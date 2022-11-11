

def skip_rope(keyword):
    num_list = []
    non_numbers = []
    for char in keyword:
        if char.isdigit():
            num_list.append(char)
        else:
            non_numbers.append(char)
    num_list = [int(x) for x in num_list]
    take_list = []
    skip_list = []
    for index in range(len(num_list)):
        if index % 2 == 0:
            take_list.append(num_list[index])
        else:
            skip_list.append(num_list[index])
    new_word = ""
    key_word = "".join(non_numbers)
    for n in range(len(take_list)):
        new_word += key_word[:take_list[n]]
        key_word = key_word[take_list[n]:]
        key_word = key_word[skip_list[n]:]
    print(new_word)


string = input()
skip_rope(string)