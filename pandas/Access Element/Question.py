import pandas as pd
#Question 1 : How to set a specific value in a DataFrame using indexing? if  want to change grandfather to mother .


a = {"name": ["Alice", "Bob", "Charlie"], "city": ["New York", "Los Angeles", "Chicago"], "birth_year": [1995, 1990, 1985], "role": ["son", "father", "grandfather"]}
df =  pd.DataFrame(a, index=["A", "B", "C"])

df["role"][2] = "mother"  # Setting a specific value in the DataFrame
print(df)