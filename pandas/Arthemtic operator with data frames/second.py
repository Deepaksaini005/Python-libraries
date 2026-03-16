import pandas as pd
#multiplying two columns of a dataframe
a = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(a)

df["c"] = df["a"] * df["b"]
print(df)

#also use other arthmetic operators like - , / , % , // , **