import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12, 13,14,15]
y = [40, 50.5 , 79.6 , 90.4 , 50, 30, 20, 10, 60, 70, 80, 85, 95, 100, 70]

color = ['red', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'cyan', 'magenta', 'yellow', 'black', 'grey', 'lime', 'navy', 'teal']

plt.scatter(x, y, c=color,marker="x" ,)  # Plot the data
plt.title("Scatter Plot with Multiple Colors", fontsize=14, color='blue')
plt.xlabel("student number", fontsize=12, color='red')
plt.ylabel("marks obtained", fontsize=12, color='green')
plt.colorbar(label='Color Scale')
plt.xticks(range(1, 16 ,2))
plt.yticks(range(0, 101, 10))
plt.grid(True)
plt.show()