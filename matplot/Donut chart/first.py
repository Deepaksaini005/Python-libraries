import  matplotlib.pyplot as plt

students = [40, 35, 25, 20, 15]

subjects = ['Math', 'Science', 'English', 'History', 'Art']

plt.pie(students, labels = subjects ,  wedgeprops={'edgecolor': 'black' } , autopct="%1.2f%%"  , pctdistance=0.4 )   
circle = plt.Circle( (0,0) , 0.5,facecolor='white' )  

# (0,0) is the center point and 0.5 is the radius of circle

# facecolor is used to fill the color of circle

plt.gca().add_artist(circle)
# gca means get current axis - it is used to get the current axis of pie chart

# add_artist is used to add the circle to pie chart
plt.show()