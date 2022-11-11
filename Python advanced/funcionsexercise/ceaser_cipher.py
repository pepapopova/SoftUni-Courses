text = input().strip()
new_word = [chr(ord(char) + 3) for char in text]
# new_word = ""
#
# for index in range(len(text)):
#     new_word += chr(ord(text[index]) + 3)

print("".join(new_word))