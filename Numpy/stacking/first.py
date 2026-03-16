import numpy as np

# stacking is used to join a sequence of arrays along a new axis.

# hstack  (horizontal stack) is used to stack arrays in sequence horizontally (column wise).

# vstack (vertical stack) is used to stack arrays in sequence vertically (row wise).

#stack method is used to join a sequence of arrays along a new axis.

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)
a3 = np.stack((a1,a2))
a4= np.hstack((a1,a2))
a5= np.vstack((a1,a2))

print("Stack" , a3)
print("hstack ",a4)
print("vstack ",a5)

