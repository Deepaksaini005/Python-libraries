import pandas as pd 

data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6]
}
df = pd.DataFrame(data)

df["Slice"] =df["A"][:2]  # slicing the first two rows of column A and assigning to new column Slice
print(df)