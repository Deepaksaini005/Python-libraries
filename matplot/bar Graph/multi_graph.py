import matplotlib.pyplot as plt
import numpy as np

x = ["python", "java", "c++", "ruby"]
y = [20, 34, 30, 35]
z = [25, 32, 34, 20]


plt.xlabel("subjects")
plt.ylabel("marks")
plt.title("Student Marks" , fontsize=14)
wi = 0.25
p =np.arange(len(x))  # the label locations
p1 = [i + wi for i in p]  # the label locations for second bar

plt.legend()
plt.bar(x,y )
plt.bar(x,z)
plt.show()