import numpy as np

array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

row_sums = np.sum(array, axis = 1)
print("The sum of elements in each row:  ", row_sums)

column_sums = np.sum(array, axis = 0)
print("The sum of elements in each column:  ", column_sums)

for row in array:
    print(f"{row}{np.sum(row)}")

print(" ".join(map(str, column_sums)))
