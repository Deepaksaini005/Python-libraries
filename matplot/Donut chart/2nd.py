import matplotlib.pyplot as plt
departments = ['R&D', 'Marketing', 'HR', 'IT', 'Operations']
budget = [50000, 30000, 10000, 20000, 40000]
plt.pie(budget , labels=departments)
Circle  =  plt.Circle( (0,0) , 0.5 , facecolor='white' )
plt.gca().add_artist(Circle)
plt.legend(loc=1)
plt.show()