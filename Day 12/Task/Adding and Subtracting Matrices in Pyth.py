#Adding and Subtracting Matrices in Python

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

add_result = A + B

subtract_result = A - B

print("Matrix A + Matrix B:")
print(add_result)

print("\nMatrix A - Matrix B:")
print(subtract_result)
