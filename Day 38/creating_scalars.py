
#python program explaining numpy.asscalar() function
#creating scalars in numpy

import numpy as edunet
in_arr=edunet.array([8])
print("input array:",in_arr)
out_scalar = edunet.isscalar(in_arr)
print("output scalar from input array:",out_scalar)

#creating vector in numpy
import numpy as np
list1=[1,2,3]
list2=[[10],
       [10],
       [10]]
vector1=np.array(list1)
vector2=np.array(list2)

print("horizontal vector")
print(vector1)

print("vertical vector")
print(vector2)


#creating matrix in numpy
import numpy as edunet
a=edunet.matrix('1 2;3 4')
print("via string input:\n",a,"\n\n")
b=edunet.matrix([[5,6,7],[4,6,7]])
print("via array_like input:\n",b)

import numpy as np
mat1=([1,6,5],[3,4,8],[2,12,3])
mat2=([3,4,6],[5,6,7],[6,56,7])
res=np.dot(mat1,mat2)
print(res)