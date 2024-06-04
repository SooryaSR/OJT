#How to inverse a matrix using NumPy

import numpy as np

matrix = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]])

inverse_matrix = np.linalg.inv(matrix)

print("Inverse of the matrix:")
print(inverse_matrix)
