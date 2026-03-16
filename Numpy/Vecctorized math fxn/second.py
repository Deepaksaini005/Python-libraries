# create an array and  calculate it radius .

import numpy as np

area = np.array([4, 9, 16, 25])    

# find the radius
radius = np.sqrt(area / np.pi)   # area = π * r^2
print(radius)
