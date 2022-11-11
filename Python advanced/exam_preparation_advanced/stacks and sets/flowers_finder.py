from collections import deque

words = {
    "rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"
}

vowels = deque(input().split())
consonant = deque(input().split())
word_is_found = False

while vowels and consonant:
    first = vowels.popleft()
    second = consonant.pop()
    for flower in words:
        words[flower] = words[flower].replace(first, "")
        words[flower] = words[flower].replace(second, "")
        if words[flower] == "":
            word_is_found = True
            print(f"Word found: {flower}")
            break
    if word_is_found:
        break

if not word_is_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonant:
    print(f"Consonants left: {' '.join(consonant)}")