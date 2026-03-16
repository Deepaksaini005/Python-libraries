# broadcasting in thenumpy library is  used to perform operations on arrays of different shapes 

import numpy as np

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4],[5]])
print(array1.shape)
print(array2.shape)



a3 = np.arange(12).reshape(4,3)
a4 =  np.arange(3).reshape(1,3)

print(a3.shape)
print(a4.shape)
print(a4)
print(a3*a4)  # here a4 is broadcasted to match the shape of a3 and then multiplication is performed element-wise

print("\n  addition example \n")

print(a3+a4)  