# nditer is a powerful multi-dimensional iterator object to iterate over arrays in an efficient way.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for i in np.nditer(arr):
    print(i)
   

# Creating a 3D array

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d)

# Using nditer to iterate through the 3D array
for i in np.nditer(arr_3d):
    print(i)
    
    
# transpose method in numpy is used to interchange the rows and columns of an array.

arr_3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3.transpose())


