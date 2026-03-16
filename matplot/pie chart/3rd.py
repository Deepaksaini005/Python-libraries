import matplotlib.pyplot as plt

departments = ['R&D', 'Marketing', 'HR', 'IT', 'Operations']
budget = [50000, 30000, 10000, 20000, 40000]
plt.pie(budget, labels=departments)
plt.show()