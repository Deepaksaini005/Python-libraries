import pandas as pd 

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],    
    "Salary": [50000, 60000, 70000, 80000],
    "Department": ["HR", "Finance", "IT", "Marketing"]
}

# remove  the IT department

df = pd.DataFrame(data)
df_filtered = df[(df["Department"]!="IT")]
print(df_filtered)


# .isin method

df_filtered_isin = df[df["Department"].isin(["IT" , "HR"])]
print(df_filtered_isin)