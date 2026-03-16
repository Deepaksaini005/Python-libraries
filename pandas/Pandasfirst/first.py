import pandas as pd
a = {"name": ["Alice", "Bob", "Charlie"],
     "age": [25, 30, 35],}
df = pd.DataFrame(a)     

 #DataFrame is use to create a table. and df is  here for dataframe object

df = pd.DataFrame(a, index=["a", "b", "c"])
print(df)


df = pd.DataFrame(a, columns=["name"])
print(df)


df["country"] = ["USA", "UK", "Canada"]
print(df)