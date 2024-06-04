#Counts the number of non-zero values in the array

import numpy as np

arr = np.array([1, 0, 2, 0, 3, 0, 4])
count = np.count_nonzero(arr)

print("Number of non-zero values:", count)
