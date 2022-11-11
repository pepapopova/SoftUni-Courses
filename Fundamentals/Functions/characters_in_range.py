def characters(a, b):
    result = []
    for char in range(ord(a) + 1, ord(b)):
        result.append(chr(char))
    return " ". join(result)


char1 = input()
char2 = input()

print(characters(char1, char2))