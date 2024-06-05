#Change data type from integer to boolean

import numpy as np

int_array = np.array([1, 0, 2, 0, 3])
bool_array = int_array.astype(bool)

print("Original integer array:", int_array)
print("Converted boolean array:", bool_array)
print("Data type of converted array:", bool_array.dtype)

