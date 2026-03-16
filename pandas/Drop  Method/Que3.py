# Drop employees earning less than 50,000.
# Drop employees from the HR department.
#  Keep only those aged 30 or above and earning at least 60,000

import pandas as pd

data = {'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [22, 28, 35, 24, 40],
    'Salary': [45000, 55000, 60000, 30000, 70000],
    'Department': ['HR', 'IT', 'Finance', 'HR', 'Sales']
}

df = pd.DataFrame(data)