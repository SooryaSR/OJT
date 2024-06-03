import numpy as np
# create an orginal array

orginal_array =np.array([1,2,3,4,5,6])
print("org array:",orginal_array)

#view
view_array = orginal_array.view()
print("view of org array:",view_array)

view_array[2]=30
print("modified:",view_array)
print("orginal array after modifying the view:", orginal_array)

#copy array

copy_array = orginal_array.copy()
print("copy:",copy_array)

#modified elemenet in copy aray
copy_array[0]=10
print("modified copy array:",copy_array)
print("orginal array after modifying the copy array:", orginal_array)