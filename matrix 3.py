def sum_diagonal(matrix):
    sum = 0
    for i in range (len(matrix)):
        sum += matrix[i][i]
    return  sum

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print("MATRIX:")
for row in matrix:
    print(row)

print("Sum of diagonal elements:", sum_diagonal(matrix))
