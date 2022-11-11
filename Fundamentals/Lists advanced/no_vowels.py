vowels = ['a', 'o', 'u', 'e', 'i']
word = input()
no_vowels_word = "".join([ch for ch in word if ch not in vowels])

print(no_vowels_word)