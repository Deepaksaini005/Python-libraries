# code for  binary search algorithm

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1
arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, target)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
    
    # other method 
    
import numpy as np 
arr = np.array([2, 3, 4, 10, 40])
target = 10
index = np.searchsorted(arr, target)
if index < len(arr) and arr[index] == target:
    print("Element is present at index", index)
else:
    print("Element is not present in array")
    
    