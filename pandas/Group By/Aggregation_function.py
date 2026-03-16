# some aggrigation functions for group by operations are sum, mean , count , max , min etc. which are used to perform calculations on grouped data.


import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob",
                "Charlie"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance",
                     "HR"],
    "Salary": [50000, 60000, 70000, 55000, 65000, 72000]
}

df = pd.DataFrame(data)
department = df.groupby("Department")
# using sum() method to get the total salary for each department
total_salary = df.groupby("Department").sum()
print(total_salary)


# using count() method to get the number of employees in each department
employee_count = df.groupby("Department").count()
print(employee_count)       


# using max() method to get the maximum salary in each department
max_salary = df.groupby("Department").max()
print(max_salary)


# using mean() method to get the average salary in each department
mean_salary = df.groupby("Department")["Salary"].mean()
print(mean_salary)


