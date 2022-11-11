info = input().split(" ")
asci_list = []
for word in info:
    for char in word:
        if char.isdigit():
            asci_list.append(char)
            word = word[1:]
    new_list = [char for char in word]
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    word = "". join(new_list)
    asci_num = int("".join(asci_list))
    first_letter = chr(asci_num)
    word = first_letter + word[0:]
    asci_list.clear()
    print(word, end= " ")

# можем да я направим и като пазим числото с конкатинейт в стринг и после с word.replace(a, b) ги разменим