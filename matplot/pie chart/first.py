import matplotlib.pyplot as plt
x = [10,20,40,40,50]
y = ["C++","C","Java","JavaScript","Python"]
e = [0,0.3,0,0.1,0]
plt.pie(x, labels =y  , explode=e , colors=["blue", "yellow", "orange", "purple", "red"]) #explode is used to highlight a particular section
plt.show()

