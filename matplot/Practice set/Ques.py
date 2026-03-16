import matplotlib.pyplot as plt
import numpy as np

ages = [18, 19, 20, 21, 22, 22, 23, 24, 25, 25,
        26, 27, 28, 28, 29, 30, 30, 31, 32, 33,
        34, 35, 36, 37, 38, 40, 42, 45, 48, 50]

subjects = ['Math', 'Science', 'English', 'History', 'Art']
students = [40, 35, 25, 20, 15]
boys = [22, 18, 12, 10, 8]
Girls = [18, 17, 13, 10, 7]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120, 150, 180, 160, 200, 220]


# Plot a bar graph showing number of students per subject.
plt.bar(subjects , students, color='skyblue')
plt.show()


# Create a histogram to show age distribution using 6 bins.
plt.hist(ages , bins =6 , color='lightgreen' , edgecolor='black')
plt.show()


# Plot a line graph showing monthly sales trend.
plt.plot(months , sales  , marker = "*" )
plt.show()

# Create a pie chart for subject distribution with percentages.
plt.pie(students  , labels = subjects , autopct='%1.1f%%' ,explode=[0.3,0,0,0,0] )
plt.show()


# Create a scatter plot of:

# x → ages
# y → random salaries

# 📌 Hint: np.random.randint()

x =  ages
y= np.random.randint( 20000 , 80000 , size = len(ages) )

plt.scatter(x,y , color =  'orange' , marker = "o" )
plt.xlabel("Ages")
plt.ylabel("Salaries")
plt.show()


# Q6. Bar vs Histogram
# Create two subplots:
# Left → Bar graph of age counts
# Right → Histogram of ages






# Q7. Line + Marker
# Plot sales with:
# markers
# grid
# title

plt.plot(sales , marker = "o"  , color = "purple" )
plt.grid()
plt.title("Monthly Sales Trend")
plt.show()


# Q8. Pie to Donut
# Convert the subject pie chart into a donut chart.
# 📌 Hint: plt.Circle()
plt.pie(students , labels = subjects )
Circle  =  plt.Circle((0,0),0.7, color='white')
plt.gca().add_artist(Circle)
plt.show()



# Q9. Multiple Lines

# Plot two line graphs on the same plot:
# sales
# cumulative sales
# 📌 Hint: np.cumsum()
plt.plot(sales , color = "red" )
cumulative_sales = np.cumsum(sales)
plt.plot(cumulative_sales , color = "blue" )
plt.show()

# Q10. Stacked Bar Chart :
# Create a stacked bar chart for:
# Boys vs Girls in subjects



subjects1 = ['Math', 'Science', 'English', 'History', 'Art']

boys = np.array([25, 20, 15, 10, 8])
girls = np.array([15, 15, 10, 10, 7])
gender = boys+girls
plt.bar(subjects1, boys , label='boys', color='orange')
plt.bar(subjects1, girls, bottom=boys, label = "Girls" , color='purple')
 # data in percentage 
plt.bar(subjects1, boys+girls, bottom=boys+girls, label = "Total" , color = "red" ) 

plt.title("Stacked Bar Chart")
plt.legend()
plt.grid()
plt.show()
