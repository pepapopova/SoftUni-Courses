n = int(input())
key_word = input()
new_list = []
key_list = []

for _ in range(n):
    current_word = input()
    new_list.append(current_word)

# for i in range(len(new_list) -1, -1, -1):
#     element = new_list[i]
#     if key_word not in element:
#         new_list.remove(element)
#     print(new_list)

for current_string in new_list:
    if key_word in current_string:
        key_list.append(current_string)

print(new_list)
print(key_list)

# for _ in range(n):
#     current_word = input()
#     new_list.append(current_word)
#     if key_word in current_word:
#         key_list.append(current_word)

