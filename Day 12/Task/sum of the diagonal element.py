#Calculate the sum of the diagonal elements of a NumPy array 3*3 and 4*4

import numpy as np

matrix_3x3 = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])

matrix_4x4 = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]])

diagonal_sum_3x3 = np.trace(matrix_3x3)
diagonal_sum_4x4 = np.trace(matrix_4x4)

print("Sum of the diagonal elements of the 3x3 matrix:", diagonal_sum_3x3)
print("Sum of the diagonal elements of the 4x4 matrix:", diagonal_sum_4x4)
