#get_keys method is used to get all the keys of the groups formed after grouping the data.

import  pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 70000, 55000, 65000, 72000]
}
df = pd.DataFrame(data)
department = df.groupby("Department")
keys = department.groups.keys()   # to get all the keys of the groups  
print(keys)


# position of  the group keys

position =df.groupby("Department").groups   #here groups is a dictionary where keys are the group names and values are the list of indices for each group

print(position)