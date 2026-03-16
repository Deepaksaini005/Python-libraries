import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 16, 17, 20]

plt.plot(x, y)  # Plot the data
plt.show()



a = ["python", "java", "c++", "ruby"]
b = [20, 34, 30, 35]
plt.xlabel("subjects")
plt.ylabel("marks")
plt.bar(a,b)
plt.show()