import matplotlib.pyplot as plt
a = ["python", "java", "c++", "ruby"]
b = [20, 34, 30, 35]
plt.title("Student Marks" , fontsize=14)
plt.xlabel("subjects", fontsize=12)
plt.ylabel("marks" , fontsize=12)

plt.bar(a,b , width=0.4 , color =('red' , 'blue' , 'green' , 'orange') ,linestyle='--' , edgecolor='black' )
plt.show()