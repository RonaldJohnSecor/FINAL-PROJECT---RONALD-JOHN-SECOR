matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Initialize sum of diagonal elements
diagonal_sum = 0

# Iterate through each row and add diagonal elements
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            diagonal_sum += matrix[i][j]

print("Sum of diagonal elements:", diagonal_sum)