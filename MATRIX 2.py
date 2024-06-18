import numpy as np

# Define the matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Sum of rows
sum_rows = np.sum(matrix, axis=1)

# Sum of columns
sum_columns = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)
print("\nSum of rows:")
print(sum_rows)
print("\nSum of columns:")
print(sum_columns)