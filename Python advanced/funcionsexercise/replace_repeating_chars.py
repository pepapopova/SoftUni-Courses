text = input()
new_text = ""

for char in text:
    if len(new_text) > 0:
        if char != new_text[-1]:
            new_text += char
    else:
        new_text += char

print(new_text)