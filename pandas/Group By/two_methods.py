# use the first and the last  to see the value of  first or last item in each group  annd  size (number of items in each group).

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob" ,  "Charlie"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance","HR"],
    "Salary": [50000, 60000, 70000, 55000, 65000, 72000]
}


df = pd.DataFrame(data)
department = df.groupby("Department")

# using first() method to get the first item in each group
first_item = df.groupby("Department").first()
print(first_item)

# using last() method to get the last item in each group
last_item = df.groupby("Department").last()
print(last_item)

# using the size() method to get the size of each group
group_size = df.groupby("Department").size()
print(group_size)

