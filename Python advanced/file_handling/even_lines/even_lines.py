to_be_replaced = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for char in result:
                if char in to_be_replaced:
                    result = result.replace(char, '@')
            print(result)