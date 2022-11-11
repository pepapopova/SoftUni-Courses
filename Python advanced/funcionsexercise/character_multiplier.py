words = input().split(" ")
total_sum = 0
if len(words[0]) > len(words[1]):
    first_word = words[0]
    second_word = words[1]
else:
    first_word = words[1]
    second_word = words[0]

for i in range(len(first_word)):
    if i >= len(second_word):
        total_sum += ord(first_word[i])
    else:
        total_sum += ord(first_word[i]) * ord(second_word[i])

print(total_sum)
