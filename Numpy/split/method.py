#split methos is  used to split the string into a list where each word is a list item
import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

a2 = np.split(a,3)
print(a2)


#hsplit is used to split the array into multiple sub-arrays horizontally (column wise).

a3 = np.hsplit(a,3)
print(a3)

#vsplit is used to split the array into multiple sub-arrays vertically (row wise).
a4 = np.vsplit(a,3)
print(a4)
