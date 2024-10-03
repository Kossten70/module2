def get_matrix(n, m, value):
    matrix = []
    for i in range(n):  # Перебор столбцов
        matrix.append([])
        for j in range(m):  # Перебор строк
            matrix[i].append(value)
    return matrix


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
