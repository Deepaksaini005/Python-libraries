import numpy as np

a = np.linspace(0,101,50)  #here 50 is the no. of elements that wants in the output 
print(a)

z =  np.zeros(4 ,  dtype=int)  #  zeros here is the  method that give the zero values .  here "dtype = int" for that give the zeros in integer form not in floating  value . 
print(z)

o =  np.ones(3)  # ones is the method to give the 1 in the output .
print(o)


f = np.full(5 , 2)  #  here 5 is the no. of values that  comes in that quantity and 2 is comes no. of times  of that quantity . 


#np.full() is a NumPy function used to create an array of a given shape filled with a specified constant value.
print(f)