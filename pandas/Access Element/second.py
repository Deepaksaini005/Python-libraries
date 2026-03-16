import pandas as pd

# giving the condition through loc to filter the rows of dataframe .

a = {"name": ["Alice", "Bob", "Charlie"], "city": ["New York", "Los Angeles", "Chicago"], "birth_year": [1995, 1990, 1985], "role": ["son", "father", "grandfather"]}
df =  pd.DataFrame(a, index=["A", "B", "C"])

# print(df.loc[ df["birth_year"] > 1985 ])


df.loc[df["birth_year"] > 1985 , "role" ] = "Elder"  
print(df)