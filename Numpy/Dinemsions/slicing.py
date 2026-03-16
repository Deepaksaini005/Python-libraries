import numpy as np

#reshape  into 3 different  matrix 
#any 5 elements access 

numbers = np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]])


new_numbers = numbers.reshape(2,2,2,2)  #reshape into 3D array. 
print(numbers.ndim) # Output: 2D matrix
print(new_numbers)


print(new_numbers[1][0][1][1])  # Output: 8
print(new_numbers[0][1][0][0])  # Output: 9
print(new_numbers[1][1][0][1])  # Output: 14
print(new_numbers[0][0][1][0])  # Output: 5
print(new_numbers[1][1][1][0])  # Output: 15



number = np.arange(1,17)
print(number)