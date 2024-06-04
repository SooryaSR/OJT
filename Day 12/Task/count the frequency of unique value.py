#How to count the frequency of unique values in NumPy array

import numpy as np

arr = np.array([1, 2, 3, 4, 1, 2, 3, 4, 5, 5, 5])

unique_values, counts = np.unique(arr, return_counts=True)

for value, count in zip(unique_values, counts):
    print(f"{value}: {count}")
