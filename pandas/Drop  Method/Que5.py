
# Print the DataFrame to observe where missing values exist.
# 👉 Goal: Visualize NaN locations.

# Use .isna().sum() to count missing values in each column.
# 👉 Goal: Understand data completeness.

# Use .notna().sum() to count how many non-missing values each column has.
# 👉 Goal: Practice .notna() for completeness check.

# Display all rows where Salary is not missing.
# 👉 Hint: df[df['Salary'].notna()]

# Show all employees whose Department and Salary are both available.
# 👉 Hint: Use .notna() with &.

import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Julia'],
    'Age': [25, 30, None, 28, 22, 35, None, 27, 31, None],
    'Department': ['HR', 'IT', 'Finance', None, 'IT', 'Finance', 'Sales', 'HR', 'Sales', None],
    'Salary': [50000, None, 60000, 48000, 52000, None, 57000, None, 59000, 61000],
    'Experience': [2, 5, 6, None, 1, 10, 7, 4, None, 8],
    'Location': ['New York', 'Los Angeles', 'Chicago', 'Miami', None, 'Dallas', 'Seattle', 'New York', 'Boston', 'Miami']
}

df = pd.DataFrame(data)


 #for question 1
df1 = df[df.isna().any(axis=1)]  # it will return all rows which has at least one missing value.
print(df1)

df_isna = df.isna().sum()   #for question 2
print(df_isna)


df_notna = df.notna().sum()   #for question 3
print(df_notna)


df_salary_notna = df[df["Salary"].notna()]   #for question 4
print(df_salary_notna)

