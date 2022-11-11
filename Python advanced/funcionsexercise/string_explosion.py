text = input()
text_list = [char for char in text]
index = -1
leftover = 0
removed = 0

for char in text_list:
    index += 1
    if char == ">":
        strength = leftover + int(text_list[index + 1])
        leftover = 0
        removed = 0
        for num in range(1, strength + 1):
            if index + 1 >= len(text_list):
                break
            if strength == 1:
                text_list.pop(index + 1)
            else:
                if text_list[index + 1] != ">":
                    text_list.pop(index + 1)
                    removed += 1
                else:
                    leftover += strength - removed
                    break


print("".join(text_list))

# for symbol in text_list[index: (index + strength)]:
        #     if symbol != ">":
        #         text_list.remove(symbol)
        #     else:
        #         strength +=

# index = 0
# for char in text:
#     if char == ">":
#         strength = int(text[text.index(char) + 1])
#         for sym in text[text.index(char):strength]:
#             if sym != ">":
#                 text.
