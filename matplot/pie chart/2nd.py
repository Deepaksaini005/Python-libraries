import matplotlib.pyplot as plt
subjects = ['Art', 'Science', 'English', 'History', 'Math']
students = [15, 35, 25, 20, 45]

# gradiant of red, blue , gold , purple

color= ["#836D69" , "#333536" , "#F1EAD2" , "#201F22" , "#413D3F"]

plt.pie(students, labels=subjects ,explode=[0,0,0,0,0.4], colors=color, autopct = "%1.2f%%" , startangle= 90,  shadow=True , radius=0.7 , labeldistance=2 , textprops={'fontsize': 15 , 'color': 'black'} , wedgeprops={'edgecolor': 'black' , 'linewidth': 2 , "edgecolor" : "b"})

# wedgeprops is used to set the properties of wedge like edgecolor , linewidth etc.

# textprops is used to set the properties of text like fontsize , color etc.

# labeldistance is used to set the distance between the center of pie chart to the label

# radius is used to increase or decrease the size of pie chart

# shadow is used to give shadow effect 

#autopct is used to show percentage on pie chart

#startangle is used to rotate the pie chart

plt.show()
