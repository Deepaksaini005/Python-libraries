import matplotlib.pyplot as plt
import numpy as np

x = ["A", "B", "C", "D"]
y = [20, 34, 30, 35]
z = [25, 32, 34, 20]

wi = 0.25
p = np.arange(len(x))  # the label locations

p1 = [i + wi for i in p]  # the label locations for second bar

p2 = [j + wi for j in p]  # the label locations for third bar


plt.xlabel("categories")
plt.ylabel("values")

plt.title("Category Values Comparison", fontsize=14)
plt.bar(p, y, width=wi, label='Y Values', color='blue', edgecolor='black')

plt.bar(p1, z, width=wi, label='Z Values', color='orange', edgecolor='black')
plt.bar(p2, y, width=wi, label='Y Values', color='green', edgecolor='black' )
plt.show()