rows, columns = [int(x) for x in input().split(" ")]
word = input()

index = 0

for row in range(rows):
    elements = [None] * columns
    # if row % 2 == 0:
    #     for col in range(columns):
    #         elements[col] = word[index % len(word)]
    #         index += 1
    # else:
    #     for col in range(columns - 1, -1, -1):
    #         elements[col] = word[index % len(word)]
    #         index += 1
    start, end, step = (0, columns, 1) if row % 2 == 0 else (columns - 1, -1, -1)
    for col in range(start, end, step):
        elements[col] = word[index % len(word)]
        index += 1

    print(''.join(elements))


