import numpy as np
#for in loop

arr_1D = np.array([1,2,3,4,5,6])
print("arr_1D:", arr_1D)

for elements in arr_1D:
    print(elements)

#2d
arr_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("arr_2D:", arr_2D)

# for rows in arr_2D:
#     print(rows)
#     for elements in rows:
#         print(elements)

#iterate without nesteed loop
for elements in np.nditer(arr_2D):
    print(elements)

#iterate with index

for index, elements in np.ndenumerate(arr_2D):
    print(f"index: {index}, Elements: {elements}",)