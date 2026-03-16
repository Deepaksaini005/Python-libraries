import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 60000, 70000, 80000],
    "Department": ["HR", "Finance", "IT", "Marketing"]
}

df = pd.DataFrame(data)

df_filtered = df[(df["Salary"] > 50000) & (df["Age"] > 25)]

print(df_filtered)
