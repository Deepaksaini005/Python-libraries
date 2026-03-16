#Apply  slicinng to both the rows and columnn .

import pandas as pd
data = {
    "A": [10, 20, 30, 40],
    "B": [50, 60, 70, 80],
    "C": [90, 100, 110, 120]
}
df = pd.DataFrame(data)
# Slicing first three rows and first two columns
df_sliced = df.loc[:2, "A":"B"]
print(df_sliced)
