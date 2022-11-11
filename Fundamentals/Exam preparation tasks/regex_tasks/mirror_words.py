import re
string = input()

matches = re.finditer(r'(#|@)([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1',string)
new_list = []
for match in matches:
    new_list.append(match.group())

valid_pairs = 0
mirror_words = []
for word in new_list:
    if '#' in word:
        new_word = word.split("#")
        if new_word[1] == new_word[3][::-1]:
            valid_pairs += 1
            mirror_words.append(word)
    elif "@" in word:
        new_word = word.split("@")
        if new_word[1] == new_word[3][::-1]:
            valid_pairs += 1
            mirror_words.append(word)

if len(new_list) <= 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{len(new_list)} word pairs found!")
    if len(mirror_words) <= 0:
        print("No mirror words!")
    else:
        print(f"The mirror words are:")
        print_list = []
        for word in mirror_words:
            if '#' in word:
                mirror_word = word.split("##")
                print_word = mirror_word[0][1:]
                print_list.append(f"{print_word} <=> {print_word[::-1]}")
            elif "@" in word:
                mirror_word = word.split("@@")
                print_word = mirror_word[0][1:]
                print_list.append(f"{print_word} <=> {print_word[::-1]}")

        print(", ".join(print_list))