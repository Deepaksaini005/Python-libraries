# insert is  used to insert values into an array at specified indices.

# syntex ---  np.insert(array,index,value,axis=None)

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
new_arr = np.insert(arr, 2, 10)  
print(new_arr)


# 2 D  array
 
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
new = np.insert(arr_2d , 1, 10, axis =1) #insert at column based on axis
print(new)

new2 = np.insert(arr_2d , 1, 10, axis =0) #insert at row based on axis
print(new2)