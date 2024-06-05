#Get the data type of an array object & Get the data type of an array containing strings


import numpy as np

array = np.array([1, 2, 3, 4, 5])
string_array = np.array(["apple", "banana", "cherry"])

array_dtype = array.dtype
string_array_dtype = string_array.dtype

print(f"The data type of the array is: {array_dtype}")
print(f"The data type of the string array is: {string_array_dtype}")
