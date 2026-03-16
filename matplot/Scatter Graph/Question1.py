import matplotlib.pyplot as plt


# make the best scatter plot for the employee , Departement and thier salary with proper labeling and title.


emply_id = [101, 102, 103, 104, 105]
departments = ['HR', 'Finance', 'IT', 'Marketing', 'Sales']
salaries = [50000, 60000, 75000, 55000, 65000]


plt.figure(figsize=(8,5))  # Set the figure size from x axis and y axis

plt.plot(emply_id, salaries, 'o', markersize=10, markeredgecolor='black', markerfacecolor='orange')

plt.title("Employee Salary by Department", fontsize=16, color='purple', fontweight='bold')
plt.xlabel("Employee ID", fontsize=12, color='red')
plt.ylabel("Salary (₹)", fontsize=12, color='green')

plt.tight_layout()
plt.show()
