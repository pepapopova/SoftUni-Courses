from string import punctuation

with open('../even_lines/text.txt', 'r') as file, open('output.txt', 'w') as result:
    for index, line in enumerate(file):
        count_letters = 0
        count_punct_signs = 0
        punctuation_symbols = set(punctuation)
        for char in line:
            if char.isalpha():
                count_letters += 1
            elif char in punctuation_symbols:
                count_punct_signs += 1
        result.write(f'Line {index + 1}: {line.strip()} ({count_letters})({count_punct_signs})\n')