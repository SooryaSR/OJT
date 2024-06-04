# Find the number of rows and columns of a given matrix using NumPy

import numpy as np

matrix=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

row, columns = matrix.shape

print("number of row:",row)
print("number of column:",columns)

