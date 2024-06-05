 #Change data type from float to integer by using 'i' as parameter value

import numpy as np

float_array = np.array([1.5, 2.3, 3.7, 4.1, 5.9])
int_array = float_array.astype('i')

print("Original float array:", float_array)
print("Converted integer array:", int_array)
print("Data type of converted array:", int_array.dtype)
