
# Task 1️⃣ Remove columns with more than 40% missing values

# Q2. Count missing values per column
# Check shape and info
# Q3. Percentage of missing values

# Task 2️⃣ Fill missing Age with median¶

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)


employee_ids = range(1001, 1041)
names = [f"Employee_{i}" for i in range(1, 41)]
departments = ['HR', 'IT', 'Finance', 'Sales', None]
locations = ['Delhi', 'Mumbai', 'Pune', 'Bangalore', None]


raw_data = {
'EmployeeID': employee_ids,
'Name': names,
'Age': [25, 28, None, 32, 30, None, 45, 38, None, 29,
41, None, 35, 26, None, 33, 39, None, 27, 31,
None, 36, 40, None, 34, 28, None, 37, 42, None,
29, 44, None, 26, 35, None, 38, 41, None, 30],
'Department': [departments[i % 5] for i in range(40)],
'Salary': [50000, 62000, None, 58000, 54000, None, 75000, 68000, None, 56000,
72000, None, 65000, 51000, None, 60000, 70000, None, 52000, 59000,
None, 66000, 71000, None, 63000, 55000, None, 69000, 74000, None,
57000, 73000, None, 50000, 64000, None, 68000, 72000, None, 56000],
'Experience': [2, 4, 6, None, 3, 5, 20, 12, None, 4,
15, None, 10, 1, None, 8, 18, None, 2, 6,
None, 11, 16, None, 9, 3, None, 14, 19, None,
5, 17, None, 1, 10, None, 13, 15, None, 4],
'Location': [locations[i % 5] for i in range(40)],
'Status': ['Active', 'Active', 'Inactive', 'Active', 'Active'] * 8
}


df = pd.DataFrame(raw_data)
print(df.shape) 
print(df.info())
print(df.isnull().sum())  # for missing  values per column 
print(df.isnull().mean()*100)  # percentage of missing values

# Remove columns with more than 40% missing values
col_drop = df.isna().mean()[df.isna().mean() > 0.4].index
df_clean = df.drop(columns=col_drop)
print(df_clean)

# Task 2️⃣ Fill missing Age with median¶

Age_median = df["Age"].median()
fill_age = df["Age"].fillna(Age_median)
print(fill_age)
print(Age_median)

# Task 3️⃣ Fill missing Salary using backward fill

fill_salary =  df["Salary"].fillna(method ='bfill')
print(fill_salary)


# Task 4️⃣ Fill missing Experience using forward fill
fill_Experience = df["Experience"].fillna(method ='ffill')
print(fill_Experience)

# Task 5️⃣ Fill missing Department and Location

fill_department = df["Department"].fillna('Unknown')
print(fill_department)

fill_location = df["Location"].fillna('Unknown')
print(fill_location)


#line chart of employee id and salary


x = df['EmployeeID']
y = df['Salary']
plt.plot(x,y)
plt.xlabel('Employee ID')
plt.ylabel('Salary')
plt.show()


# Bar chart department vs employee id 


df['Department'].value_counts().plot(kind='bar')
plt.title('Employee Count by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()



# create a graph according  to the average salary  and department
 
avg_salary = df.groupby("Department")["Salary"].mean()
plt.bar(avg_salary.index, avg_salary.values)
plt.title(' Graph of Average Salary by Department')
plt.xlabel(' Average Salary')
plt.ylabel(" Department")
plt.show()

