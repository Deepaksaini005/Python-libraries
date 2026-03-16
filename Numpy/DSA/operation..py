
#operations (additions , subtraction , multiplication , division) on arrays
import numpy as np

a = np.arange(4).reshape(2,2)
b = np.arange(4,8).reshape(2,2)

print("Array a:\n",a)
print("Array b:\n",b)
# addition
print("Addition:\n",a + b)
# subtraction
print("Subtraction:\n",a - b)
# multiplication
print("Multiplication:\n",a * b)
# division
print("Division:\n",a / b)

#transpose of an array
print("Transpose of a:\n",a.T)

