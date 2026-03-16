
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
# print(df)

new_data   = df.copy()  # it will create a copy of original data frame
print(new_data)

new_data.to_csv("employee_data.csv")  # it will save the new_data data frame to a csv file without index

import os
os.listdir()  # to verify that the file has been created