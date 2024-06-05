#converting id into 2D
#.reshape() is the method which is used for reshaping the arrays.

import numpy as np
array_1D = np.array([1,2,3,4,5,6])
print("array 1D:",array_1D)
print("shape of array1D:", array_1D.shape)

#reshaping the 1d array to 2D array

array_2D = array_1D.reshape((2,3))
print("2D array:",array_2D)
print("shape of the array_2D: ", array_2D.shape)

array_3D = array_1D.reshape((3,2))
print("3D array:",array_3D)
print("shape of the array_3D: ", array_3D.shape)


#reshaping back 2D to 1D
array_1D_back =array_2D.reshape((1,6))
print("array_1D_back :",array_1D_back)
print("shape of the array_1D_back :", array_1D_back.shape)

array_1D_back =array_2D.reshape((-1))
print("array_1D_back :",array_1D_back)
print("shape of the array_1D_back :", array_1D_back.shape)

