import matplotlib.pyplot as plt
import  numpy as np

x = np.arange(10)
plt.subplot(2,1,1)  # syntex - row , column , position 
plt.plot(x,x**2)
plt.show()


x = np.arange(10)
plt.subplot(2,1,2)  # syntex - row , column , position 
plt.plot(x,x**3)
plt.show()