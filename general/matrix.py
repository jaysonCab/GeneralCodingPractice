'''
A matrix is a 2 dimentional array
ALWAYS USES numpy library

Its always row by column
3 x 2    *     2 x 3
Column of first must be same as row of second
Then resulting matrix is row of first times column of second
'''
import numpy as np

# December 31st, 2024
# matrixA = np.array([
#     [2,5,7],
#     [1,2,3],
#     [7,8,2]
# ])

# matrixB = np.array([
#     [8,0,1],
#     [0,3,4],
#     [1,0,7]
# ])

# Addition and subtraction is very simple and straight forward
# print(matrixA+matrixB)

# Multiplication is different, you take the rows of the first matrix and multiply by the column of matrix b
# print(matrixA.dot(matrixB))

A = np.array([
    [1,2,3]
])

B = np.array([
    [1],
    [2],
    [3]
])

print(A.dot(B))

# A = np.array([
#     [3,1,4]
# ])

# B = np.array([
#     [4,3],
#     [2,5],
#     [6,8]
# ])

# print(A.dot(B))

# print(np.linalg.inv(A))

# 