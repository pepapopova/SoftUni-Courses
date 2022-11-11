# def get_primary(matrix):
#     primary = [matrix[i][i] for i in range(len(matrix))]
#     return primary
#
# def get_secondary(matrix):
#     secondary = []
#     for row in range(len(matrix)):
#         secondary.append(matrix[row][len(matrix) - row - 1])
#     return secondary

size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

# primary_diagonal = get_primary(matrix)
# secondary_diagonal = get_secondary(matrix)

primary_diagonal = []
secondary_diagonal = []

for index in range(size):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][size - 1 - index])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")