# ravel method is used to create a flattened one-dimensional array view of a multi-dimensional array. it copy the data only if necessary.

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ravel())
