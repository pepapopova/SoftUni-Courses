rows = int(input())
matrix = []

# for i in range(rows):
#     row = [int(x) for x in input().split(", ")]
#     matrix.append(row)
#     even_matrix = [[x for x in row if x % 2 == 0] for row in matrix]
#
# print(even_matrix)

matrix = [[int(x) for x in input().split(", ")] for row in range(rows)]
print([[x for x in row if x % 2 == 0] for row in matrix])