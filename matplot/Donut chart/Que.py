import matplotlib.pyplot as plt
Subjects = ['Math', 'Science', 'English', 'History', 'Art']
students = [40, 35, 25, 20, 15]

plt.pie(students , labels =Subjects , autopct="%1.2f%%" , startangle=90)   
plt.legend(loc =1 )
plt.show()