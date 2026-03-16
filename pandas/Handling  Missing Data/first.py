#method - fillna  - it is used to fill missing values in our data frame with a specified value.


import pandas as pd
import numpy as np

data = {
    'EmployeeID': range(201, 216),
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva',
             'Frank', 'Grace', 'Helen', 'Ian', 'Julia',
             'Kevin', 'Laura', 'Mike', 'Nina', 'Oscar'],
    'Age': [25, np.nan, 38, 29, np.nan,
            45, 32, np.nan, 41, 28,
            35, 50, np.nan, 27, 30],
    'Department': ['HR', 'IT', 'Finance', 'Sales', 'IT',
                   'Finance', np.nan, 'HR', 'Sales', 'IT',
                   'Sales', 'HR', 'Finance', 'HR', np.nan],
    'Salary': [50000, 60000, np.nan, 48000, 52000,
               np.nan, 57000, 54000, 59000, np.nan,
               61000, 63000, 58000, np.nan, 55000],
    'Experience': [2, 5, 10, np.nan, 1,
                   15, 7, 4, 12, 3,
                   8, 20, 6, np.nan, 9]
}

df = pd.DataFrame(data)
print(df)


df1 =df.fillna(0)  # it will fill all missing values with 0
print(df1)


df2 = df.fillna({
    "Age": df["Age"].mean()
    } )   # it will fill missing values in Age column with mean of that column
print(df2)


df3 = df.fillna(method="ffill")  # it will fill missing values with previous value in that column
print(df3)


df4 = df.fillna(method="bfill")  # it will fill missing values with next value in that column
print(df4)


df5 = df.fillna({
    "Age": df["Age"].mean(),
    "Department": "Unknown",
    "Salary": df["Salary"].mean()
})   # it will fill missing values in Age column with mean of that column , Department with "Unknown" and Salary with mean of that column
print(df5)