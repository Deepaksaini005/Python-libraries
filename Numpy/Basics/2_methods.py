import numpy as np

a =np.random.randint(0,11,5)  #randint() generates random integers.
print(a)   # Generates an array of 5 random integers between 0 and 10



b = np.random.rand(5,2)  #rand() generates random floating-point numbers.
print(b) # Generates a 5x2 array of random float values between 0 and 1



#creating an array in numpy

arr= np.array([2,4,5] , dtype=bool )  # if in these array has 0 then its give false  forthat particular element 
print(arr)


#reshape method and arrange method  in nnumpy
c=np.arange(1,11).reshape(10,1)  # 10 is for row counnt and 1 for column count
print(c)


d= np.arange(1,16).reshape(5,3) 
print(d)