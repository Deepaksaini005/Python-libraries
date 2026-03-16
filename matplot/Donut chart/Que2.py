# Create a donut chart and highlight the highest budget department.

import matplotlib.pyplot as plt
departments = ['R&D', 'Marketing', 'HR', 'IT', 'Operations']
budget = [50000, 30000, 10000, 20000, 40000]

bug = max(budget)

e = [0.3 if b == bug else 0 for b in budget]

plt.pie(budget , labels=departments, autopct="%1.0f%%", explode = e)

Circle  =  plt.Circle( (0,0) , 0.5 , facecolor='white' )
plt.gca().add_artist(Circle)
plt.show()