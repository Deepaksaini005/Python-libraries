import matplotlib.pyplot as plt

x  = [1,2,3,4,5]
y = [10,15,16,17,20]
color   = ['red', 'blue', 'green', 'orange', 'purple']
size = [50, 100, 50, 20, 25]

plt.scatter(x, y, c = color, s=size)  # Plot the data

plt.title("Scatter Plot Example", fontsize=14 ,  color  ='blue')

plt.colorbar(label ='Color Scale')

plt.xlabel("X-axis Label", fontsize=12 , color ='red')

plt.ylabel("Y-axis Label", fontsize=12 , color ='green')
plt.show()