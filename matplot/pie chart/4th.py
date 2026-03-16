
import matplotlib.pyplot as plt
subjects = ['Math', 'Science', 'English', 'History', 'Art']
students = [40, 35, 25, 20, 15]
e = [0, 0.2, 0.5, 0, 0.4]
c = ["#58271F" , "#3D96C3" , "#C1A032" , "#311D5A" , "#D63C89"]
plt.pie(students , labels = subjects , autopct="%1.2f%%" , startangle=0, explode=e , colors=c , counterclock=True )   # counterclock is used to set the direction of pie chart
plt.legend(loc =1 )  
plt.show()
