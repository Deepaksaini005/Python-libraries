import pandas as pd

# Creating a DataFrame with multiple columns and custom index labels
a = {"name": ["Alice", "Bob", "Charlie"], "city": ["New York", "Los Angeles", "Chicago"], "birth_year": [1995, 1990, 1985], "role": ["son", "father", "grandfather"]}
df =  pd.DataFrame(a, index=["A", "B", "C"])
# print(df)

# loc is used to access a group of rows and columns by labels or a boolean array.

print(df.loc["A"]) 

print(df.loc["B" , "role"])  # Accessing specific value at row "B" and column "role"


print(df.loc[["A", "C"], ["name", "city"]])  # Accessing multiple rows and columns
 
 
 
 
# iloc is used for integer-location based indexing for selection by position.
print(df.iloc[0])                                             