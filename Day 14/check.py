import numpy as np

array = np.array([10,13,16,84,66,44])
#np.where(array == 25)   //where()condition to filter & condition

#element greater than 16 for the above array

elements = np.where(array > 16, 0, array)
print(elements)
# print(array[elements])