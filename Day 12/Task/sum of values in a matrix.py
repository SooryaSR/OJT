# Find the sum of values in a matrix

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

column_sum = np.sum(matrix, axis=0)
print("Sum of each column:", column_sum)

row_sum = np.sum(matrix, axis=1)
print("Sum of each row:", row_sum)
