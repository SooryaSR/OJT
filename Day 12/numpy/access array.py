import numpy as np
array_2D =np.array([[1,2,3],[4,5,6]])

#acessing  a single element

element = array_2D[1,2]
print("element at the index of [1,2]",element)

#accessin second element of the first array
element= array_2D[0,1]
print("element of [0,1] : ",element)

#accessing row wise elements

row = array_2D[1:]
print("2nd row:", row)

#accessing first row

row = array_2D[0,:]
print("1st row:", row)

column = array_2D[:,1]
print("2nd column:",column)

column = array_2D[:,2]
print("2nd column:",column)

#slicing
#access the subarray with rows of 0 and 1, column of 1 and 2

slice_array = array_2D[0:2,1:3]
print("subarray", slice_array)


