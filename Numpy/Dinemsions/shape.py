import numpy as np

#shape method is used to give the shape of the array in which  no. of dimensions, no. of rows and no. of columns.

# ex -  (1,3,5)   # here  1 is no. of dimensions , 3 is no. of rows and 5 is no. of columns.


array = np.array([[['A','B','C'],['D','E','F'],['G','H','I'],
                   ['J','K','L'],['M','N','O'],['P','Q','R'],
                   ['S','T','U'],['V','W','X'],['Y','Z','a']]])



print(array.shape)  # Output: (1, 9, 3)


print(array.ndim)  # Output: 3

print(array[0][1][0]+array[0][1][1]*2 + array[0][5][0]+array[0][0][0]+array[0][3][1])  #output : Deepak

#these  method is concnate the particular elements of the array according to the index value.



# Another Example

new_array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                       [['J','K','L'],['M','N','O'],['P','Q','R']],
                       [['S','T','U'],['V','W','X'],['Y','Z','a']]]) 

print(new_array.shape)  # Output: (3, 3, 3)

print(new_array[1][0][1]+new_array[0][2][2]+new_array[1][1][0])