import numpy as np


#ndim is used to check the dimension of the array

# 0D array
arr = np.array("A")
print(arr.ndim)  # Output: 0


#1 D  array
arr1 = np.array(["A", "B", "C"])
print(arr1.ndim)  # Output: 1 
#1D array has one dimension (a single row or column)

# 2D  array
arr2 = np.array([["A", "B", "C"], ["D", "E", "F"]])
print(arr2.ndim)  # Output: 2
#2D array has two dimensions (rows and columns)

# 3D array
arr3 = np.array([[["A","B"], ["C","D"], ["E","F"]]])
print(arr3.ndim)  # Output: 3
#3D array has three dimensions (depth, rows, and columns)