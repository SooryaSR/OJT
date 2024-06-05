import numpy as np

array =np.array([1,2,3,4,5,6,7,8,9])
split= np.split(array,3)
print(array)
print(split)

#multidimentional hor/vert

arr_2d =np.array([[1,2,3,4],[5,6,7,8]])

vsplit =np.hsplit(arr_2d,2)
print("splitted v:",vsplit)
