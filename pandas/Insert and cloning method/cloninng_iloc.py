import pandas as pd

data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
}

df = pd.DataFrame(data)

# Using iloc do slicing .

df["Slice_iloc"] = df.iloc[:2, 2]  # Slicing the first two rows of column c using iloc and assigning to new column Slice
print(df)