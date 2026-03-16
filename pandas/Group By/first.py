# group by method is used to group the data based on a specific column or columns.
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "Charlie"],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 70000, 55000, 65000, 72000]
}

df = pd.DataFrame(data)
department = df.groupby("Department")
print(department)


# using loop to print group data

for name , group in department:   # bcs department is df.groupby("Department")
    print(f"Department: {name}")
    print(group)
    
    
# #using the get group() method to retrieve a specific group

it_group = df.groupby("Department").get_group("IT")
print(it_group)
  
  
  
          # display the multiple Groups . 
Multi_group = df[df["Department"].isin(["HR", "IT"])]  
print(Multi_group)


# other method for this  using lambda function
multi_group_lambda = df.groupby("Department").filter(lambda x: x.name in ["HR", "IT"])
print(multi_group_lambda)