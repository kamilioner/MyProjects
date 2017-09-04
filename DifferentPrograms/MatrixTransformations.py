matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(matrix)
matrix.append([13, 14, 15, 16])
print(matrix)


def transform_matrix(a_matrix):
    matrix_tmp = []
    for i in range(len(a_matrix)):
        matrix_tmp.append([row[i] for row in a_matrix])
    return matrix_tmp

print(list(zip(*matrix)))
matrix = transform_matrix(matrix)
print(matrix)