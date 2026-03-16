import matplotlib.pyplot as plt
from matplotlib import style

subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Art']
student_marks = [ 55, 67, 45, 70, 89, 90, 76, 88]
average_marks = [ 60, 65, 50, 68, 75, 80, 70, 85]
style.use('dark_background')

plt.axis([0,5 , 0,90])
plt.figure(figsize=(10,6))

plt.plot(subjects, student_marks, linestyle='--' , label='Student Marks' )

plt.plot(subjects, average_marks, linestyle='--' , label='Average Marks' )
plt.legend( )
plt.show()

