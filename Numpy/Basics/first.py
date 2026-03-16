import numpy as np

a = np.array([1, 2, 3, 4, "hii"])
print(a)

# Use dtype=object for ragged / inhomogeneous nested lists
b = np.array([[1, 2, 3, 4], [10, 20, 30, 40]])
print(b)

c = np.array([[[1, 2, 3], [10, 20, 30], [40, 50, 60]]])
print(c)