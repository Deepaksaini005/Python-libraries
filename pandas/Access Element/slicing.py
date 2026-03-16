import pandas as pd


a = {"name": ["Alice", "Bob", "Charlie"], "city": ["New York", "Los Angeles", "Chicago"], "birth_year": [1995, 1990, 1985], "role": ["son", "father", "grandfather"]}
df =  pd.DataFrame(a, index=["A", "B", "C"])

df.loc["A":"C" , "name":"city"]  # Slicing rows from "A" to "C" and columns from "name" to "city"
print(df)