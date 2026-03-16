import pandas as pd


# Creating a DataFrame with multiple columns and custom index labels 

a = {"name": ["Alice", "Bob", "Charlie"], "city": ["New York", "Los Angeles", "Chicago"] , "birth_year": [1995, 1990, 1985] , "role":["son","father","grandfather"] }
df =pd.DataFrame(a , index = ["A" , "B" , "C"])

df["age"] = 2025 - df["birth_year"] 
print(df)


# The apply function is used to apply a function along an axis of the DataFrame.
df["age"] = df["birth_year"].apply(lambda x: 2025 - x)



# Adding a new column based on a condition using apply and lambda function for adult/minor .
df["age_adult"] = df["age"] .apply(lambda x: "adult" if x>=18 else "minor")
print(df)