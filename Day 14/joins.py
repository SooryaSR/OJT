import numpy as np 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

concat = np.concatenate((arr1,arr2))
print(concat)

arr2D_1 =np.array([[1,2,3],[4,5,6]])
arr2D_2 =np.array([[7,8,9],[10,11,12]])
vstack_array =np.vstack((arr2D_1,arr2D_2))
hstack_array =np.hstack((arr2D_1,arr2D_2))

print("vertically:",vstack_array)
print("horizontally:",hstack_array)

