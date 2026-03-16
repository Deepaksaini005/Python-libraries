import matplotlib.pyplot as plt
import  numpy as np

# [np.sin  , np.cos , np.tan]

fig , ax = plt.subplots(2,2)

# fig :to call  the  object : Graph 

ax[0,0].plot([1,2,3],[1,4,9])
ax[0,1].plot([1,2,3],[1,4,9])
ax[1,0].plot([1,2,3],[1,4,9])
ax[1,1].plot([1,2,3],[1,4,9])
plt.show()
 
 
fig , ax  = plt.subplots(2,3)   
ax[0,0].plot([0,0,1] , [1,2,4])
ax[0,1].plot([0,1,1] , [1,2,4])
ax[0,2].plot([1,0,1] , [4,6,8])
ax[1,0].plot([1,0,1] , [1,3,5])
ax[1,1].plot([0,0,1] , [4,2,3])
ax[1,2].plot([0,0,1] , [2,4,6])
plt.show()


x = np.linspace(0,2*np.pi,100)

fig, ax = plt.subplots(1,3)

# Sin
ax[0].plot(x,np.sin(x))
ax[0].set_title("Sin Graph")

# Cos
ax[1].plot(x,np.cos(x))
ax[1].set_title("Cos Graph")

# Tan
ax[2].plot(x,np.tan(x))
ax[2].set_title("Tan Graph")

plt.show()






