def get_magic_triangle(triangle_size):
    magic_triangle = [[1], [1, 1]]

    for row_index in range(3, triangle_size + 1):

        row_to_append = [j * 0 for j in range(row_index)]
        for col_index in range(len(row_to_append)):
            if col_index == 0 or col_index == len(row_to_append) - 1:
                row_to_append[col_index] = 1
            else:
                elem = magic_triangle[-1][col_index] + magic_triangle[-1][col_index - 1]
                row_to_append[col_index] = elem
        magic_triangle.append(row_to_append)

    return magic_triangle


def get_magic_triangle(n):
    output = []

    for row in range(n):
        line = []
        for col in range(row + 1):
            if col == 0:
                line.append(1)
            elif col == row:
                line.append(1)
            else:
                a = output[row - 1][col]
                b = output[row - 1][col - 1]
                line.append(a + b)

        output.append(line)

    return output


print(get_magic_triangle(8))