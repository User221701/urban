def get_matrix(m,n,value):
    matrix = []
    if m <= 0 or n <= 0:
        return matrix
    for i in range(m):
        stroka = []
        for j in range(n):
            stroka.append(value)
        matrix.append(stroka)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
